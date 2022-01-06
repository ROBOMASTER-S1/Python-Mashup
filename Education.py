'Minute Python Program Examples'

# Python Sets{}

# Let's create a set called my_set that will get rid of any duplicate values.

my_set={
    'a', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','z','z'}

# Let's view my_set, using a print() function to print my_set values inside the
# print() function to be able to see the output on the screen.

print(my_set) # my_set variable

# execute/run the program and see what happens

# Sets are not like tuples or lists. Sets have no indexes [:] and sets are always in
# random order as well. Re-execute/run this Python Program example a few more
# times to see what happens with the my_set variable values. They are always in
# random order, never repeating the same order they were supposed to be in.
# So let's do something about that!

convert=tuple(my_set) # use the tuple() function
sorted_values=sorted(convert) # sort the convert = tuple()
print(sorted_values) # sorted values variable

# or the:

convert=list(my_set) # use the list() function
sorted_values=sorted(convert) # sort the convert = list()
print(sorted_values) # sorted values variable

# Let's print the letter 'a' and 'z' on the screen

print(sorted_values[0]+sorted_values[25]) # forward indexing

print(sorted_values[0],sorted_values[25]) # forward indexing

# or this:

print(sorted_values[0]+sorted_values[-1]) # reverse indexing

print(sorted_values[0],sorted_values[-1]) # reverse indexing

# Let's print the entire alphabet with a for-loop

for i in sorted_values:
    print(i)

for i in sorted_values:
    print(i,end='') # the end = '' keeps the printout on the same line

# Try these end='' examples and see what happens when you re-
# execute/run this for-loop Python program example above.

# print(i,end='') # without a space
# print(i,end=' ') # with a space
# print(i,end=',') # with a comma
# print(i,end='-') # with hyphen
# print(i,end='+') # with plus sign
# print(i,end=' Hello ') # ' Hello '

# Sets are perfect for getting rid of duplicate values, but to be able
# to use them properly in Python programs, they must be converted to
# a tuple or a list first to be able to access their indexes [] value.

# Let's see how many alphabet letters there are in our converted set
# using the len() function

print(len(sorted_values))

# screen output:   26

# Let's check the sorted_values values

print(sorted_values) # no indexes []

# screen output:

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Note: the sort() function changes the actual list, but the sorted() function only
# changes the copy of the actual list, not the actual list itself. So be very careful
# on which sorting function you wish to use. Here is the one we used:

sorted_values=sorted(convert)

# Here is the sort() fuction we didn't use:

convert.sort()
print(convert)

# The sorted_values variable isn't there to be, only the copy of a modified list.
# In this case the actual list got midified instead, which might not be what you
# had in mind. So be very careful on which sorting() function you wish to use.
# Most of the time, it's much better to use the sorted() function than it would be
# to use the sort() function.

# Now you have a general idea of what sets{} are and how to properly use them
# in Python programs to make them work and do their job as they were designed.
# And that job is to get rid of any duplicate values only. Use sets if you have really
# large string values and you want to make sure there are no duplicate values by
# converting them to tuples or lists alike. However tuples aren't mutable, whereas
# lists are mutable. Use the list() function if you want to modify your values through-
# out the program's execution run.
'''----------------------------------------------------------------------------------------------------------------------'''
# Create a Python program that can calculate the MEAN
# of a set of number values

numbers=(1,2,3,4,5)
addition=sum(numbers)
mean=(len(numbers))
answer=(addition/mean)

print('The total sum =',f'{addition} \
and the total mean =',f'{mean} \
\n\n{addition}/{mean} = {answer}')

'''----------------------------------------------------------------------------------------------------------------------'''
# Order of Operation-bedmas_list example 1:

# Multiplication and Division always hold
# the presidency over addition and subtraction.
# Use a single asterisk * to create multiplication.

bedmas_list=(
    2*2+4,2+4*2,4+2*2,
    2*2-4,2-4*2,4-2*2,
    2/2+4,2+4/2,4+2/2,
    2/2-4,2-4/2,4-2/2)

for i in bedmas_list:
    print(int(i))

# Order of Operation-bedmas_list example 2:

# exponents always hold the presidency over
# multiplication and division, as well as addition
# and subtraction alike. Use a double asterisk **
# to create exponents

bedmas_list=(
    2*2**4,2**4*2,2/2**4,
    2**4/2,2+2**4,2**4+2,
    2-2**4,2**4-2
    )

for i in bedmas_list:
    print(int(i))
