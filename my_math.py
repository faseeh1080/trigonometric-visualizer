def tan_csc_sec_cot_from_sin_cos(sin: float, cos:float) -> tuple:
    """Returns 'Undefined' for tan, csc, sec, or cot if their respective denominators are zero"""
    if cos == 0:
        tan = "Undefined"
    else:
        tan = sin / cos
    if sin == 0:
        csc = "Undefined"
    else:
        csc = 1 / sin
    if cos == 0:
        sec = "Undefined"
    else:
        sec = 1 / cos
    if tan == "Undefined" or tan == 0:
        cot = "Undefined"
    else:
        cot = 1 / tan

    return tan, csc, sec, cot