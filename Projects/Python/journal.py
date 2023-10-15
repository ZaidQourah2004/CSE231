import sys
import json
import bcrypt
from base64 import b64encode, b64decode
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMenuBar, QMenu, QAction, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, QInputDialog
from PyQt5.QtCore import Qt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QActionGroup, QLabel, QLineEdit, QListWidget, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMenuBar, QMenu, QAction, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, QInputDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class PasswordDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Enter Password")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.unlock_button = QPushButton("Unlock")
        self.unlock_button.clicked.connect(self.unlock)
        layout.addWidget(self.unlock_button)

        self.setLayout(layout)

    def unlock(self):
        self.password = self.password_input.text().encode('utf-8')

        if not self.password:
            QMessageBox.warning(self, "Error", "Please enter a password.")
            return

        with open("password.json", "r") as file:
            stored_password = json.load(file)

        hashed_password = stored_password["password"].encode('utf-8')
        if bcrypt.checkpw(self.password, hashed_password):
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Incorrect password.")


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Password Authentication")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Unlock")
        self.login_button.clicked.connect(self.unlock)
        layout.addWidget(self.login_button)

        self.set_password_button = QPushButton("Set Password")
        self.set_password_button.clicked.connect(self.set_password)
        layout.addWidget(self.set_password_button)

        self.change_password_button = QPushButton("Change Password")
        self.change_password_button.clicked.connect(self.change_password)
        layout.addWidget(self.change_password_button)

        self.settings_button = QPushButton("Settings")
        self.settings_button.clicked.connect(self.open_settings)
        layout.addWidget(self.settings_button)

        self.setLayout(layout)

    def open_settings(self):
        if self.password_exists():
            password_dialog = PasswordDialog(self)
            if password_dialog.exec_() == QDialog.Accepted:
                # Password was entered correctly, open the settings
                QMessageBox.information(self, "Settings", "Settings button clicked!")
        else:
            QMessageBox.warning(self, "Error", "Please set a password to login.")

    def validate_normal_password(self, password):
            if len(password) < 6:
                return False

            has_upper = any(c.isupper() for c in password)
            has_lower = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)

            return has_upper and has_lower and has_digit

    def password_exists(self):
        try:
            with open("password.json", "r") as file:
                json.load(file)
                return True
        except FileNotFoundError:
            return False

    def unlock(self):
        self.password = self.password_input.text().encode('utf-8')

        if not self.password:
            QMessageBox.warning(self, "Error", "Please enter a password.")
            return

        if not self.password_exists():
            QMessageBox.warning(self, "Error", "Please set a password to login.")
            return

        with open("password.json", "r") as file:
            stored_password = json.load(file)

        hashed_password = stored_password["password"].encode('utf-8')
        if bcrypt.checkpw(self.password, hashed_password):
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Incorrect password.")

    def set_new_password(self, password_type):
        def get_confirm_password(prompt):
            confirm_password, ok = QInputDialog.getText(self, "Confirm Password", prompt, QLineEdit.Password)
            return confirm_password if ok else None

        if password_type == 'Normal':
            new_password, ok = QInputDialog.getText(self, "Set Password", "Enter your new password (at least 6 characters, one uppercase, one lowercase, and one number):", QLineEdit.Password)
            if ok and self.validate_normal_password(new_password):
                confirm_password = get_confirm_password("Re-enter your new password:")
                return new_password if new_password == confirm_password else None
            else:
                QMessageBox.warning(self, "Error", "Password does not meet the criteria.")
                return None
        elif password_type == '4-digit':
            new_password, ok = QInputDialog.getInt(self, "Set Password", "Enter your new 4-digit password:", min=1000, max=9999)
            if ok:
                confirm_password = get_confirm_password("Re-enter your new 4-digit password:")
                return str(new_password) if str(new_password) == confirm_password else None
            else:
                return None
        elif password_type == '6-digit':
            new_password, ok = QInputDialog.getInt(self, "Set Password", "Enter your new 6-digit password:", min=100000, max=999999)
            if ok:
                confirm_password = get_confirm_password("Re-enter your new 6-digit password:")
                return str(new_password) if str(new_password) == confirm_password else None
            else:
                return None

    def set_password(self):
        if self.password_exists():
            QMessageBox.warning(self, "Error", "A password already exists. Use 'Change Password' to update your password.")
            return

        password_type, ok = QInputDialog.getItem(self, "Set Password", "Choose a password type:", ["Normal", "4-digit", "6-digit"], editable=False)

        if not ok:
            return

        new_password = self.set_new_password(password_type)

        if new_password:
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            stored_password = {"password": hashed_password.decode('utf-8')}

            with open("password.json", "w") as file:
                json.dump(stored_password, file)

            QMessageBox.information(self, "Success", "Password set successfully.")

    def change_password(self):
        if not self.password_exists():
            QMessageBox.warning(self, "Error", "No password set. Please set a password.")
            return

        old_password, ok1 = QInputDialog.getText(self, "Change Password", "Enter your old password:", QLineEdit.Password)

        if not ok1:
            return

        password_type, ok2 = QInputDialog.getItem(self, "Change Password", "Choose a new password type:", ["Normal", "4-digit", "6-digit"], editable=False)

        if not ok2:
            return

        new_password = self.set_new_password(password_type)

        if not new_password:
            return

        with open("password.json", "r") as file:
            stored_password = json.load(file)

        hashed_password = stored_password["password"].encode('utf-8')
        if bcrypt.checkpw(old_password.encode('utf-8'), hashed_password):
            new_hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            stored_password = {"password": new_hashed_password.decode('utf-8')}

            with open("password.json", "w") as file:
                json.dump(stored_password, file)

            QMessageBox.information(self, "Success", "Password changed successfully.")
        else:
            QMessageBox.warning(self, "Error", "Incorrect old password.")


