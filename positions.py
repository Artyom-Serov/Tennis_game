"""Модуль настроек позиций шарика и рокетки."""

from dataclasses import dataclass


@dataclass
class Position:
    x_up_left: int
    y_up_left: int
    x_down_right: int
    y_down_right: int
