def bmi(weight, height):
    num = weight/(height ** 2)
    if num <= 18.5:
        return "Underweight"
    elif num <= 25.0:
        return "Normal"
    elif num <= 30.0:
        return "Overweight"
    elif num > 30:
        return "Obese"