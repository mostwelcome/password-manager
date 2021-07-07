"""Driver code."""
from password_manager import PasswordManager


password_manager = PasswordManager()
password_manager._set_window()
password_manager._set_canvas()
password_manager._set_labels()
password_manager._set_entries()
password_manager._set_buttons()
password_manager.render_window()
