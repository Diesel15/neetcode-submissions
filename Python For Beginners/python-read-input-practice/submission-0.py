def add_two_numbers() -> int:
    user_input = input()
    x = user_input.split(",")
    sumx = 0
    for z in range(len(x)):
        sumx += int(x[z])
    return sumx
# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
