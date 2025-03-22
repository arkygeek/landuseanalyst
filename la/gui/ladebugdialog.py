#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debug dialog for Landuse Analyst - Singleton Pattern Implementation
"""
import os
from qgis.PyQt.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QCheckBox,
    QLabel, QSplitter
)
from qgis.PyQt.QtCore import Qt, QSettings, QSize, pyqtSignal
from qgis.PyQt.QtGui import QFont, QTextCursor
from la.lib.lautils import MESSAGE_BUS

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
        # self.setAttribute(Qt.WA_DeleteOnClose)
        
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
        
        # Text area
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setLineWrapMode(QTextEdit.NoWrap)
        font = QFont("Monospace")
        font.setStyleHint(QFont.TypeWriter)
        self.text_edit.setFont(font)
        layout.addWidget(self.text_edit)
        
        # Button row
        button_layout = QHBoxLayout()
        
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_log)
        button_layout.addWidget(self.clear_button)
        
        self.auto_scroll = QCheckBox("Auto-scroll")
        self.auto_scroll.setChecked(True)
        button_layout.addWidget(self.auto_scroll)
        
        button_layout.addStretch()
        
        self.copy_button = QPushButton("Copy All")
        self.copy_button.clicked.connect(self.copy_all)
        button_layout.addWidget(self.copy_button)
        
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.hide)  # Changed from close to hide to preserve the instance
        button_layout.addWidget(self.close_button)
        
        layout.addLayout(button_layout)

    def add_debug_message(self, message: str):
        """Add message to log with auto-scroll handling"""
        if not message:
            return
  
        self.text_edit.append(message)
        if self.auto_scroll.isChecked():
            cursor = self.text_edit.textCursor()
            cursor.movePosition(QTextCursor.End)
            self.text_edit.setTextCursor(cursor)

    def add_messages_from_history(self, messages_list: list):
        """Bulk load historical messages"""
        if not messages_list:
            return
  
        self.text_edit.append("\n".join(messages_list))
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