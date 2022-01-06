'Minute Python Program Examples'

# *Args and **Kwargs. What are they?

# whenever you create functions that involve variables
# inside the function's empty parentheses; these are called
# 'ARGUMENTS'. As you can see, there are three argument
# variables: my_arg1 my_arg2 and my_arg3. The 'my_arguments()'
# function has three parameters, which contain these three
# argument variable names. However, if you don't supply the
# proper amount of returned argument values inside the 'print()'
# function, you will get an error, crashing your program on the
# spot.

def my_arguments(my_arg1,my_arg2,my_arg3): # fixed number of three parameter variables
    return'My arg 1 has been returned safe and sound.'

print(my_arguments(
    'Return my arg 1',
    'Return my arg 2',
    'Return my arg 3')) # fixed number of three argument values

# To get around this problem, we can use the ' *args ' implementer
# instead. Say you had far too many argument variables, but you
# don't want to fill the 'my_arguments()' function with endless
# parameters, you can use ' *args '. For example, consider the
# following:

def my_arguments(*args): # unknown number of parameter variables
    return'My arg 1 has been returned safe and sound.'

print(my_arguments(
    'Return my arg 1',
    'Return my arg 2',
    'Return my arg 3',
    'Return my arg 4')) # unlimited argument values

# Keyword arguments can also be shortened in your Python code as
# well with the ' **kwargs ' implementer. In this example the ' **kwargs '
# implementer is in place of any keyword arguments, which would
# normally be inside the 'print()' function's 'print' statement's inner
# closed parentheses, due to the function's caller 'my_keyword_arguments()'
# inside the 'print()' function itself.

def my_keyword_arguments(**kwargs): # unknown number of keyword arguments
    return'My kwarg 1 has been returned safe and sound.'

print(my_keyword_arguments()) # no argument values needed

# Here is when you can actually see the inconvenience of using physical
# keywords all the time. Especially if you have no idea just how many
# arguments you might need or how many keyword arguments you might
# need. These two implementers can save you a whole lot of time and
# energy.

def my_keyword_arguments(keyward_argument): # one fixed argument variable
    return'My kwarg 1 has been returned safe and sound.'

print(my_keyword_arguments(
    'This is a physical argument value')) # one fixed argument value

# Note: You can name the *args and **kwargs implementers any name you
# like however, you must assign either one asterisk ' * ' for the 'args' implementer,
# or a double asterisk ' ** ' for the 'kwargs' implementer. For example:

def my_arguments(*my_args): # unknown number of parameter variables
    return'My arg 1 has been returned safe and sound.'

print(my_arguments(
    'Return my arg 1',
    'Return my arg 2',
    'Return my arg 3',
    'Return my arg 4')) # unlimited argument values

def my_keyword_arguments(**my_keyword_args): # unknown number of keyword arguments
    return'My kwarg 1 has been returned safe and sound.'

print(my_keyword_arguments()) # no argument values needed

# Note: the ' *args ' and ' **kwargs ' implementer names are always the standard
# to Python programmers. Use 'args' and kwargs' implementer names only.

# Now you know what ' *args ' and ' **kwargs ' are, but in most case scenarios
# you won't always need to use them. However, with large complex programs,
# sometimes these little things in Python can go a long way, which also drastically
# reduces redundant code on the programmer's part, while cutting though all the
# confusion at the same time. It's like killing two birds with only one stone's throw.
