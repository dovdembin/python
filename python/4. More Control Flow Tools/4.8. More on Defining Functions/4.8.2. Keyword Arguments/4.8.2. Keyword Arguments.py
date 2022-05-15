# ========================================
def keyword_and_positional_argument(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


keyword_and_positional_argument(1000)  # 1 positional argument
keyword_and_positional_argument(voltage=1000)  # 1 keyword argument
keyword_and_positional_argument(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
keyword_and_positional_argument(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
keyword_and_positional_argument('a million', 'bereft of life', 'jump')  # 3 positional arguments
keyword_and_positional_argument('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# keyword_and_positional_argument()                     # required argument missing
# keyword_and_positional_argument(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# keyword_and_positional_argument(110, voltage=220)     # duplicate value for the same argument
# keyword_and_positional_argument(actor='John Cleese')  # unknown keyword argument
