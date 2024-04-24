"""Модуль настроек шарика."""

from tkinter import Canvas
from constants import (RADIUS_X, RADIUS_Y, X_0_BALL, Y_0_BALL,
                       WINDOW_HEIGHT, WINDOW_WIDTH)


class Ball:
    def __init__(self, canvas: Canvas, platform, score) -> None:
        self.canvas = canvas
        self.platform = platform
        self.score = score
        self.id = canvas.create_oval(X_0_BALL, Y_0_BALL,
                                     RADIUS_X, RADIUS_Y,
                                     fill='blue')
        self.canvas.move(self.id, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.x = self.y = -2
