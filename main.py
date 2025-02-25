def flick_switch(lst):
    result = []
    flick = True
    for item in lst:
        if item == "flick":
            flick = not flick
        result.append(flick)
    return result
