# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt: as a senior Python developer, review this code and find/fix the bug:**

**AI's Corrected Code:
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        # Fixed: even numbers have a remainder of 0 when divided by 2
        if num % 2 == 0:  
            total += num
    return total** ```python
# AI's fixed version of the code

## Problem 2: Refactoring

**My Prompt: help me factor this code to be more clear, concise, and idiomatic as a senior Python developer:**

**AI's Corrected Code:
def get_names_of_adults(users: list[dict]) -> list[str]:
    """Return names of users who are 18 or older."""
    return [user['name'] for user in users if user['age'] >= 18] ```python 
# AI's fixed version of the code

## Problem 3: Documenting

**My Prompt:**
> You are senior Python developer. Review this code and help me write a professional NumPy-style docstring for this function:

**AI's Corrected Code:def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float
        The length of the rectangle. Must be a positive number.
    width : float
        The width of the rectangle. Must be a positive number.

    Returns
    -------
    float
        The calculated area of the rectangle.

    Raises
    ------
    ValueError
        If either `length` or `width` is less than or equal to zero.

    Examples
    --------
    >>> calculate_area(5.0, 4.0)
    20.0
    >>> calculate_area(10, 2)
    20.0
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width**```python
# AI's fixed version of the code

# Testing GitHub Upload
