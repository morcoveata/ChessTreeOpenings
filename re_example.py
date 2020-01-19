import re
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


def main():

	app = QtGui.QApplication(sys.argv)

	w = QtGui.QWidget()
	w.resize(250, 150)
	w.move(300, 300)
	w.setWindowTitle('Simple')

	#exemplu = QtCore.QString('mama are mere (cu niste bestele)')
	exemplu = "                            mama are mere [cu niste bestele]"

	inputPng = QtGui.QPlainTextEdit()
	text = open('text.pgn').read()
	inputPng.setPlainText(text)

	# re.sub(r'\[.*\]', '', exemplu)
	print re.sub(r'\[[^()]*\]', '', exemplu)

	print exemplu.replace("  ", "")
	


	

	w.show()

	sys.exit(app.exec_())



if __name__ == '__main__':
	main()

