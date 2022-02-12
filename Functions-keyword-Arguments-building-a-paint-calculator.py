import math
def paint_calc(h, w, c):
    number_of_cans = (h * w) / c
    round_of_cans = math.ceil(number_of_cans)
    print(f"You'll need {round_of_cans} cans of paint.")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(h=test_h, w=test_w, c=coverage)
