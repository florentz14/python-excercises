# -------------------------------------------------
# File Name: ITSE-1003/Examples/oop_20.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Enum with class state.
# -------------------------------------------------

from enum import Enum, auto


class TrafficLightState(Enum):
    RED = auto()
    YELLOW = auto()
    GREEN = auto()


class TrafficLight:
    def __init__(self) -> None:
        self.state = TrafficLightState.RED

    def next(self) -> None:
        if self.state == TrafficLightState.RED:
            self.state = TrafficLightState.GREEN
        elif self.state == TrafficLightState.GREEN:
            self.state = TrafficLightState.YELLOW
        else:
            self.state = TrafficLightState.RED


def main() -> None:
    light = TrafficLight()
    for _ in range(4):
        print("Current state:", light.state.name)
        light.next()


if __name__ == "__main__":
    main()
