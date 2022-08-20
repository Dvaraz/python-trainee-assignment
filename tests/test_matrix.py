import asyncio

from traverse_matrix.matrix import clean_matrix, get_matrix, traverse_matrix

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/' \
             'python-trainee-assignment/main/matrix.txt'
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]

CLEANED_MATRIX = [[10, 20, 30, 40],
                  [50, 60, 70, 80],
                  [90, 100, 110, 120],
                  [130, 140, 150, 160]]


def test_clean_matrix():
    with open('matrix.txt') as file:
        assert clean_matrix(file.read()) == CLEANED_MATRIX


def test_traverse_matrix():
    assert traverse_matrix(CLEANED_MATRIX) == TRAVERSAL


def test_get_matrix():
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL
