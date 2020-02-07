def slices(series, length):

    if len(series) < length or length <= 0:
        raise ValueError("Length is less then 0 or higher then string length", length, len(series))

    return [series[x:x+length] for x in range(0,len(series)) if x+length <= len(series)]


