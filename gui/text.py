import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, \
    QPushButton, QVBoxLayout, QTextEdit, QColorDialog, QMessageBox, QFileDialog,QHBoxLayout
import PyQt6.QtCore as qtc 

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("text edit")

        layout = QVBoxLayout()
        buttons=QHBoxLayout()

        self.textedit=QTextEdit()
        layout.addWidget(self.textedit)
        # Create another button
        quit_btn = QPushButton("Quit")
        quit_btn.clicked.connect(self.quit)
        buttons.addWidget(quit_btn)

        # Create another button
        open_btn = QPushButton("Open")
        open_btn.clicked.connect(self.open_btn_click)
        buttons.addWidget(open_btn)

        # Create another button
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_btn_click)
        buttons.addWidget(save_btn)
        layout.addLayout(buttons)
        # Create the windows central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_btn_click(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt *.html)")
        file=open(filename,"r")
        self.textedit.setPlainText(file.read())
        file.close()

        print(filename)

    def save_btn_click(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt *.html)")
        file=open(filename,"w")
        file.write(self.textedit.toPlainText())
        file.close()

        print(filename)


    def quit(self):
        dlg = QMessageBox.warning(self, "Quit?", "Are you sure", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        print(dlg)
        if dlg == QMessageBox.StandardButton.Ok:
            # qtc.QCoreApplication.quit()
            self.app.quit()



app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()