import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtWebKit

VERSION = "0.1"

class Escribano(QtGui.QWidget):
	def __init__(self):
		super(Escribano, self).__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(0, 0, 800, 600)
		self.setWindowTitle("Escribano %s" % VERSION)
		self.setWindowIcon(QtGui.QIcon('escribano.png'))

		self.textEdit = QtGui.QTextEdit(self)
		QtCore.QObject.connect(self.textEdit,
			QtCore.SIGNAL('textChanged()'), self.onTextChanged)

		self.webView = QtWebKit.QWebView(self)
		self.webView.load(QtCore.QUrl("http://www.google.com"))

		self.split = QtGui.QSplitter(QtCore.Qt.Horizontal, self)
		self.split.addWidget(self.textEdit)
		self.split.addWidget(self.webView)

		self.hbox = QtGui.QHBoxLayout(self)
		self.hbox.addWidget(self.split)

		fg = self.frameGeometry()
		fg.moveCenter(QtGui.QDesktopWidget().availableGeometry().center())
		self.move(fg.topLeft())

		self.show()

	def onTextChanged(self):
		print(self.textEdit.toPlainText())


def main():
	app = QtGui.QApplication(sys.argv)
	ex = Escribano()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
