"""A tiny project with one intentional bug for the course exercises."""


def average_duration(values: list[int]) -> float:
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) // len(values)  # Intentional bug: integer division.
