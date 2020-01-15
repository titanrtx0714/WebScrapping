"""
Unit tests for the kontext library.
"""


import logging

from kontext import extract
from lxml import html



logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def test_titles():
    '''Test the extraction of titles'''
    title, _ = extract('<html><head><title>Test Title</title></head><body></body></html>')
    assert title == 'Test Title'


def test_dates():
    '''Simple tests for date extraction (most of the tests are carried out externally for htmldate module)'''
    _, date = extract('<html><head><meta property="og:published_time" content="2017-09-01"/></head><body></body></html>')
    assert date == '2017-09-01'


if __name__ == '__main__':
    test_titles()
    test_dates()
