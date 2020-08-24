def _front_times(str,n):
    if(len(str) < 3):
        return str * n
    return (str[0] + str[1] + str[2]) * n