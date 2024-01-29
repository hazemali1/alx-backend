#!/usr/bin/env python3
"""csv, math, typing modules"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """tuples index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        if index_range(page, page_size)[0] > len(self.dataset()):
            return []
        if index_range(page, page_size)[1] > len(self.dataset()):
            return []
        t = index_range(page, page_size)
        s = t[0]
        d = t[1]
        data = self.dataset()
        return [data[s:d]]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """get hyper"""
        if page + 1 > len(self.dataset()) - 1:
            n = page + 1
        else:
            n = None
        return {
			"page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page. page_size),
            "next_page": n,
            "prev_page": page - 1,
            "total_pages": (len(self.dataset()) + page_size - 1) // page_size
		}

