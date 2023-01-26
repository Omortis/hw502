import os
os.system("cls")
# os.system("clear")

# Question 3
#
# Finish the function below that takes in the length of the two parallel
# sides of a trapezoid 𝑎 and 𝑏, which are separated by a distance h,
# and returns its area.
#
# Area of a trapezoid A = (h/2)(a + b)
# ---------------------------------------------------------------------


def area_of_trapezoid(a, b, h):
    return (h / 2)*(a + b)


print(area_of_trapezoid(3, 3, 5))
print(area_of_trapezoid(3, 4, 5))
