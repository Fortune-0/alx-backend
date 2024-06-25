#!/usr/bin/env python3
"""
Defines class Server that paginates a database of popular baby names
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Method that returns all the desired pages"""
        assert isinstance(page_size, int) and page_size > 0
        assert isinstance(page, int) and page > 0
        dataset_len = len(self.dataset())
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []
