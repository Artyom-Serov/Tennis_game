"""Модуль настроек отображения и поведения рокетки."""

from tkinter import Canvas

from positions import Position
from constants import (LENGHT_RACKET, HEIGHT_RACKET, X_0_RACKET, Y_0_RACKET,
                       VECTOR_LEFT, VECTOR_RIGHT, WINDOW_HEIGHT, WINDOW_WIDTH)


class Racket:
    def __init__(self, canvas: Canvas) -> None:
        self.canvas = canvas
        self.id = canvas.create_rectangle(X_0_RACKET, Y_0_RACKET,
                                          LENGHT_RACKET, HEIGHT_RACKET,
                                          fill='red')
        self.canvas.move(self.id, WINDOW_WIDTH // 2 - LENGHT_RACKET // 2,
                         WINDOW_HEIGHT - 50)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)

    def move_right(self, event):
        self.x = VECTOR_RIGHT

    def move_left(self, event):
        self.x = VECTOR_LEFT

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        position = Position(*self.canvas.coords(self.id))

        if position.x_up_left <= 0:
            self.x = 0
        elif position.x_down_right >= WINDOW_WIDTH:
            self.x = 0
