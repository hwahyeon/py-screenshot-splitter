from tkinter import filedialog, messagebox
import os
import platform
from langs import get_text
from database import load_setting, save_setting


def open_folder(event=None):
    save_folder = load_setting('save_folder')

    if platform.system() == "Windows":
        os.startfile(save_folder)
    elif platform.system() == "Darwin":
        # macOS
        os.system(f"open {save_folder}")
    else:
        # Linux
        os.system(f"xdg-open {save_folder}")


def change_folder_location(save_folder, save_setting, current_language):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        save_folder = folder_selected
        save_setting('save_folder', save_folder)
        messagebox.showinfo(get_text(current_language, "folder_change_title"),
                            (get_text(current_language, "folder_change_cont") + '\n' + save_folder))
