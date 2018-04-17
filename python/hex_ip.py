def hexIpToIntIP(string):
    # C0:A8:01:01
    if string is not None:
        tmp_arr = string.replace(":", " ").split()
        return '.'.join(str(int(string_num.upper(), 16)) for string_num in tmp_arr)
    else:
        return None