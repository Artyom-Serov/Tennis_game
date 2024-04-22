"""Модуль настроек запуска игры."""

from tkinter import Canvas, Tk


if __name__ == '__main__':
    app = Tk()
    app.title('Tennis')
    app.resizable(0, 0)
    app.wm_attributes('-topmost', 1)
