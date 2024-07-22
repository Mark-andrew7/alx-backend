#!/usr/bin/env python3
"""
function returns tuple of size two containing a start index and an end index
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    function returns tuple of size two containing start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)
