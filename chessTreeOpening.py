import re
import sys
import collections
import operator
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

		print type (final_string)
		print "final_string"
		print final_string.strip()
		print '\n'
		# final_string.strip()

		# def a1(test_str):
		# 	ret = ''
		# 	skip2c = 0
		# 	index = 0
		# 	ind_list = []
		# 	for i in test_str:
		# 		index += 1
		# 		if i == '(':
		# 			skip2c += 1
		# 		elif i == ')' and skip2c > 0:
		# 			skip2c -= 1
		# 		elif skip2c == 1:
		# 			ret += i
		# 			ind_list.append(index)
		# 	return ret, ind_list


		def a1(test_str):
			ret = ''
			skip2c = 0
			index = 0
			ind_list = []
			for i in test_str:
				index += 1
				if i == '(':
					skip2c += 1
				elif i == ')' and skip2c > 0:
					skip2c -= 1
				elif skip2c == 1:
					ret += i
					ind_list.append(index)
			return ret, ind_list

		########################
		#print a (final_string)
		#print extract(final_string)

		#print final_string
		# print a1(final_string)[0]
		# print a1(final_string)[1]

		# https://stackoverflow.com/questions/53045597/assigning-keys-to-a-dictionary-from-a-string
		def make_dict(test_str):
			dict_moves = {}
			list_char = []
			list_index = []
			count = 0
			for i in test_str:
				count += 1
				list_char.append(i)
				list_index.append(count)
			dict_moves = dict(zip(list_index, list_char))
			return dict_moves

		# print make_dict(final_string)

		# https://stackoverflow.com/questions/41970992/appending-values-to-dictionary-in-for-loop
		def get_brackets (get_dict):
			temp_dict = {}
			for key, value in get_dict.items():
				if value == '(' or value == ')':
					if key not in temp_dict:
						temp_dict[key] = []
					temp_dict[key].append(value)
			return temp_dict

		dict_1 = make_dict(final_string)
		print type (dict_1)
		print "dict_1"
		print dict_1
		print '\n'

		# https: // stackoverflow.com / questions / 613183 / how - do - i - sort - a - dictionary - by - value
		dict_2 = get_brackets(dict_1)
		dict_2 = sorted(dict_2.items(), key=operator.itemgetter(0))
		dict_2 = collections.OrderedDict(dict_2)
		print "dict_2"
		print dict_2
		print '\n'

		def get_variation(ex_dict):
			start = 0
			fin = 0
			for key, value in ex_dict.items():
				aiurea = int(key)
				if value == ['(']:
					start = aiurea
				elif value == [')']:
					fin = aiurea
					return start, fin
					return
		

		dict_3 = get_variation(dict_2)
		print "dict_3"
		print type (dict_3)
		print dict_3
		print '\n'

		# newstr = final_string[3:9]
		position_first_bracket = dict_3[0]
		position_last_bracket = dict_3[1]
		print final_string
		final_string = final_string[0: position_first_bracket-1:] + final_string[position_last_bracket::]
		# final_string = final_string [0: 46:] + final_string [85: :]
		print final_string

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
