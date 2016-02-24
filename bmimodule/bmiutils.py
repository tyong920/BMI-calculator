def bmi_float(value):
    """
    convert input value to float
    :param value: input number
    :return: float(value)
    """

    # assume input is a number
    try:
        return float(value)
    except:
        return 0.0


def bmi_calculate(weight, height):
    """
    calculate BMI
    :param weight: weight in kg
    :param height: height in cm
    :return: reslut of the bmi calculation or 0 if division by 0 had occurred
    """

    w = bmi_float(weight)
    h = bmi_float(height) / 100  # cm to m

    try:
        return w / pow(h, h)
    except ZeroDivisionError:
        print('Division by Zero')
        return 0.0


def bmi_verdict(bmi):
    if bmi < 18.5:
        verdict = 'You\'re underweight, eat more to keep healthy. '
    elif 18.5 <= bmi <= 24.9:
        verdict = 'You\'re of normal weight, try to keep it.'
    elif 24.9 < bmi < 30:
        verdict = 'You\'re overweight.'
    else:
        verdict = 'You\'re obese, do something!'

    return verdict
