#!/usr/bin/env python3
from bmimodule import bmiutils


def print_bmi(bmi):
    print('Your BMI is {0:.2f}'.format(bmi))


def print_verdict(bmi):
    verdict = bmiutils.bmi_verdict(bmi)
    print(verdict)


def main():
    weight = bmiutils.bmi_float(input('Weight(kg) = '))
    height = bmiutils.bmi_float(input('Height(cm) = '))
    bmi = bmiutils.bmi_calculate(weight, height)
    print_bmi(bmi)
    print_verdict(bmi)


if __name__ == '__main__':
    main()