class JournalEntry:
    def __init__(self, password):
        self.password = password
        self.text = ""

    def encrypt_entry(self):
        cipher = AES.new(self.password[:32], AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(self.text.encode('utf-8'), AES.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ciphertext).decode('utf-8')
        return json.dumps({'iv': iv, 'ciphertext': ct})

    def decrypt_entry(self, encrypted_data):
        encrypted_data = json.loads(encrypted_data)
        iv = b64decode(encrypted_data['iv'])
        ct = b64decode(encrypted_data['ciphertext'])
        cipher = AES.new(self.password[:32], AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')

    def save_entry(self, file_name):
        encrypted_data = self.encrypt_entry()
        with open(file_name, "w") as file:
            file.write(encrypted_data)

    def load_entry(self, file_name):
        with open(file_name, "r") as file:
            encrypted_data = file.read()
            try:
                plaintext = self.decrypt_entry(encrypted_data)
                self.text = plaintext
                return True
            except Exception as e:
                QMessageBox.warning(self, "Error", "Failed to decrypt journal entry. Make sure the password is correct.")
                return False
            

class JournalApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Show the login dialog
        login_dialog = LoginDialog(self)
        if login_dialog.exec_() != QDialog.Accepted:
            sys.exit()

        self.password = login_dialog.password

        # Configure the main window
        self.setWindowTitle("Basic Journaling App")
        self.setGeometry(100, 100, 800, 600)

        self.entries = []
        self.current_entry_index = -1
        
        # Set up text editor
        self.text_editor = QTextEdit(self)
        self.setCentralWidget(self.text_editor)

        # Set up menu bar
        menu_bar = self.menuBar()
        file_menu = QMenu("&File", self)
        menu_bar.addMenu(file_menu)

        # Set up actions
        load_action = QAction("&Load", self)
        load_action.setShortcut("Ctrl+O")
        load_action.triggered.connect(self.load_entry)

        save_action = QAction("&Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_entry)

        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        # Add actions to the file menu
        file_menu.addAction(load_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)
        

        # Set up menu bar
        menu_bar = self.menuBar()
        file_menu = QMenu("&File", self)
        menu_bar.addMenu(file_menu)

        self.settings_action = QAction("&Settings", self)
        self.settings_action.triggered.connect(self.open_settings)

        file_menu.addAction(self.settings_action)
        self.add_settings_button()  # Add this line to call the method

    def add_settings_button(self):
        toolbar = self.addToolBar("Settings")
        settings_icon = QIcon.fromTheme("preferences-system")
        settings_button = toolbar.addAction(settings_icon, "Settings")
        settings_button.triggered.connect(self.open_settings)


    def open_settings(self):
        if not self.password_exists():
            QMessageBox.warning(self, "Error", "Please set a password to login.")
            return

        password_dialog = PasswordDialog(self)
        if password_dialog.exec_() == QDialog.Accepted:
            # Password was entered correctly, open the settings
            QMessageBox.information(self, "Settings", "Settings button clicked!")

    def password_exists(self):
            try:
                with open("password.json", "r") as file:
                    json.load(file)
                    return True
            except FileNotFoundError:
                return False

    def encrypt_entry(self, plaintext):
        cipher = AES.new(self.password[:32], AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ciphertext).decode('utf-8')
        return json.dumps({'iv': iv, 'ciphertext': ct})

    def decrypt_entry(self, encrypted_data):
        encrypted_data = json.loads(encrypted_data)
        iv = b64decode(encrypted_data['iv'])
        ct = b64decode(encrypted_data['ciphertext'])
        cipher = AES.new(self.password[:32], AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')

    def load_entry(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Load Journal Entry", "", "Encrypted Text Files (*.encrypted);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "r") as file:
                encrypted_data = file.read()
                try:
                    plaintext = self.decrypt_entry(encrypted_data)
                    self.text_editor.setPlainText(plaintext)
                except Exception as e:
                    QMessageBox.warning(self, "Error", "Failed to decrypt journal entry. Make sure the password is correct.")

    def save_entry(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Journal Entry", "", "Encrypted Text Files (*.encrypted);;All Files (*)", options=options)
        if file_name:
            plaintext = self.text_editor.toPlainText()
            encrypted_data = self.encrypt_entry(plaintext)
            with open(file_name, "w") as file:
                file.write(encrypted_data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = JournalApp()
    main_window.show()
    sys.exit(app.exec_())