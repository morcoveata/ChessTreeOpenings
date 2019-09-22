import re
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Window(QtGui.QMainWindow):
	"""docstring for window(QMainWindow)"""
	def __init__(self):
		super(Window, self).__init__()


##############################################
		# manipulate a png string
		# https://stackoverflow.com/questions/14596884/remove-text-between-and-in-python

		# def a(test_str):
		# 	ret = ''
		# 	skip1c = 0
		# 	skip2c = 0
		# 	for i in test_str:
		# 		if i == '[':
		# 			skip1c += 1
		# 		elif i == '(':
		# 			skip2c += 1
		# 		elif i == ']' and skip1c > 0:
		# 			skip1c -= 1
		# 		elif i == ')'and skip2c > 0:
		# 			skip2c -= 1
		# 		elif skip1c == 0 and skip2c == 0:
		# 			ret += i
		# 	return ret


	
		###############################

	# function for get main variation

		def a(test_str):
			ret = ''
			skip2c = 0
			for i in test_str:
				if i == '(':
					skip2c += 1
				elif i == ')'and skip2c > 0:
					skip2c -= 1
				elif skip2c == 0:
					ret += i
			return ret


					###############################

	# function for get first variation 
	# primeste textul din prima paranteza sau a doua sau a treia incastrate una in alta

		def a1(test_str):
			ret = ''
			skip2c = 0
			for i in test_str:
				if i == '(':
					skip2c += 1
				elif i == ')'and skip2c > 0:
					skip2c -= 1
				elif skip2c == 1:
					ret += i
			return ret



	
		inputPng = open('text.pgn').read()

		 

		# remove head of pgn with rectangel brackets
		finalString = re.sub(r'\[.*?\]', '', inputPng)


		
		# print finalString

		#################################
		#################################
		# prelucrare text din fisier pgn		
		
		#transform pargraph sign to space sign
		finalString = finalString.replace("\n", "")
		# remove space sign
		finalString = finalString.replace("  ", "")

		# print finalString.strip()
		finalString.strip()



		variantaPrincipala = a(finalString)
		variantaSecundara = a1(finalString)




		# finalString = a1(finalString)
		# #transform pargraph sign to space sign
		# finalString = finalString.replace("\n", "")
		# # remove space sign
		# finalString = finalString.replace("  ", "")

		# print finalString.strip()
		



		# with open("guru99.pgn", "a") as myfile:
		# 	myfile.write("First Line\n")
		#     myfile.close()

		###################################
		# write header for pgn
		with open("guru99.pgn", 'r+') as file:
			originalContent = file.read()
			file.seek(0, 0)              # Move the cursor to top line
			file.write('[Event "?"]\n')
			file.write('[Site "?"]\n')
			file.write('[Date "????.??.??"]\n')
			file.write('[Round "?"]\n')
			file.write('[White "?"]\n')
			file.write('[Black "?"]\n')
			file.write('[Result "*"]\n')
			file.write('[ECO "C65"]\n')
			file.write('[Annotator "LucaCiubota_Gamer"]\n')
			file.write('[PlyCount "31"]\n')
			file.write('[SourceDate "2019.05.25"]\n')
			file.write(originalContent)
				


		# test new pgn
		# f= open("guru99.pgn","w+")
		# f.write(finalString)
		# f.close()



		##################
		# draw GUI
		widget = QtGui.QWidget(self)
		self.setCentralWidget(widget)

		
		self.textEdit = QtGui.QTextEdit()
		self.treeWiew = QtGui.QTreeView()

		layout = QtGui.QGridLayout()
		layout.addWidget(self.textEdit, 0, 0)
		layout.addWidget(self.treeWiew, 1, 0)


		widget.setLayout(layout)

	##############
	# work on tree view

		model = QtGui.QStandardItemModel()
		model.setHorizontalHeaderLabels(['var 1', 'var 2', 'var 3', 'var 4', 'var 5', 'var 6'])
		self.treeWiew.setModel(model)
		self.treeWiew.setUniformRowHeights(True)

		parent1 = QtGui.QStandardItem(variantaPrincipala)
		child1 = QtGui.QStandardItem(variantaSecundara)
		child2 = QtGui.QStandardItem("varianta 2")
		child3 = QtGui.QStandardItem("varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 ")
		child4 = QtGui.QStandardItem("varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 ")
		child5 = QtGui.QStandardItem("varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 ")
		child6 = QtGui.QStandardItem("varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 varianta 3 ")
		
		model.setItem(0,0, parent1)
		parent1.setRowCount(0)
		parent1.setColumnCount(0);
		parent1.setChild(0, 0, child1);
		parent1.setChild(1, 1, child2);
		parent1.setChild(2, 2, child3);	
		parent1.setChild(3, 3, child4);	
		parent1.setChild(4, 4, child5);	
		parent1.setChild(5, 5, child6);	

		# parent1.appendColumn([child1, child2, child3])

		# model.appendRow(parent1)


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

