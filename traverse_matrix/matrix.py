import asyncio
from typing import List

import aiohttp
import aiohttp.web


def clean_matrix(string: str) -> List:
    """
    Function to matrix from raw string.
    :param string: string to prepare
    :return: prepared matrix
    """
    matrix = []
    string = string.splitlines()
    for i in range(1, len(string), 2):
        matrix.append([int(i) for i in string[i].replace("|", "").split()])
    return matrix


def traverse_matrix(matrix: List) -> List[int]:
    """
    Function to spiral traverse matrix counter clockwise order.
    :param matrix: prepared matrix
    :return: traversed matrix
    """

    left_border, right_border = 0, len(matrix[0])
    top_border, bot_border = 0, len(matrix)
    matrix_path = []

    while left_border < right_border and top_border < bot_border:

        for i in range(top_border, bot_border - 1):
            matrix_path.append(matrix[i][left_border])
        left_border += 1

        for i in range(left_border - 1, right_border):
            matrix_path.append(matrix[bot_border - 1][i])
        bot_border -= 1

        if not (left_border < right_border and top_border < bot_border):
            break

        for i in range(bot_border - 1, top_border - 1, -1):
            matrix_path.append(matrix[i][right_border - 1])
        right_border -= 1

        for i in matrix[top_border][right_border - 1: left_border - 1: -1]:
            matrix_path.append(i)
        top_border += 1

    return matrix_path


async def get_matrix(url: str) -> List[int]:
    """
    Function to get text from url async.
    :param url: url to get data
    :return: traversed matrix from data.
    """
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    print(f"Status: {resp.status}")
                    print(f"Content type: {resp.headers['content-type']}")
                    matrix = await resp.text()
                else:
                    print(resp.status)
        except aiohttp.ClientConnectionError as e:
            print(f'Connection Error {e}')
    cleaned_matrix = clean_matrix(matrix)
    final_path = traverse_matrix(cleaned_matrix)
    return final_path

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
