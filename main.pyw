from PySide import QtCore, QtGui
import subprocess
import sys
import re
from design import Ui_Dialog
from math import sqrt


class Main:

	"""Responsible for rendering and application logic"""

	def __init__(self):

		"""Create application, form and init UI"""

		self.app = QtGui.QApplication(sys.argv)


		self.Dialog = QtGui.QDialog()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self.Dialog)
		self.Dialog.show()

		self.Dialog.setFixedSize(356, 484)
		self.ui.textEdit.setDisabled(True)
		self.ui.textEdit.setFontPointSize(14)
		self.ui.textEdit.setTextColor("black")

		# Custom expression
		self.value = []
		self.result = 0
		self.find_sqrt = 0

		self.ui.textEdit.setText(str(self.result))


	@staticmethod
	def pyside_install():
		subprocess.call([sys.executable, "-m", "pip", "install", "pyside"])


	def button_pressed(self, char):

		"""Add character to custom expression"""

		self.value.append(char)
		self.ui.textEdit.setText("".join(self.value))


	def cancel(self):

		"""Clear custom expression"""

		self.value.clear()
		self.ui.textEdit.setText("".join(self.value))


	def undo(self):

		"""Undo last user input"""

		del self.value[-1]
		self.ui.textEdit.setText("".join(self.value))


	def show_result(self):

		"""Converts a custom expression to an interpreter-friendly view
		And show result of eval"""

		for n, i in enumerate(self.value):
			if i == "√":
				self.value[n] = "sqrt("
				self.find_sqrt += 1
				continue
			if (re.match(r"[^\.√0-9]", i)) and (self.find_sqrt > 0):
				self.value[n-1] += ")" * self.find_sqrt
				self.find_sqrt = 0
			if i == "^":
				self.value[n] = "**"

		if self.find_sqrt > 0:
			self.value.append(")" * self.find_sqrt)
			self.find_sqrt = 0

		self.result = str(eval("".join(self.value)))
		self.ui.textEdit.setText(self.result)
		self.value.clear()
		self.value.append(self.result)

	def hook_logic(self):

		"""Control user input"""

		self.ui.pushButton.clicked.connect(lambda: self.button_pressed("8"))
		self.ui.pushButton_2.clicked.connect(lambda: self.cancel())
		self.ui.pushButton_3.clicked.connect(lambda: self.button_pressed("."))
		self.ui.pushButton_4.clicked.connect(lambda: self.button_pressed("4"))
		self.ui.pushButton_5.clicked.connect(lambda: self.button_pressed("1"))
		self.ui.pushButton_6.clicked.connect(lambda: self.button_pressed("5"))
		self.ui.pushButton_7.clicked.connect(lambda: self.button_pressed("2"))
		self.ui.pushButton_8.clicked.connect(lambda: self.button_pressed("0"))
		self.ui.pushButton_9.clicked.connect(lambda: self.button_pressed("√"))
		self.ui.pushButton_10.clicked.connect(lambda: self.button_pressed("6"))
		self.ui.pushButton_11.clicked.connect(lambda: self.button_pressed("3"))
		self.ui.pushButton_12.clicked.connect(lambda: self.undo())
		self.ui.pushButton_13.clicked.connect(lambda: self.button_pressed("^"))
		self.ui.pushButton_14.clicked.connect(lambda: self.button_pressed("7"))
		self.ui.pushButton_15.clicked.connect(lambda: self.button_pressed("9"))
		self.ui.pushButton_16.clicked.connect(lambda: self.button_pressed("/"))
		self.ui.pushButton_17.clicked.connect(lambda: self.button_pressed("*"))
		self.ui.pushButton_18.clicked.connect(lambda: self.button_pressed("-"))
		self.ui.pushButton_19.clicked.connect(lambda: self.button_pressed("+"))
		self.ui.pushButton_20.clicked.connect(lambda: self.show_result())

		# Run main loop
		sys.exit(self.app.exec_())


if __name__ == "__main__":
	main = Main()
	main.pyside_install()
	main.hook_logic()