#!/usr/bin/env python3
"""2-hypermedia_pagination"""

import csv
import math
from typing import List, Dict, Union

index_range = __import__("0-simple_helper_function").index_range


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
        """get data set

        Args:
            page (int, optional): number of page. Defaults to 1.
            page_size (int, optional): size or limit of the page.
            Defaults to 10.

        Returns:
            List[List]: data set filtered by page indexes
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indexes = index_range(page, page_size)
        start = indexes[0]
        end = indexes[1]

        try:
            return self.dataset()[start:end]
        except Exception:
            return []

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Union[int, List[List]]]:
        """returns a dictionary containing meta data about the page

        Args:
            page (int, optional): number of page. Defaults to 1.
            page_size (int, optional): size or limit of the page.
            Defaults to 10.

        Returns:
            Dict[str, Union[int, List[List]]]: key/value pair of metadata
        """
        data = self.dataset()
        page_data = self.get_page(page, page_size)
        page_len = len(page_data)
        total_pages = math.ceil(len(data) / page_size)
        next_page = page + 1 if total_pages > page else None
        prev_page = page - 1 if page != 1 else None

        hyper = {
            'page_size': page_len,
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return hyper
