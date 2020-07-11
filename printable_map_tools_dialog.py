# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PrintableMapToolsDialog
                                 A QGIS plugin
 "Pintable Map Tools" is a plugin under development for QGIS. The goal is to create modules and enhancements for printable maps, including label placement.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-07-11
        git sha              : $Format:%H$
        copyright            : (C) 2020 by STADTKREATION
        email                : qgis@stadtkreation.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'printable_map_tools_dialog_base.ui'))


class PrintableMapToolsDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(PrintableMapToolsDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
