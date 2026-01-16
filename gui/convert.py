import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
# import PyQt6.QtCore as qtc
# import PyQt6.QtGui as qtg


# Subclass QMainWindow to customise your application's main window
class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        layout = qtw.QGridLayout()

        self.setWindowTitle("metres to feet")

        widget = qtw.QWidget()

        widget.setLayout(layout)

        self.textbox=qtw.QLineEdit()

        self.value=("?")

        self.gobut=qtw.QPushButton("go")
        self.gobut.clicked.connect(self.go_click)

        self.setCentralWidget(widget)
        self.label = qtw.QLabel()
        layout.addWidget(self.label, 0, 0, 1, 3)
        layout.addWidget(self.textbox, 1, 0)
        layout.addWidget(self.gobut, 2, 0)

    def go_click(self):
        convert=self.textbox.text()
        try:
            self.value="feet  "+str(int(convert)*3.28)
        except:
            self.value="feet  ?"
        self.label.setText(self.value)
        
app = qtw.QApplication([])
window = MainWindow()
window.show()
app.exec()