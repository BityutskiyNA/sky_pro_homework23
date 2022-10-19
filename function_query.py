

def filter_query(param, data):
    return list(filter(lambda x: param in x, data))


def map_query(param, data):
    col_num = int(param)
    return list(map(lambda x: x.split(' ')[col_num], data))


def unique_query(data, *args, **kwargs):
    return list(set(data))


def sort_query(param, data):
    rev = False if param == 'asc' else True
    return sorted(data, reverse=rev)


def limit_query(param, data):
    limit = int(param)
    return list(data[:limit])