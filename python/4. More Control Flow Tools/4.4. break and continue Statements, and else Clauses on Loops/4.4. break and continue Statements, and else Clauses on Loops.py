def break_():
    for i in range(0, 3):
        if i == 2:
            print("2")
            break
    else:
        print("end of loop")


def continue_():
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found an odd number", num)