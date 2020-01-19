#! /usr/bin/env python3
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In this prototype/example a QTreeView is created. Then it's populated with
# three containers and all containers are populated with three rows, each 
# containing three columns.
# Then the last container is expanded and the last row is selected.
# The container items are spanned through the all columns.
# Note: this requires > python-3.2
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sys, os, pprint, time
from PyQt4 import QtGui
from PyQt4 import QtCore


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app = QtGui.QApplication(sys.argv)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# init widgets
view = QtGui.QTreeView()
view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
model = QtGui.QStandardItemModel()
model.setHorizontalHeaderLabels(['col1', 'col2', 'col3'])
view.setModel(model)
view.setUniformRowHeights(True)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# populate data

parent1 = QtGui.QStandardItem("caca maca")
child1 = QtGui.QStandardItem("mama1")
child2 = QtGui.QStandardItem("mama2")
child3 = QtGui.QStandardItem("mama31")
parent1.appendColumn([child1, child2, child3])
model.appendRow(parent1)

# for i in range(3):
#     parent1 = QtGui.QStandardItem('Family {}. Some long status text for sp'.format(i))
#     for j in range(3):
#         child1 = QtGui.QStandardItem('Child {}'.format(i*3+j))
#         child2 = QtGui.QStandardItem('row: {}, col: {}'.format(i, j+1))
#         child3 = QtGui.QStandardItem('row: {}, col: {}'.format(i, j+2))
#         parent1.appendRow([child1, child2, child3])
#     model.appendRow(parent1)
#     # span container columns
#     view.setFirstColumnSpanned(i, view.rootIndex(), True)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# expand third container
index = model.indexFromItem(parent1)
view.expand(index)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# select last row
selmod = view.selectionModel()
index2 = model.indexFromItem(child3)
selmod.select(index2, QtGui.QItemSelectionModel.Select|QtGui.QItemSelectionModel.Rows)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
view.show()
sys.exit(app.exec_())
# ~~~~~~~~~~~~~~~~~~~~

# verific checkout