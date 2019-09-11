import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Window(QtGui.QMainWindow):
	"""docstring for window(QMainWindow)"""
	def __init__(self):
		super(Window, self).__init__()



		widget = QtGui.QWidget(self)
		self.setCentralWidget(widget)

		
		self.textEdit = QtGui.QTextEdit()
		self.treeWiew = QtGui.QTreeView()

		layout = QtGui.QGridLayout()
		layout.addWidget(self.textEdit, 0, 0)
		layout.addWidget(self.treeWiew, 1, 0)


		widget.setLayout(layout)

		model = QtGui.QStandardItemModel()
		model.setHorizontalHeaderLabels(['col1', 'col2', 'col3'])
		self.treeWiew.setModel(model)
		self.treeWiew.setUniformRowHeights(True)
		parent1 = QtGui.QStandardItem('mama')

		child1 = QtGui.QStandardItem('Child1')
		child2 = QtGui.QStandardItem('Child2')
		child3 = QtGui.QStandardItem('Child3')
		parent1.appendRow([child1, child2, child3])

		model.appendRow(parent1)






		# https://programtalk.com/python-examples/PyQt4.QtGui.QDesktopWidget.screenGeometry/
		rect = QtGui.QDesktopWidget().screenGeometry()
		width = rect.width()
		height = rect.height()
		self.setGeometry(40, 40, width*2/3, height*2/3)








if __name__ == '__main__':
	app = QtGui.QApplication([])
	gui = Window()
	gui.show()
	app.exec_()
		
