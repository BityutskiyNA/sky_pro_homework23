import function_query

CMD_FUNCT = {
    'filter': function_query.filter_query,
    'map': function_query.map_query,
    'unique': function_query.unique_query,
    'sort': function_query.sort_query,
    'limit': function_query.limit_query
}
FILE_NAME = 'data/apache_logs.txt'

def build_query(cmd1, cmd2, param1, param2):
    with open(FILE_NAME) as file:
        data = list(map(lambda x: x.strip(), file))

    rezult = CMD_FUNCT[cmd1](param=param1, data=data)
    return CMD_FUNCT[cmd2](param=param2, data=rezult)
