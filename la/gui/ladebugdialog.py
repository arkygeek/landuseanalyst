#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debug dialog for Landuse Analyst - Singleton Pattern Implementation
"""
import os
import re
from typing import List, Dict, Optional

from qgis.PyQt.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QPlainTextEdit, QPushButton, QCheckBox, QWidget, QLabel,
    QScrollArea, QApplication, QTextEdit
)
from qgis.PyQt.QtCore import Qt, QSettings, QSize, QRect, pyqtSlot
from qgis.PyQt.QtGui import QPaintEvent, QResizeEvent, QFont, QPainter, QColor, QTextFormat, QCloseEvent, QTextCursor, QTextBlockFormat, QTextCharFormat

# la.lib.lautils contains MESSAGE_BUS and LaUtils.LaDebugLogger
from la.lib.lautils import MESSAGE_BUS, LaUtils

# --- Helper Widget for Line Numbers ---

class LineNumberArea(QWidget):
    """Line number area widget for DebugTextEdit."""

    def __init__(self, editor: 'DebugTextEdit'):
        """Initialize with parent editor."""
        super().__init__(editor)
        self.editor = editor
        self.setBackgroundRole(self.editor.backgroundRole())
        self.setAutoFillBackground(True)


    def sizeHint(self) -> QSize:
        """Return recommended size for the widget."""
        return QSize(self.editor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event: 'QPaintEvent'):
        """Paint the line numbers."""
        # Delegate painting to the editor
        self.editor.lineNumberAreaPaintEvent(event)

# --- Custom Text Edit with Line Numbers ---

class DebugTextEdit(QPlainTextEdit):
    """Enhanced QPlainTextEdit with line numbers."""

    def __init__(self, parent: Optional[QWidget] = None):
        """Initialize with parent."""
        super().__init__(parent)
        self.setReadOnly(True)
        self.setLineWrapMode(QPlainTextEdit.NoWrap) # Default no wrap

        # Configure the editor font
        myFont = QFont("Monospace")
        myFont.setStyleHint(QFont.TypeWriter)
        self.setFont(myFont)

        # Create line number area
        self.mLineNumberArea = LineNumberArea(self)

        # This checkbox will be set by the parent dialog after initialization
        self.mShowLineNumbersCheckbox: Optional[QCheckBox] = None

        # Initialize line number mapping
        self.mLineNumberMappings = []

        # Connect signals for updating line number area
        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine) # Optional: highlight current line

        # Initial update
        self.updateLineNumberAreaWidth()
        # self.highlightCurrentLine() # Uncomment if initial highlight is desired


    def lineNumberAreaWidth(self) -> int:
        """Calculate the width of the line number area."""
        if not self.mShowLineNumbersCheckbox or not self.mShowLineNumbersCheckbox.isChecked():
            return 0 # No width if line numbers are hidden

        myDigits = 1
        myMaxVal = max(1, self.blockCount())
        while myMaxVal >= 10:
            myMaxVal //= 10
            myDigits += 1

        # Calculate space needed for the highest line number + padding
        # Ensure at least 2 digits width for aesthetics
        mySpace = 5 + self.fontMetrics().horizontalAdvance('9') * max(myDigits, 2)
        return mySpace

    def updateLineNumberAreaWidth(self):
        """Update the viewport margins to accommodate line numbers."""
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, theRect: QRect, theVerticalScrollDelta: int):
        """Update the line number area when the text view is scrolled."""
        if theVerticalScrollDelta:
            self.mLineNumberArea.scroll(0, theVerticalScrollDelta)
        else:
            # Update the specific area that needs repainting
            self.mLineNumberArea.update(0, theRect.y(), self.mLineNumberArea.width(), theRect.height())

        if theRect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth()

    def resizeEvent(self, theEvent: 'QResizeEvent'):
        """Handle resize events to update line number area geometry."""
        super().resizeEvent(theEvent)
        myContentsRect = self.contentsRect()
        self.mLineNumberArea.setGeometry(QRect(myContentsRect.left(), myContentsRect.top(),
                                             self.lineNumberAreaWidth(), myContentsRect.height()))

    def lineNumberAreaPaintEvent(self, theEvent: 'QPaintEvent'):
        """Paint the line numbers in the line number area."""
        if not self.mShowLineNumbersCheckbox or not self.mShowLineNumbersCheckbox.isChecked():
            return # Don't paint if hidden

        painter = QPainter(self.mLineNumberArea)
        # Use a slightly different background for the line number area
        painter.fillRect(theEvent.rect(), QColor("#F0F0F0"))

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        # Get the top/bottom geometry relative to the viewport
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()
        height = self.fontMetrics().height()
        width = self.mLineNumberArea.width() - 5 # Right padding

        # Iterate over visible blocks
        while block.isValid() and top <= theEvent.rect().bottom():
            if block.isVisible() and bottom >= theEvent.rect().top():
                number = str(blockNumber + 1)
                painter.setPen(QColor("#FF0000")) # Red color for line numbers
                painter.setFont(self.font())
                painter.drawText(0, int(top), width, height, Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber += 1

    def highlightCurrentLine(self):
        """Optional: Highlight the background of the current line."""
        # This is optional styling and can be removed if not needed
        extraSelections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            lineColor = QColor(Qt.yellow).lighter(160)
            selection.format.setBackground(lineColor)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
        self.setExtraSelections(extraSelections)

    def toggleLineNumbers(self, show: bool):
        """Toggle the display of line numbers."""
        self.updateLineNumberAreaWidth()
        self.mLineNumberArea.setVisible(show) # Show/hide the widget itself
        self.mLineNumberArea.update() # Force repaint


# --- Main Debug Dialog ---

class LaDebugDialog(QDialog):
    """
    Non-modal debug dialog with filtering, line numbers, and auto-scroll.
    Implemented as a singleton to ensure only one instance exists.
    """
    _instance: Optional['LaDebugDialog'] = None

    @classmethod
    def get_instance(cls, parent: Optional[QWidget] = None) -> 'LaDebugDialog':
        """Get or create the singleton instance."""
        if cls._instance is None:
            print("Creating new LaDebugDialog instance")
            cls._instance = LaDebugDialog(parent)
        elif not cls._instance.isVisible():
             # If instance exists but is hidden, ensure it's properly parented and show
             print("Reusing hidden LaDebugDialog instance")
             if parent and cls._instance.parent() != parent:
                 cls._instance.setParent(parent) # Re-parent if necessary
             # cls._instance.show() # Optionally show immediately
        else:
             print("Returning visible LaDebugDialog instance")

        return cls._instance

    def __init__(self, parent: Optional[QWidget] = None):
        """Initialize with parent for proper window management."""
        if LaDebugDialog._instance is not None:
             # This should ideally not happen if get_instance is used correctly,
             # but serves as a safeguard against direct instantiation.
             raise RuntimeError("LaDebugDialog is a singleton, use get_instance()")

        super().__init__(parent)
        LaDebugDialog._instance = self # Register the instance

        # --- Internal State ---
        self.mMessages: List[str] = [] # Store raw messages received
        self.mFilterCheckboxes: Dict[str, QCheckBox] = {}

        # --- Window Configuration ---
        self.setWindowTitle("Landuse Analyst - Debug Log")
        self.setMinimumSize(800, 400)
        # Standard dialog flags allowing minimize/maximize/close
        self.setWindowFlags(
            Qt.Dialog |
            Qt.WindowTitleHint |
            Qt.WindowCloseButtonHint |
            Qt.WindowMinMaxButtonsHint
        )
        # Do NOT set WA_DeleteOnClose as we want the singleton to persist

        # Restore saved geometry (position and size)
        settings = QSettings()
        saved_geometry = settings.value("landuse_analyst/debug_dialog_geometry")
        if saved_geometry:
            self.restoreGeometry(saved_geometry)
        else:
             # Default size if no geometry saved
            self.resize(QSize(800, 400))

        # --- UI Setup ---
        self._setupUi()

        # --- Connect to Global Message Bus ---
        # Ensure clean connection
        try:
            MESSAGE_BUS.debugMessaged.disconnect(self.addDebugMessage)
        except TypeError:
            pass # Signal was not connected
        MESSAGE_BUS.debugMessaged.connect(self.addDebugMessage)

        # --- Load Initial State ---
        self._loadFilterPreferences() # Load which filters were checked
        self.applyFilters() # Apply filters to load initial history


    def _setupUi(self):
        """Initialize UI components and layout."""
        # Use a horizontal main layout
        mainLayout = QHBoxLayout(self)

        # ---- LEFT SIDE: FILTERS ----
        filterPanel = QWidget()
        filterPanel.setMaximumWidth(200) # Limit width of filter panel
        filterLayout = QVBoxLayout(filterPanel)
        filterLayout.setContentsMargins(5, 5, 5, 5) # Add some margin

        # Filter section title
        filterTitle = QLabel("<b>Message Types</b>")
        filterLayout.addWidget(filterTitle)

        # "Select All" checkbox
        self.mSelectAllCheckbox = QCheckBox("All Message Types")
        self.mSelectAllCheckbox.setChecked(True) # Start with all selected
        self.mSelectAllCheckbox.stateChanged.connect(self._toggleAllFilters)
        filterLayout.addWidget(self.mSelectAllCheckbox)

        # Scrollable area for filter checkboxes
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setFrameShape(QScrollArea.StyledPanel) # Add a subtle frame
        scrollWidget = QWidget()
        self.mFilterScrollLayout = QVBoxLayout(scrollWidget) # Store layout reference
        self.mFilterScrollLayout.setSpacing(2) # Compact spacing
        self.mFilterScrollLayout.setAlignment(Qt.AlignTop) # Align checkboxes to top

        # Add initial known components (sorted)
        initialComponents = sorted(LaUtils.debug.getComponents())
        for component in initialComponents:
            self._addFilterCheckbox(component)

        # Add stretch to push checkboxes to top when few items
        self.mFilterScrollLayout.addStretch(1)

        # Set up scrollable area
        scrollWidget.setLayout(self.mFilterScrollLayout)
        scrollArea.setWidget(scrollWidget)
        filterLayout.addWidget(scrollArea, 1) # Scroll area takes available vertical space

        # ---- RIGHT SIDE: TEXT AREA AND BUTTONS ----
        rightPanel = QWidget()
        rightLayout = QVBoxLayout(rightPanel)
        rightLayout.setContentsMargins(0, 5, 5, 5) # Match filter panel margins

        # Text area
        self.mTextEdit = DebugTextEdit(self)
        rightLayout.addWidget(self.mTextEdit, 1) # Text edit takes most space

        # --- Button Row ---
        buttonLayout = QHBoxLayout()
        buttonLayout.setSpacing(10)

        self.mClearButton = QPushButton("Clear")
        self.mClearButton.setToolTip("Clear the log display")
        self.mClearButton.clicked.connect(self._clearLog)
        buttonLayout.addWidget(self.mClearButton)

        self.mAutoScrollCheckbox = QCheckBox("Auto-scroll")
        self.mAutoScrollCheckbox.setToolTip("Automatically scroll to the bottom when new messages arrive")
        self.mAutoScrollCheckbox.setChecked(True)
        buttonLayout.addWidget(self.mAutoScrollCheckbox)

        self.mShowLineNumbersCheckbox = QCheckBox("Show line numbers")
        self.mShowLineNumbersCheckbox.setToolTip("Toggle visibility of line numbers")
        self.mShowLineNumbersCheckbox.toggled.connect(self._toggleLineNumbers)
        buttonLayout.addWidget(self.mShowLineNumbersCheckbox)

        # Link the checkbox to the text edit
        self.mTextEdit.mShowLineNumbersCheckbox = self.mShowLineNumbersCheckbox

        self.mWordWrapCheckbox = QCheckBox("Word wrap")
        self.mWordWrapCheckbox.setToolTip("Toggle word wrapping for long lines")
        self.mWordWrapCheckbox.toggled.connect(self._toggleWordWrap)
        buttonLayout.addWidget(self.mWordWrapCheckbox)

        buttonLayout.addStretch() # Push buttons to the right

        self.mCopyButton = QPushButton("Copy All")
        self.mCopyButton.setToolTip("Copy the entire log content to the clipboard")
        self.mCopyButton.clicked.connect(self._copyAll)
        buttonLayout.addWidget(self.mCopyButton)

        self.mCloseButton = QPushButton("Hide") # Changed text to "Hide"
        self.mCloseButton.setToolTip("Hide the debug window (does not close the application)")
        self.mCloseButton.clicked.connect(self.hide) # Use hide() directly
        buttonLayout.addWidget(self.mCloseButton)

        # Add button layout to right panel
        rightLayout.addLayout(buttonLayout)

        # Add panels to main layout
        mainLayout.addWidget(filterPanel)
        mainLayout.addWidget(rightPanel, 1) # Right panel takes more horizontal space

        # Load preferences from settings for checkboxes
        settings = QSettings()
        showLines = settings.value("landuse_analyst/debug_show_line_numbers", False, type=bool)
        self.mShowLineNumbersCheckbox.setChecked(showLines)
        # Ensure initial state matches checkbox
        self.mTextEdit.toggleLineNumbers(showLines)

        wordWrap = settings.value("landuse_analyst/debug_word_wrap", False, type=bool)
        self.mWordWrapCheckbox.setChecked(wordWrap)
        # Ensure initial state matches checkbox
        self._toggleWordWrap(wordWrap) # Call slot to apply wrap mode

    def _addFilterCheckbox(self, component: str):
        """Adds a checkbox for a given component type to the filter list."""
        if component in self.mFilterCheckboxes:
            return # Already exists

        checkbox = QCheckBox(component)
        checkbox.setChecked(True) # New filters default to checked
        checkbox.stateChanged.connect(self.applyFilters)

        # Insert checkbox alphabetically into the layout
        inserted = False
        for i in range(self.mFilterScrollLayout.count() - 1): # Exclude the stretch
            item = self.mFilterScrollLayout.itemAt(i)
            widget = item.widget()
            if isinstance(widget, QCheckBox) and widget.text() > component:
                self.mFilterScrollLayout.insertWidget(i, checkbox)
                inserted = True
                break
        if not inserted:
            # Insert before the stretch if not inserted alphabetically
             self.mFilterScrollLayout.insertWidget(self.mFilterScrollLayout.count() - 1, checkbox)

        self.mFilterCheckboxes[component] = checkbox


    @pyqtSlot(str)
    def addDebugMessage(self, message: str):
        """Slot to receive and process a new debug message."""
        # Store the raw message internally
        self.mMessages.append(message)

        # Check if the message's component type filter exists, add if not
        component = self._getComponentFromMessage(message)
        if component and component not in self.mFilterCheckboxes:
            self._addFilterCheckbox(component)
            # No need to re-apply all filters here, just check if the new type is active
            # (which it will be by default)

        # Check if the component of the new message is currently enabled in filters
        if component in self.mFilterCheckboxes and self.mFilterCheckboxes[component].isChecked():
            # If the filter for this message type is active, append it to the text edit
            is_at_bottom = False
            scrollbar = self.mTextEdit.verticalScrollBar()
            if self.mAutoScrollCheckbox.isChecked():
                # Check if scrollbar is near the bottom before appending
                is_at_bottom = scrollbar.value() >= (scrollbar.maximum() - 5)

            # Append the message (potentially with line number formatting)
            display_message = self._formatMessageForDisplay(message)
            self.mTextEdit.appendPlainText(display_message) # Use plain text to avoid formatting issues

            if self.mAutoScrollCheckbox.isChecked() and is_at_bottom:
                scrollbar.setValue(scrollbar.maximum()) # Scroll to bottom


    def _getComponentFromMessage(self, message: str) -> Optional[str]:
        """Extracts the component part (e.g., 'UI', 'Diet') from a raw message."""
        # Simple split, assumes "Component: Message" format
        parts = message.split(':', 1)
        if parts:
            return parts[0].strip()
        return None

    def _formatMessageForDisplay(self, message: str) -> str:
        """Formats a raw message for display (e.g., adding line numbers if enabled)."""
        # Currently, we just display the raw message as plain text.
        # If line numbers were added by the source, they would be part of the string.
        # If we wanted client-side line numbers (less reliable if filtered),
        # we would calculate the line number based on mTextEdit.blockCount() here.
        # For simplicity, let's assume line numbers are NOT added here.
        return self._stripHtmlTags(message) # Ensure clean display

    def _stripHtmlTags(self, text: str) -> str:
        """Remove HTML tags from text."""
        # Simple regex to remove tags - might need refinement for complex HTML
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def _saveFilterPreferences(self):
        """Save filter checkbox states to QSettings."""
        settings = QSettings()
        active_filters = [comp for comp, cb in self.mFilterCheckboxes.items() if cb.isChecked()]
        settings.setValue("landuse_analyst/debug_active_filters", active_filters)
        LaUtils.debug.log(f"Saved active filters: {active_filters}", "Debug")


    def _loadFilterPreferences(self):
        """Load saved filter checkbox states from QSettings."""
        settings = QSettings()
        active_filters = settings.value("landuse_analyst/debug_active_filters", [])
        LaUtils.debug.log(f"Loading active filters: {active_filters}", "Debug")

        # Block signals during update
        self.mSelectAllCheckbox.blockSignals(True)
        for checkbox in self.mFilterCheckboxes.values():
            checkbox.blockSignals(True)

        # If no saved filters, default to all checked
        if not active_filters:
             active_filters = list(self.mFilterCheckboxes.keys())
             for checkbox in self.mFilterCheckboxes.values():
                 checkbox.setChecked(True)
        else:
             for component, checkbox in self.mFilterCheckboxes.items():
                 checkbox.setChecked(component in active_filters)

        # Unblock signals
        for checkbox in self.mFilterCheckboxes.values():
            checkbox.blockSignals(False)
        self.mSelectAllCheckbox.blockSignals(False)

        # Update the "Select All" checkbox state
        self._updateSelectAllState()

    def _updateSelectAllState(self):
        """Update the 'Select All' checkbox based on individual filter states."""
        all_checked = True
        any_checked = False
        if not self.mFilterCheckboxes: # Handle case with no filters yet
            all_checked = False
        else:
            for checkbox in self.mFilterCheckboxes.values():
                if checkbox.isChecked():
                    any_checked = True
                else:
                    all_checked = False
                if any_checked and not all_checked: # Optimization
                    break

        # Block signals to prevent recursive calls
        self.mSelectAllCheckbox.blockSignals(True)
        if all_checked:
            self.mSelectAllCheckbox.setCheckState(Qt.Checked)
        elif any_checked:
            self.mSelectAllCheckbox.setCheckState(Qt.PartiallyChecked)
        else:
            self.mSelectAllCheckbox.setCheckState(Qt.Unchecked)
        self.mSelectAllCheckbox.blockSignals(False)

    @pyqtSlot(int)
    def _toggleAllFilters(self, state: int):
        """Toggle all individual filter checkboxes based on 'Select All' state."""
        check_state = (state == Qt.Checked)

        # Block signals on individual checkboxes during update
        for checkbox in self.mFilterCheckboxes.values():
            checkbox.blockSignals(True)
            checkbox.setChecked(check_state)
            checkbox.blockSignals(False)

        # Apply the filters once after all changes
        self.applyFilters()


    @pyqtSlot()
    def applyFilters(self):
        """Apply current filters to the displayed messages."""
        # Update the state of the 'Select All' checkbox first
        self._updateSelectAllState()
        # Save the current filter selection
        self._saveFilterPreferences()

        # Get the set of currently active filter components
        active_filters = {comp for comp, cb in self.mFilterCheckboxes.items() if cb.isChecked()}
        LaUtils.debug.log(f"Applying filters: {active_filters}", "Debug")

        # Filter messages but keep track of the original line number for each visible message
        visible_messages = []
        line_numbers = []
        line_count = 1
        
        for message in self.mMessages:
            component = self._getComponentFromMessage(message)
            if component in active_filters:
                # Only include messages that match active filters
                visible_messages.append(self._formatMessageForDisplay(message))
                line_numbers.append(line_count)
            line_count += 1

        # Update the text edit efficiently
        self.mTextEdit.setUpdatesEnabled(False)  # Disable updates for performance
        self.mTextEdit.clear()
        
        # Create a special formatted text that includes line numbers in red at the beginning of each line
        formatted_text = ""
        for i, (message, line_num) in enumerate(zip(visible_messages, line_numbers)):
            if i > 0:
                formatted_text += "\n"
            # We don't actually include the line number in the text since the line number area will handle that
            formatted_text += message
        
        self.mTextEdit.appendPlainText(formatted_text)
        
        # Store the mapping of visual lines to actual line numbers for the line number area to use
        self.mTextEdit.mLineNumberMappings = line_numbers
        self.mTextEdit.mLineNumberArea.update()  # Force the line number area to update
        
        self.mTextEdit.setUpdatesEnabled(True)  # Re-enable updates

        # Handle auto-scroll after content update
        if self.mAutoScrollCheckbox.isChecked():
            scrollbar = self.mTextEdit.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())

        LaUtils.debug.log("Filters applied with preserved line numbering.", "Debug")

    @pyqtSlot()
    def _clearLog(self):
        """Clear stored messages and the display."""
        self.mMessages.clear()
        self.mTextEdit.clear()
        LaUtils.debug.log("Log cleared.", "Debug")
        # Optionally clear LaUtils.debug history?
        # LaUtils.debug.clearHistory()


    @pyqtSlot()
    def _copyAll(self):
        """Copy the currently displayed log content to the clipboard."""
        clipboard = QApplication.clipboard()
        if clipboard:
            clipboard.setText(self.mTextEdit.toPlainText())
            LaUtils.debug.log("Displayed log copied to clipboard.", "Debug")

    def closeEvent(self, event: 'QCloseEvent'):
        """Handle closing the dialog (hides instead of deleting)."""
        # Save geometry (position and size)
        settings = QSettings()
        settings.setValue("landuse_analyst/debug_dialog_geometry", self.saveGeometry())

        # Save other preferences (already handled by toggles)
        self._saveFilterPreferences() # Ensure latest filter state is saved

        # Hide the dialog instead of accepting the close event
        self.hide()
        event.ignore() # Prevent the dialog from being destroyed
        LaUtils.debug.log("Debug dialog hidden.", "Debug")

    @pyqtSlot(bool)
    def _toggleLineNumbers(self, checked: bool):
        """Toggle line numbers visibility."""
        # Save the setting
        settings = QSettings()
        settings.setValue("landuse_analyst/debug_show_line_numbers", checked)
        # Update the text edit widget
        self.mTextEdit.toggleLineNumbers(checked)
        LaUtils.debug.log(f"Show line numbers toggled: {checked}", "Debug")

    @pyqtSlot(bool)
    def _toggleWordWrap(self, checked: bool):
        """Toggle word wrap setting."""
        # Save the setting
        settings = QSettings()
        settings.setValue("landuse_analyst/debug_word_wrap", checked)
        # Update the text edit widget's wrap mode
        wrap_mode = QPlainTextEdit.WidgetWidth if checked else QPlainTextEdit.NoWrap
        self.mTextEdit.setLineWrapMode(wrap_mode)
        # Update line number area as wrapping affects layout
        self.mTextEdit.updateLineNumberAreaWidth()
        LaUtils.debug.log(f"Word wrap toggled: {checked}", "Debug")

    # Make sure the instance is cleaned up if the application quits
    # This might require connecting to qApp.aboutToQuit() if parent is None
    # or relying on Qt's parent-child cleanup mechanism if parent is provided.
    def __del__(self):
         print(f"LaDebugDialog instance {id(self)} being deleted.")
         # Clean up singleton reference if this instance is the one registered
         if LaDebugDialog._instance is self:
             LaDebugDialog._instance = None