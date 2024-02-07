# login.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QColor, QPalette, QFont
from PyQt5.QtCore import Qt, pyqtSignal

class LoginScreen(QWidget):
    login_successful = pyqtSignal()

    def __init__(self, client=None):
        super().__init__()

        self.client = client
        self.menu_screen = None

        # Set up the color palette
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(36, 41, 46))  # OneDark background color
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Button, QColor(46, 51, 56))  # OneDark button color
        palette.setColor(QPalette.ButtonText, Qt.white)
        self.setPalette(palette)

        # Set font
        font = QFont("Segoe UI", 12)
        self.setFont(font)

        # Create widgets
        login_label = QLabel('V2 Discord Bot', self)
        login_label.setAlignment(Qt.AlignCenter)
        login_label.setStyleSheet('color: white; font-size: 24px; font-weight: bold;')

        username_input = QLineEdit(self)
        username_input.setPlaceholderText('Username')
        username_input.setStyleSheet('background-color: #282c34; color: white; font-size: 14px; border: 1px solid #2c313a; border-radius: 5px;')

        password_input = QLineEdit(self)
        password_input.setPlaceholderText('Password')
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setStyleSheet('background-color: #282c34; color: white; font-size: 14px; border: 1px solid #2c313a; border-radius: 5px;')

        login_button = QPushButton('Login', self)
        login_button.setStyleSheet('background-color: #61afef; color: white; font-size: 14px; border: 1px solid #61afef; border-radius: 5px;')

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(login_label)
        layout.addWidget(username_input)
        layout.addWidget(password_input)
        layout.addWidget(login_button)

        self.setLayout(layout)

        # Connect button signals to functions
        login_button.clicked.connect(self.login)

        # Set up the window
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Login')

    def login(self):
        username = self.findChild(QLineEdit, 'Username').text()
        password = self.findChild(QLineEdit, 'Password').text()

        if username == 'Diego' and password == '42069':
            print('Login successful')
            self.login_successful.emit()
        else:
            print('Login failed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec_())
