#!/usr/bin/env python3
"""
This module provides a simple helper
function to load index range of a page.
"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Return a tuple that contains the
    start and end index of a page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset.
        """
        print(page, page_size)
        assert isinstance(page, int) and isinstance(
            page_size, int
        ), "raised when page and/or page_size are not ints"
        assert page != 0 and page_size != 0, "raised with 0"
        assert page > 0 and page_size > 0, "raised with negative values"

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index]


if __name__ == "__main__":
    server = Server()
    print(server.get_page(1, 3))
