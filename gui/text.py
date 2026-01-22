import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QTextEdit, QMessageBox, QFileDialog , QPushButton
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("text edit")

        layout = QVBoxLayout()
        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")

        file_menu.addAction("&Open", self.open_file)
        file_menu.addAction("&Save as", self.save_file)
        file_menu.addAction("Sa&ve", self.save)
        file_menu.addSeparator()
        file_menu.addAction("E&xit", self.quit)

        self.textedit=QTextEdit()
        layout.addWidget(self.textedit)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_file(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt *.html)")
        try:
            file=open(self.filename,"r")
            self.textedit.setPlainText(file.read())
            file.close()
        except:
            print(self.filename)

    def save_file(self):
        self.filename, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt *.html)")
        try:
            file=open(self.filename,"w")
            file.write(self.textedit.toPlainText())
            file.close()
        except:
            print(self.filename)
    def save(self):
        try:
            file=open(self.filename,"w")
            file.write(self.textedit.toPlainText())
            file.close()
        except:
            print(self.filename)


    def quit(self):
        try:
            file=open(self.filename,"r")
            data=file.read()
            file.close()
        except:
            print("file not found")
            data=""
        if data!=self.textedit.toPlainText():
            dlg = QMessageBox.warning(self, "Exit?", "Are you sure you have unsaved changes", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            if dlg == QMessageBox.StandardButton.Ok:
            # qtc.QCoreApplication.quit()
                self.app.quit()
        else:
            self.app.quit()



app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()