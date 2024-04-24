"""Модуль настроек отображения и поведения рокетки."""

from tkinter import Canvas
from constants import (LENGHT_RACKET, HEIGHT_RACKET, X_0_RACKET, Y_0_RACKET,
                       WINDOW_HEIGHT, WINDOW_WIDTH)


class Racket:
    def __init__(self, canvas: Canvas) -> None:
        self.canvas = canvas
        self.id = canvas.create_rectangle(X_0_RACKET, Y_0_RACKET,
                                          LENGHT_RACKET, HEIGHT_RACKET,
                                          fill='red')
        self.canvas.move(self.id, WINDOW_WIDTH // 2 - LENGHT_RACKET // 2,
                         WINDOW_HEIGHT - 50)
        self.x = 0
