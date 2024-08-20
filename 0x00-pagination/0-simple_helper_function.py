#!/usr/bin/env python3
"""
This module provides a simple helper
function to load index range of a page.
"""


def index_range(page, page_size):
    """
    Return a tuple that contains the
    start and end index of a page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
