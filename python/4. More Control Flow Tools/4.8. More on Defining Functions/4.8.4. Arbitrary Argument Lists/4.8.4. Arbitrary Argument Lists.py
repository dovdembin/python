# ========================================
def arbitrary_arguments_args(*names):
    """This function greets all the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


arbitrary_arguments_args("Monica", "Luke", "Steve", "John")


# ========================================
def arbitrary_arguments_kwargs(**keywords):
    for kw in keywords:
        print(kw, ":::::", keywords[kw])


arbitrary_arguments_kwargs(shopkeeper="Michael Palin", client="John Cleese", sketch="Cheese Shop Sketch")


# ========================================
def arbitrary_arguments3(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print("-" * 40)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


arbitrary_arguments3("Limburger",
                     "It's very runny, sir.",
                     "It's really very, VERY runny, sir.",
                     shopkeeper="Michael Palin",
                     client="John Cleese",
                     sketch="Cheese Shop Sketch")


# ===========================================