import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QLabel, QLineEdit, QGridLayout

from PySide6.QtGui import QIcon, QFont

from PySide6.QtCore import Qt

app = QApplication(sys.argv)

class StartWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()
        
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(screen_geometry)

        centerX = screen_geometry.width() / 2

        layout = QVBoxLayout()

        #label1: FinancEasy
        self.label1 = QLabel()
        self.label1.setWordWrap(True)
        self.label1.setText("FinancEasy\n Make finance easy.")

        font = QFont()
        font.setPointSize(30)
        self.label1.setFont(font)
        self.label1.setAlignment(Qt.AlignCenter)

        #button1: create your own cryptocurrency
        self.button1 = QPushButton()
        self.button1.setText("Create your own cryptocurrency!")
        self.button1.clicked.connect(self.button_clicked)

        #button2: or, track my daily spending
        self.button2 = QPushButton()
        self.button2.setText("or, track my daily spending")
        self.button2.clicked.connect(self.button_clicked)

        #setting the layout
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.label1)
        button_layout.addSpacing(100)
        button_layout.addWidget(self.button1)
        button_layout.addSpacing(10)
        button_layout.addWidget(self.button2)
        button_layout.setAlignment(Qt.AlignCenter)
        layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def button_clicked(self):
        self.hide()
        new_page = CreatePage(self)
        new_page.show()

class CreatePage(QMainWindow):
    def __init__(self, parent=None):
        
        super().__init__(parent)
        self.setWindowTitle("Set Up Page")

        screen_geometry = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(screen_geometry)

        layout = QVBoxLayout()

        #label2 : create your own cryptocurrency
        self.label2 = QLabel()
        self.label2.setText("Create your own cryptocurrency")

        font = QFont()
        font.setPointSize(30)
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignCenter)

        #label3 : currency name
        self.label3 = QLabel()
        self.label3.setText("Currency name")

        font2 = QFont()
        font2.setPointSize(10)
        self.label3.setFont(font2)

        #typing box : currency name
        self.typing_curr_name = QLineEdit()
        self.typing_curr_name.setPlaceholderText("Eg. bitcoin")
        self.typing_curr_name.returnPressed.connect(self.on_curr_entered)

        #label4 : symbol
        self.label4 = QLabel()
        self.label4.setText("Symbol")

        font2 = QFont()
        font2.setPointSize(10)
        self.label4.setFont(font2)

        #typing box : symbol
        self.typing_symbol = QLineEdit()
        self.typing_symbol.setPlaceholderText("Eg. $")
        self.typing_symbol.returnPressed.connect(self.on_symbol_entered)

        #button3 : submit 
        self.button3 = QPushButton()
        self.button3.setText("SUBMIT")
        self.button3.clicked.connect(self.to_home)

        #button4 : back to main window
        self.button4 = QPushButton()
        self.button4.setText("back")
        self.button4.clicked.connect(self.return_to_startWindow)
        
        #create input layout
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.label2)
        input_layout.addSpacing(50)
        input_layout.addWidget(self.label3)
        input_layout.addWidget(self.typing_curr_name)
        input_layout.addSpacing(20)
        input_layout.addWidget(self.label4)
        input_layout.addWidget(self.typing_symbol)
        input_layout.addSpacing(20)
        input_layout.addWidget(self.button3)
        input_layout.addSpacing(20)
        input_layout.addWidget(self.button4)
        input_layout.setAlignment(Qt.AlignCenter)
        layout.addLayout(input_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_curr_entered(self):
        text = self.typing_curr_name.text()
    
    def on_symbol_entered(self):
        symbol = self.typing_symbol.text()

    def to_home(self):
        self.hide()
        home_page = CreateHomePage(self)
        home_page.show()

    def return_to_startWindow(self):
        self.close()
        parent_window = self.parent()
        parent_window.show()


class CreateHomePage(QMainWindow):
    def __init__(self, parent=None):
        
        super().__init__(parent)
        self.setWindowTitle("Home Page")

        screen_geometry = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(screen_geometry)

        layout = QVBoxLayout()

        #button5 : exit
        self.button5 = QPushButton()
        self.button5.setText("EXIT")
        self.button5.clicked.connect(self.quit)

        #setting the layout
        home_layout = QVBoxLayout()
        home_layout.addWidget(self.button5)
        home_layout.setAlignment(Qt.AlignCenter)
        layout.addLayout(home_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def quit(self):
        QApplication.quit()

window = StartWindow()
window.setWindowTitle("FinancEasy")
window.show()
app.exec()
