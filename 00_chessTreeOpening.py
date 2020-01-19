import re
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Window(QtGui.QMainWindow):
	"""docstring for window(QMainWindow)"""
	def __init__(self):
		super(Window, self).__init__()

		# get the file to work with
		input_png = open('e:\\programare\\pyqt\\chessTreeOpening\\text.pgn').read()

		# remove head of pgn with rectangle brackets
		final_string = re.sub(r'\[.*?\]', '', input_png)

		# print final_string

		#################################
		#################################
		# prelucrare text din fisier pgn		
		
		# transform paragraph sign to space sign
		final_string = final_string.replace("\n", "")

		# remove space sign
		final_string = final_string.replace("  ", "")

		print final_string.strip()
		# final_string.strip()

		# check if exist round brackets in text
		def verify_for_round_brackets(text):
			exist_brackets = 0
			for sign in text:
				if sign == '(':
					exist_brackets = +1
			return exist_brackets
		print verify_for_round_brackets(final_string)



#####################

		def a(test_str):
			ret = ''
			skip2c = 0
			nr_par = 0
			for i in test_str:
				if i == '(':
					skip2c += 1
					nr_par += 1
				elif i == ')' and skip2c > 0:
					skip2c -= 1
				elif skip2c == 1 and nr_par == 1:
					ret += i
				print nr_par
			return ret
#####################

		print '/n'
		print a (final_string)


		# draw GUI
		widget = QtGui.QWidget(self)
		self.setCentralWidget(widget)

		
		self.textEdit = QtGui.QTextEdit()
		self.treeWiew = QtGui.QTreeView()


		layout = QtGui.QGridLayout()
		layout.addWidget(self.textEdit, 0, 0)
		layout.addWidget(self.treeWiew, 1, 0)


		widget.setLayout(layout)


		#set dinamicaly geometry
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
