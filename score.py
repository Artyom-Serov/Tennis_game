"""Модуль управления счётом очков."""

from tkinter import Canvas

from constants import SCORE_STEP, X_0_SCORE, Y_0_SCORE


class Score:
    def __init__(self, canvas: Canvas) -> None:
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(X_0_SCORE, Y_0_SCORE,
                                     text=self.score, fill='green')

    def add(self):
        self.score += SCORE_STEP
        self.canvas.itemconfig(self.id, text=self.score)
