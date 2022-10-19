from typing import Dict, Callable

import function_query

CMD_FUNCT: Dict[str, Callable] = {
    'filter': function_query.filter_query,
    'map': function_query.map_query,
    'unique': function_query.unique_query,
    'sort': function_query.sort_query,
    'regex': function_query.regex,
    'limit': function_query.limit_query
}
FILE_NAME: str = 'data/apache_logs.txt'


def build_query(cmd1: str, cmd2: str, param1: str, param2: str):
    with open(FILE_NAME) as file:
        data = list(map(lambda x: x.strip(), file))
    rez = CMD_FUNCT[cmd1](param=param1, data=data)
    return CMD_FUNCT[cmd2](param=param2, data=rez)

