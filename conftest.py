import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture(scope='session')
def list_of_test_books():
    list_of_test_books = [
                          'Гордость и предубеждение и зомби',
                          'Что делать, если ваш кот хочет вас убить',
                          'Принесенные ветром'
                         ]
    return list_of_test_books
