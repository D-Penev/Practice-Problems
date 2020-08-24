def without_end(str):
    result = list(str)
    result.pop(0)
    result.pop(-1)
    return ''.join(result)