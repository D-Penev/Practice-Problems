def string_splosion(str):
    test = ""
    for x in range(len(str)):
        test += str[0:x + 1]

    return test