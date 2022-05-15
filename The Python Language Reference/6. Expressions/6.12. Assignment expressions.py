# named expression or walrus expression

print((start := input("Do you want to start(y/n)?")) == "y")

# With parentheses
if (sum := 10 + 5) > 10:
    print(sum)  # return 15

# Without parentheses
if sum := 10 + 5 > 10:
    print(sum)  # return True
