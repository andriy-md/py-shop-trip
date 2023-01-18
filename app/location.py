from __future__ import annotations
from math import sqrt


class Location:
    def __init__(self, coordinates: list) -> None:
        self.x, self.y = coordinates

    def distance_to_other_location(self, other: Location) -> int | float:
        distance = sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        )
        return distance
