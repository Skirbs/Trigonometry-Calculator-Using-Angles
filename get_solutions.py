import math


def get_solutions(angle, decimal_places):  # angle is in radians
    """Returns a dictionary of solved trigonometric ratio"""
    angle_in_degrees = math.degrees(angle)

    sine_answer = round(math.sin(angle), decimal_places)
    cosine_answer = round(math.cos(angle), decimal_places)
    if angle_in_degrees % 90 == 0 and angle_in_degrees % 180 != 0:
        # Since values at these degrees are infinite, it will return "N/A"
        tangent_answer = "N/A"
    else:
        tangent_answer = round(math.tan(angle), decimal_places)

    try:
        cosecant_answer = round(1 / sine_answer, decimal_places)
    except:
        cosecant_answer = "N/A"
    try:
        secant_answer = round(1 / cosine_answer, decimal_places)
    except:
        secant_answer = "N/A"
    try:
        cotangent_answer = round(
            1 / round(math.tan(angle), decimal_places), decimal_places
        )
    except:
        cotangent_answer = "N/A"

    answers_dict = {
        "sine": sine_answer,
        "cosine": cosine_answer,
        "tangent": tangent_answer,
        "cosecant": cosecant_answer,
        "secant": secant_answer,
        "cotangent": cotangent_answer,
    }

    for key, values in answers_dict.items():
        # Some bug makes values -0.0, so it converts it back to 0
        if values == -0.0:
            answers_dict[key] = 0

    return answers_dict
