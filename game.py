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

    x = (screen_width/2) - (WINDOW_WIDTH/2)
    y = (screen_height/2) - (WINDOW_HEIGHT/2)

    app.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, x, y))
    app.update()

    app.mainloop()
