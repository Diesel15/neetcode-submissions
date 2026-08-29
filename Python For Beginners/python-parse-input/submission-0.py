from typing import List

def read_integers() -> List[int]:
    user_input = input()
    x = user_input.split(",")
    y = []
    for z in range(len(x)):
        y.append(int(x[z]))
    return y
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
