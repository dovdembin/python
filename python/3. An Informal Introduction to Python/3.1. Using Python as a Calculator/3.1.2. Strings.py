str1 = 'spam eggs'  # single quotes
str2 = 'doesn\'t'  # use \' to escape the single quote...
str3 = "doesn't"  # ...or use double quotes instead
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'  # \n means newline
print(s)  # with print(), \n produces a new line
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

# End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line
print("""\ 
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
# Strings can be concatenated
print(3 * 'un' + 'ium')  # 3 times 'un', followed by 'ium'
print('Py' 'thon')  # Two or more string literals next to each other are automatically concatenated.
text = ('Put several strings within parentheses '
        'to have them joined together.')  # break long strings
prefix = 'Py'
python = prefix + 'thon'
word = 'Python'
print(word[0])  # character in position 0 'P'
print(word[-1])  # last character counting from the right:

# ###################### slicing ##################################

print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)
print(word[:2])  # character from the beginning to position 2 (excluded)
print(word[4:])  # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end
print(word[:2] + word[2:])  # 'Python'
print(word[-6])
print(word[4:42])  # 'on'
print(word[42:])  # ''
s = 'supercalifragilisticexpialidocious'
print(len(s))

