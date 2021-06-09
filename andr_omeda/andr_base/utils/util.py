def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    # https://stackoverflow.com/a/312464/9935473
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def is_string(var):
    return isinstance(var, str)


def is_dict(var):
    return isinstance(var, dict)


def is_bytes(var):
    return isinstance(var, bytes)
