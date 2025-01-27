"""Tea Party"""

_author_: str = "730664602"


def main_planner(guests: int) -> None:
    """The Main Plan for Tea Party"""


print("A Cozy Tea Party for" + " " + str(guests) + " " + "People!")
print("Tea_bags:" + " " + str(tea_bags(people=guests)))
print("Treats:" + " " + str(treats(people=guests)))


def tea_bags(people: int) -> int:
    """Calculating Number of Tea Bags"""
    return people * 2


def treats(people: int) -> int:
    """Calculating Number of Treats"""
    return int(tea_bag(people=people)) * 1.5


def cost(tea_count: int, treat_count: int) -> float:
    """Total Cost of Tea Bags and Treats"""
