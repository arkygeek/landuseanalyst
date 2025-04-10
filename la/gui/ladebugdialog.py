#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debug dialog for Landuse Analyst - Singleton Pattern Implementation
"""
import os
from qgis.PyQt.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QPlainTextEdit, QPushButton, QCheckBox, QWidget, QLabel, QComboBox
)
from qgis.PyQt.QtCore import Qt, QSettings, QSize, QRect
from qgis.PyQt.QtGui import QFont, QTextCursor, QPainter, QColor
from la.lib.lautils import MESSAGE_BUS


class LineNumberArea(QWidget):
    """Line number area widget for QPlainTextEdit."""

    def __init__(self, editor):
        """Initialize with parent editor."""
        super().__init__(editor)
        self.editor = editor

    def sizeHint(self):
        """Return recommended size for the widget."""
        return QSize(self.editor.line_number_area_width(), 0)

    def paintEvent(self, event):
        """Paint the line numbers."""
        if not self.editor.show_line_numbers.isChecked():
            return

        # Set the background color
        painter = QPainter(self)
        painter.fillRect(event.rect(), QColor("#F0F0F0"))  # Light gray background

        # Paint the line numbers
        block = self.editor.firstVisibleBlock()
        block_number = block.blockNumber()
        top = int(self.editor.blockBoundingGeometry(block).translated(
            self.editor.contentOffset()).top())
        bottom = top + int(self.editor.blockBoundingRect(block).height())
        width = self.width() - 5  # Right margin

        # Maintain alignment with wrapped or unwrapped lines
        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                # Draw line number in red
                painter.setPen(QColor("#CC0000"))  # Red color
                painter.setFont(self.editor.font())
                painter.drawText(0, top, width, self.editor.fontMetrics().height(),
                                Qt.AlignRight, str(block_number + 1))

            block = block.next()
            top = bottom
            bottom = top + int(self.editor.blockBoundingRect(block).height())
            block_number += 1


class DebugTextEdit(QPlainTextEdit):
    """Enhanced QPlainTextEdit with line numbers."""

    def __init__(self, parent=None):
        """Initialize with parent."""
        super().__init__(parent)
        self.setReadOnly(True)
        self.setLineWrapMode(QPlainTextEdit.NoWrap)

        # Configure the editor
        font = QFont("Monospace")
        font.setStyleHint(QFont.TypeWriter)
        self.setFont(font)

        # Create line number area
        self.line_number_area = LineNumberArea(self)

        # This checkbox will be set by the parent dialog
        self.show_line_numbers = None

        # Connect signals
        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)

    def line_number_area_width(self):
        """Calculate the width of the line number area."""
        if not hasattr(self, 'show_line_numbers') or not self.show_line_numbers or not self.show_line_numbers.isChecked():
            return 0

        max_width = 0
        block_count = self.blockCount()

        # Calculate space needed for the highest line number
        digits = len(str(block_count))
        digits = max(digits, 2)  # At least 2 digits for aesthetics

        # Width = number of digits * width of a single digit + padding
        max_width = digits * self.fontMetrics().width('9') + 10

        return max_width

    def update_line_number_area_width(self):
        """Update the viewport margins to accommodate line numbers."""
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def update_line_number_area(self, rect, dy):
        """Update the line number area when the text view is scrolled."""
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            self.line_number_area.update(0, rect.y(), self.line_number_area.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width()

    def resizeEvent(self, event):
        """Handle resize events to update line number area."""
        super().resizeEvent(event)

        cr = self.contentsRect()
        self.line_number_area.setGeometry(QRect(cr.left(), cr.top(),
                                             self.line_number_area_width(), cr.height()))

    def toggle_line_numbers(self, show):
        """Toggle the display of line numbers."""
        self.update_line_number_area_width()
        self.line_number_area.update()


class LaDebugDialog(QDialog):
    """
    Non-modal debug dialog with proper Qt parenting and lifecycle management
    Implemented as a singleton to ensure only one instance exists
    """
    # Singleton instance
    _instance = None

    @classmethod
    def get_instance(cls, parent=None):
        """Get or create the singleton instance"""
        if cls._instance is None or not cls._instance.isVisible():
            # If instance doesn't exist or was closed, create a new one
            cls._instance = LaDebugDialog(parent)
        return cls._instance

    def __init__(self, parent=None):
        """Initialize with parent for proper window management"""
        super().__init__(parent)

        # Window configuration
        self.setWindowTitle("Landuse Analyst - Debug Log")
        self.setMinimumSize(800, 400)
        self.setWindowFlags(
            Qt.Dialog |
            Qt.WindowTitleHint |
            Qt.WindowCloseButtonHint |
            Qt.WindowMinMaxButtonsHint
        )

        # Do NOT set WA_DeleteOnClose as we want the singleton to persist

        # Restore saved size
        settings = QSettings()
        saved_size = settings.value("landuse_analyst/debug_dialog_size", QSize(800, 400))
        self.resize(saved_size)

        # UI setup
        self._setup_ui()

        # Connect signals - but check if already connected to avoid duplicates
        try:
            MESSAGE_BUS.debugMessaged.disconnect(self.add_debug_message)
        except TypeError:
            # Was not connected, which is fine
            pass

        MESSAGE_BUS.debugMessaged.connect(self.add_debug_message)

    def _setup_ui(self):
        """Initialize UI components"""
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add filter controls at the top
        filter_layout = QHBoxLayout()
        
        # Message type filter combo box
        from la.lib.lautils import LaUtils
        self.filter_combo = QComboBox(self)
        self.filter_combo.addItem("All Messages")
        
        # Get current component types and ensure important ones are included
        components = LaUtils.debug.getComponents()
        
        # Always include these important categories even if not in history
        important_types = ["Error", "Calculations", "Diet", "Animals", "Crops"]
        for item in important_types:
            if item not in components:
                components.append(item)
                
        self.filter_combo.addItems(sorted(components))
        self.filter_combo.currentTextChanged.connect(self.apply_filter)
        
        filter_layout.addWidget(QLabel("Filter by type:"))
        filter_layout.addWidget(self.filter_combo)
        filter_layout.addStretch()
        layout.addLayout(filter_layout)

        # Text area - using custom QPlainTextEdit with line numbers
        self.text_edit = DebugTextEdit(self)
        layout.addWidget(self.text_edit)

        # Button row
        button_layout = QHBoxLayout()

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_log)
        button_layout.addWidget(self.clear_button)

        self.auto_scroll = QCheckBox("Auto-scroll")
        self.auto_scroll.setChecked(True)
        button_layout.addWidget(self.auto_scroll)

        # Add line numbers checkbox
        self.show_line_numbers = QCheckBox("Show line numbers")
        self.show_line_numbers.setChecked(False)
        self.show_line_numbers.toggled.connect(self.toggle_line_numbers)
        button_layout.addWidget(self.show_line_numbers)

        # Assign line numbers checkbox to the text edit
        setattr(self.text_edit, 'show_line_numbers', self.show_line_numbers)

        # Add word wrap checkbox
        self.word_wrap = QCheckBox("Word wrap")
        self.word_wrap.setChecked(False)
        self.word_wrap.toggled.connect(self.toggle_word_wrap)
        button_layout.addWidget(self.word_wrap)

        button_layout.addStretch()

        self.copy_button = QPushButton("Copy All")
        self.copy_button.clicked.connect(self.copy_all)
        button_layout.addWidget(self.copy_button)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.hide)
        button_layout.addWidget(self.close_button)

        layout.addLayout(button_layout)

        # Load preferences from settings
        settings = QSettings()
        show_lines = settings.value("landuse_analyst/debug_show_line_numbers", False, type=bool)
        self.show_line_numbers.setChecked(show_lines)

        word_wrap = settings.value("landuse_analyst/debug_word_wrap", False, type=bool)
        self.word_wrap.setChecked(word_wrap)
        
        # Load saved filter preference
        saved_filter = settings.value("landuse_analyst/debug_message_filter", "All Messages")
        index = self.filter_combo.findText(saved_filter)
        if index >= 0:
            self.filter_combo.setCurrentIndex(index)

        # Initialize word wrap based on saved preference
        self.toggle_word_wrap(word_wrap)

    def add_debug_message(self, message: str):
        """Add message to log with auto-scroll handling and filter respect"""
        if not message:
            return

        # Check if message matches current filter
        current_filter = self.filter_combo.currentText()
        if current_filter != "All Messages":
            # Messages are in format "Component: Message"
            if not message.startswith(current_filter + ":"):
                return
        
        # Strip any HTML tags before displaying
        clean_message = self._strip_html_tags(message)
        self.text_edit.appendPlainText(clean_message)
        
        if self.auto_scroll.isChecked():
            cursor = self.text_edit.textCursor()
            cursor.movePosition(QTextCursor.End)
            self.text_edit.setTextCursor(cursor)

    def add_messages_from_history(self, messages_list: list):
        """Bulk load historical messages"""
        if not messages_list:
            return

        # Temporarily disable updates to improve performance
        self.text_edit.setUpdatesEnabled(False)

        # Strip HTML tags and add messages
        stripped_messages = [self._strip_html_tags(msg) for msg in messages_list]
        self.text_edit.appendPlainText("\n".join(stripped_messages))

        # Re-enable updates
        self.text_edit.setUpdatesEnabled(True)

        if self.auto_scroll.isChecked():
            cursor = self.text_edit.textCursor()
            cursor.movePosition(QTextCursor.End)
            self.text_edit.setTextCursor(cursor)

    def clear_log(self):
        """Clear all messages"""
        self.text_edit.clear()

    def copy_all(self):
        """Copy full log to clipboard"""
        self.text_edit.selectAll()
        self.text_edit.copy()
        cursor = self.text_edit.textCursor()
        cursor.clearSelection()
        self.text_edit.setTextCursor(cursor)

    def closeEvent(self, event):
        """Handle proper cleanup but preserve the singleton instance"""
        # Save size
        settings = QSettings()
        settings.setValue("landuse_analyst/debug_dialog_size", self.size())

        # Instead of closing, just hide the dialog and ignore the event
        self.hide()
        event.ignore()

        # Do NOT disconnect signals as we want to keep receiving them

    def toggle_line_numbers(self, checked):
        """Toggle line numbers visibility

        Args:
            checked: Whether line numbers should be shown
        """
        # Save the setting
        settings = QSettings()
        settings.setValue("landuse_analyst/debug_show_line_numbers", checked)

        # Update the line number area
        self.text_edit.toggle_line_numbers(checked)

    def toggle_word_wrap(self, checked):
        """Toggle word wrap setting

        Args:
            checked: Whether word wrap should be enabled
        """
        # Save the setting
        settings = QSettings()
        settings.setValue("landuse_analyst/debug_word_wrap", checked)

        # Update the text edit widget
        if checked:
            self.text_edit.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        else:
            self.text_edit.setLineWrapMode(QPlainTextEdit.NoWrap)

        # Update the line number area since line wrapping may change layout
        self.text_edit.update_line_number_area_width()
        self.text_edit.line_number_area.update()

    def apply_filter(self, filter_type: str):
        """Apply message type filter and update display.
        
        Args:
            filter_type: The message type to filter by, or "All Messages" for no filter
        """
        # Save the filter preference
        settings = QSettings()
        settings.setValue("landuse_analyst/debug_message_filter", filter_type)

        # Clear current display
        self.text_edit.clear()

        # Get filtered message history
        from la.lib.lautils import LaUtils
        messages = LaUtils.debug.getHistory(
            component_filter="" if filter_type == "All Messages" else filter_type,
            with_line_numbers=self.show_line_numbers.isChecked()
        )

        # Add filtered messages
        self.add_messages_from_history(messages)

    def _strip_html_tags(self, text):
        """Remove HTML tags from text for proper display in QPlainTextEdit.
        
        Args:
            text: Text containing HTML formatting
            
        Returns:
            Plain text without HTML tags
        """
        import re
        # Replace HTML color spans with their content
        text = re.sub(r'<span[^>]*>(.*?)</span>', r'\1', text)
        # Replace any other HTML tags
        text = re.sub(r'<[^>]*>', '', text)
        return text