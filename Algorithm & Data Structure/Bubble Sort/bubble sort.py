my_string = "laiwejfgcxiewjmfgiwejamxnzbnbwuiooprfglwixwjlw"
char_list = list(my_string)

for i in range(0, len(char_list) - 1):
    for j in range(0, len(char_list) - i - 1):
        if char_list[j] > char_list[j + 1]:
            tmp = char_list[j]
            char_list[j] = char_list[j + 1]
            char_list[j + 1] = tmp

print(char_list)
