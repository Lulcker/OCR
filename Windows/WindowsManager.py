from enum import Enum


class WindowsNames(Enum):

    MainWindow = 1
    EditPersonWindow = 2


class WindowsManager:

    def __init__(self):
        self.windows = dict()

    def show_window(self, window_name):
        self.windows[window_name].show()

    def close_window(self, window_name):
        self.windows[window_name].close()
