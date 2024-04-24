"""Модуль настроек шарика."""

from dataclasses import dataclass
from tkinter import Canvas
from constants import (RADIUS_X, RADIUS_Y, X_0_BALL, Y_0_BALL,
                       WINDOW_HEIGHT, WINDOW_WIDTH)


class Ball:
    def __init__(self, canvas: Canvas, racket, score) -> None:
        self.canvas = canvas
        self.racket = racket
        self.score = score
        self.id = canvas.create_oval(X_0_BALL, Y_0_BALL,
                                     RADIUS_X, RADIUS_Y,
                                     fill='blue')
        self.canvas.move(self.id, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.x = self.y = -2
        self.fell_down = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        positions = Position(*self.canvas.coords(self.id))

        if positions.y_down_right >= WINDOW_HEIGHT:
            self.fell_down = True
            return
        if positions.y_up_left <= 0:
            self.y = 2
        if self.hit_the_racket(positions):
            self.score.add()
            self.y = -2

    def hit_the_racket(self, positions: 'Position') -> bool:
        racket_position = Position(*self.canvas.coords(self.racket.id))
        return (
            positions.x_down_right >= racket_position.x_up_left and
            positions.x_up_left <= racket_position.x_down_right and
            racket_position.y_up_left <= positions.y_down_right <=
            racket_position.y_down_right
        )


@dataclass
class Position:
    x_up_left: int
    y_up_left: int
    x_down_right: int
    y_down_right: int
