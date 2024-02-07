# main.py
import sys
from PyQt5.QtWidgets import QApplication
from menu import MenuScreen

class MainApplication(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.menu_screen = MenuScreen()

    def show_menu(self):
        self.menu_screen.show()

if __name__ == '__main__':
    app = MainApplication(sys.argv)
    app.show_menu()
    sys.exit(app.exec_())
