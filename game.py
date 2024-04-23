"""Модуль настроек запуска игры."""

from tkinter import Canvas, Tk
from constants import WINDOW_WIDTH, WINDOW_HEIGHT


if __name__ == '__main__':
    app = Tk()
    app.title('Tennis')
    app.resizable(0, 0)
    app.wm_attributes('-topmost', 1)

    canvas = Canvas(app, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack()

    screen_width = app.winfo_screenmmwidth()
    screen_height = app.winfo_screenmmheight()

