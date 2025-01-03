import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from skyldocsup import Ui_MainWindow

class MainWindowController(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.is_maximized = False
        self.menu_visible = True
        self.username = None

        # Set up UI connections
        self.setup_connections()

    def setup_connections(self):
        """Connect UI buttons to their respective methods."""
        self.ui.to_signupbtn.clicked.connect(self.show_signup_page)
        self.ui.to_loginbtn.clicked.connect(self.show_login_page)
        self.ui.signup_btn.clicked.connect(self.handle_signup)
        self.ui.signin_btn.clicked.connect(self.handle_login)
        self.ui.getStartedbtn.clicked.connect(self.show_main_page)
        self.ui.menubtn.clicked.connect(self.toggle_menu)
        self.ui.homebtn.clicked.connect(self.show_home_page)
        self.ui.createbtn.clicked.connect(self.show_add_supplier_page)
        self.ui.addsupplierbtn.clicked.connect(self.show_add_supplier_page)
        self.ui.additembtn.clicked.connect(self.show_add_item_page)
        self.ui.additembtn_2.clicked.connect(self.show_add_item_page)
        self.ui.archivebtn.clicked.connect(self.show_archive_page)
        self.ui.profilebtn.clicked.connect(self.show_profile_page)
        self.ui.editprofilebtn.clicked.connect(self.show_editprofile_page)
        self.ui.saveprofilebtn.clicked.connect(self.show_profile)
        self.setup_window_controls()

    def setup_window_controls(self):
        """Set up controls for minimizing, maximizing, and closing the window."""
        for btn in [self.ui.closeButton, self.ui.closeButton_3]:
            btn.clicked.connect(self.close_program)
        for btn in [self.ui.minimize, self.ui.minimize_3]:
            btn.clicked.connect(self.minimize_program)
        for btn in [self.ui.restoreDown, self.ui.restoreDown_3]:
            btn.clicked.connect(self.toggle_maximize_restore)

    # User action handlers
    def handle_signup(self):
        """Handle the signup process."""
        username = self.ui.signup_username.text()
        email = self.ui.email.text()
        password = self.ui.signup_pass.text()
        confirm_password = self.ui.confirmpass.text()

        if not username or not email or not password or not confirm_password:
            self.show_error_message("All fields are required!")
            return

        if password != confirm_password:
            self.show_error_message("Passwords do not match!")
            return

        self.show_welcome_page()

    def handle_login(self):
        """Handle the login process."""
        username = self.ui.signin_username.text()
        password = self.ui.signin_pass.text()

        if not username or not password:
            self.show_error_message("Both fields are required!")
            return

        self.show_welcome_page()

    def show_error_message(self, message):
        """Display an error message to the user."""
        QtWidgets.QMessageBox.warning(self, "Error", message)

    # Page navigation methods
    def show_signup_page(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.signup_pg)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.welcome_signin)

    def show_login_page(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.login_pg)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.welcome_login)

    def show_welcome_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.welcome)
        
    def show_main_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)

    def show_home_page(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.homepg)

    def show_add_supplier_page(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.addsupplierpg)

    def show_add_item_page(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.additempg)
        
    def show_archive_page(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.archivepg)
        
    def show_profile_page(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.profilepg)
        
    def show_editprofile_page(self):
        self.ui.stackedWidget_6.setCurrentWidget(self.ui.editprofilepg)
        
    def show_profile(self):
        self.ui.stackedWidget_6.setCurrentWidget(self.ui.profile)
        
    def toggle_menu(self):
        self.ui.menupg.setVisible(not self.menu_visible)
        self.menu_visible = not self.menu_visible
        
    # Window control methods
    def close_program(self):
        """Prompt user for confirmation before closing the application."""
        reply = QMessageBox.question(
            self, 
            "Confirm Exit", 
            "Are you sure you want to exit?", 
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.close()

    def minimize_program(self):
        self.showMinimized()

    def toggle_maximize_restore(self):
        if self.is_maximized:
            self.showNormal()
        else:
            self.showMaximized()
        self.is_maximized = not self.is_maximized

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindowController()
    main_window.show()
    sys.exit(app.exec_())
