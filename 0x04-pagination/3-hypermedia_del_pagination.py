#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """returns a dictionary containing meta data about the page

        Args:
            index (int, optional): key where to start. Defaults to None.
            page_size (int, optional): limit of data. Defaults to 10.

        Returns:
            Dict: key/value pair of metadata
        """
        assert index < len(self.__indexed_dataset)

        data = {}
        for i in range(index, index + page_size):
            if i in self.__indexed_dataset:
                data[i] = self.__indexed_dataset[i]

        hyper_index = {
            "index": index,
            "data":  list(data.values()),
            "page_size": len(data),
            "next_index": max(data.keys())+1,
        }
        return hyper_index
