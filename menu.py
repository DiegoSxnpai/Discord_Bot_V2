# menu.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtGui import QColor, QPalette, QPixmap
from PyQt5.QtCore import Qt
from colorama import Fore, Style

class MenuScreen(QWidget):
    def __init__(self, client=None):
        super().__init__()

        self.client = client

        # Set up the color palette
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(54, 57, 63))  # Discord-like background color
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Button, QColor(79, 84, 92))  # Discord-like button color
        palette.setColor(QPalette.ButtonText, Qt.white)
        self.setPalette(palette)

        # Set up the layout
        main_layout = QHBoxLayout()

        # Left side - Server list and user info
        server_info_layout = QVBoxLayout()

        # Placeholder for server list
        server_list_label = QLabel('Server List:')
        server_list_label.setStyleSheet('color: white; font-size: 14px;')
        server_info_layout.addWidget(server_list_label)

        # Placeholder for the list of servers
        server_list_widget = QListWidget(self)
        servers = ['Bot Server', 'Server 1', 'Server 2']  # Replace with the actual server list
        for server in servers:
            item = QListWidgetItem(server)
            server_list_widget.addItem(item)
        server_info_layout.addWidget(server_list_widget)

        # Placeholder for user info
        user_info_label = QLabel('Bot Information:')
        user_info_label.setStyleSheet('color: white; font-size: 14px;')
        server_info_layout.addWidget(user_info_label)

        # Placeholder for bot information
        bot_info_text = QLabel('Bot Name: V2-Beta\nBot ID: 1200837473350205510\nOwner: DiegoSxnpai')  # Replace with actual bot information
        bot_info_text.setStyleSheet('color: white; font-size: 14px;')
        server_info_layout.addWidget(bot_info_text)

        main_layout.addLayout(server_info_layout)

        # Right side - Buttons
        button_layout = QVBoxLayout()

        send_message_button = QPushButton('Send Message to All Users', self)
        send_message_button.setStyleSheet('background-color: #7289da; color: white; font-size: 14px; border: 1px solid #7289da; border-radius: 5px;')

        user_info_button = QPushButton('Information about Users', self)
        user_info_button.setStyleSheet('background-color: #7289da; color: white; font-size: 14px; border: 1px solid #7289da; border-radius: 5px;')

        server_info_button = QPushButton('Information about Server', self)
        server_info_button.setStyleSheet('background-color: #7289da; color: white; font-size: 14px; border: 1px solid #7289da; border-radius: 5px;')

        exit_button = QPushButton('Exit', self)
        exit_button.setStyleSheet('background-color: #e06c75; color: white; font-size: 14px; border: 1px solid #e06c75; border-radius: 5px;')

        button_layout.addWidget(send_message_button)
        button_layout.addWidget(user_info_button)
        button_layout.addWidget(server_info_button)
        button_layout.addWidget(exit_button)

        main_layout.addLayout(button_layout)

        # Set up the window
        self.setLayout(main_layout)
        self.setGeometry(300, 300, 800, 600)  # Set a larger size
        self.setWindowTitle('Discord-like Menu')

        # Load Discord logo as a placeholder
        discord_logo_label = QLabel(self)
        pixmap = QPixmap('discord_logo.png')  # Replace 'discord_logo.png' with the path to your logo
        discord_logo_label.setPixmap(pixmap)
        discord_logo_label.setGeometry(20, 20, 200, 60)  # Adjust the position and size of the logo

    def send_message_to_all_users(self):
        print("Sending message to all users")

    def show_user_info(self):
        print("Displaying information about users")

    def show_server_info(self):
        print("Displaying information about server")
