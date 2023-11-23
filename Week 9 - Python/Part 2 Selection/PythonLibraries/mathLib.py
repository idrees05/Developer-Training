import math  # import the math library/class/module

radius = float(input("Enter radius: "))
area = math.pi * radius ** 2

print(f"The area is {area}")

# method 1
print(f"The area displayed is rounded to 2 decimal places {area:.2f}")
# exercise: modify the code above to round to 3 decimal places


# method 2
"Complete the code block below to use the floor method to round down nearest whole number"
roundDown = math
print(f"The area is rounded down to the nearest whole number: {roundDown}")


# method 3
"Complete the code block below to use the ceil method to round up to nearest whole number"
roundUp = math.ceil(area)
print(f"The area is rounded up to the nearest whole number: {roundUp}")

# method 4
"Complete the code block below to use the round method to round up to two decimal places"
print(f"Using the round method:{(area, 2)}")
