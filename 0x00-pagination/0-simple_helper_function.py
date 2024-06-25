#!/usr/bin/env python3
""" Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start
        and end indices (inclusive) for the given page.

    Example:
        >>> index_range(2, 10)
        (10, 20)
        This would return the start and end indices
        for the second page, with 10 items per page.
    """
    start = (page - 1) * page_size
    end = page * page_size
    # print(f"starting index: {start}")
    # print(f"last index: {end}")
    return start, end
