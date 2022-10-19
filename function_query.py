import re
from typing import Iterator


def filter_query(param: str, data: list[str]) -> list[str]:
    return list(filter(lambda x: param in x, data))


def map_query(param: str, data: list[str]) -> list[str]:
    col_num = int(param)
    return list(map(lambda x: x.split(' ')[col_num], data))


def unique_query(data: list[str], *args, **kwargs) -> list[str]:
    return list(set(data))


def sort_query(param: str, data: list[str]) -> list[str]:
    rev = False if param == 'asc' else True
    return sorted(data, reverse=rev)


def limit_query(param: str, data: list[str]) -> list[str]:
    limit = int(param)
    return list(data[:limit])


def regex(param: str, data: list[str]) -> list[str]:
    return [x for x in get_plates(data, param)]


def get_plates(letters: list[str], param: str) -> Iterator[str]:
    for item in letters:
        for p in re.findall(rf"{param}", item):
            yield item
