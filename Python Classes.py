# Welcome to Python Classes

# Classes in Python can hold multiple objects,
# such as variables, values and 'def()' functons
# alike. However classes cannot work correctly
# without anything to call up from them. In the
# example below, when we run the program,
# it works without having to call up anything;
# as if we just wrote a simple 'print' string and
# wasted time creating a class. Classes have to
#return values through their variables inside
# the class code blocks.

class Not_correct:
  print('This is not how a class object works.')

'''----------------------------------------------------------------'''
# Let's create our first single class and call up its
# class name and its variable name

class Correct: # class name
  first_name='This is how a class object works.' # variable name with its green string value

# Let's call up both the class name and the variable name

print(Correct.first_name)

# screen output:    This is how a class object works.
'''----------------------------------------------------------------'''
# Let's create a single class called Programmer
# and let's also create variables for my first name,
# my middle name and my last name. Make sure
# to keep your code block indented.

class Programmer:
  first_name='Joesph'
  middle_name='C.'
  last_name='Richardson'

# Let's call both the class and it's contents inside
# these three 'print' statements. First, let's call up
# the class: 'Programmer' and then call up each
# variable inside the class code block with a period.

print(Programmer.first_name) # class name.variable name
print(Programmer.middle_name)
print(Programmer.last_name)
'''----------------------------------------------------------------'''
# Let's create a single class called 'Programmer
# and create a variable with three string values
# inside it.

class Programmer:
    full_name='Joesph','C.','Richardson'

# Let's call up the class name and each value inside
# the class code block. Just like tuples and lists,
# we must call up each value by its indices/index '[0]'.
# Invoke the (end=' ') to keep text output on the
# same line.

print(Programmer.full_name[0],end=' ')
print(Programmer.full_name[1],end=' ')
print(Programmer.full_name[2])

# screen output:    Joesph C. Richardson
'''----------------------------------------------------------------'''
# Let's create a for-loop that does the very same
# job as the above program example showed.

class Programmer:
    full_name='Joesph','C.','Richardson'

# The for-loop made possible that we only have
# to use one 'print' statement, not three as was
# the case before.

for i in range(3):
    print(Programmer.full_name[i],end=' ')
'''----------------------------------------------------------------'''
# Let's create a single class that calls up a 'def()'
# function, along with its variables.

name='Joesph','C.','Richardson'

class Programmer:
    def full_name():
        print(name[0],end=' ')
        print(name[1],end=' ')
        print(name[2])

# Let's call up the clas name first, followed by
# the 'def()' function's variable.

Programmer.full_name()

# screen output:    Joesph C. Richardson
'''----------------------------------------------------------------'''
# Let's create a for-loop that does the very same
#bjob as the above program example showed.

name='Joesph','C.','Richardson'

class Programmer:
    def full_name():
        for i in range(3):
            print(name[i],end=' ')

Programmer.full_name()

# screen output:    Joesph C. Richardson
'''----------------------------------------------------------------'''
# Let's create the very same for-loop, but instead
# of looping through a rage number, we will loop
# through the 'name' variable.

name='Joesph','C.','Richardson'

class Programmer:
    def full_name():
        for i in name:
            print(i,end=' ')

Programmer.full_name()

# screen output:    Joesph C. Richardson
'''----------------------------------------------------------------'''
# Let's create a single class that can call a return
# value through a 'def()' function.

return_name='Joesph','C.','Richardson'

class Programmer:
    def full_name():
        return return_name

print(Programmer.full_name()[0],end=' ')
print(Programmer.full_name()[1],end=' ')
print(Programmer.full_name()[2])

# screen output:    Joesph C. Richardson
'''----------------------------------------------------------------'''
# Let's create a for-loop that does the very same
# job as the above program example showed.

name='Joesph','C.','Richardson'

class Programmer:
    def full_name():
        return name

for i in range(3):
    print(Programmer.full_name()[i],end=' ')

# screen output:    Joesph C. Richardson
'''----------------------------------------------------------------'''
# Let's create a single class with two variables:
# 'name' and 'python' and return their values,
# one at a time in each of these two following
# program examples:

name='Joesph','C.','Richardson'
python='Programmer\'s','Glossary','Bible'

class Programmer:
    def full_name():
        return name

for i in range(3):
    print(Programmer.full_name()[i],end=' ')

# screen output:    Joesph C. Richardson
'''----------------------------------------------------------------'''
name='Joesph','C.','Richardson'
python='Programmer\'s','Glossary','Bible'

class Programmer:
    def full_name():
        return python

for i in range(3):
    print(Programmer.full_name()[i],end=' ')

# screen output:    Programmer's Glossary Bible
'''----------------------------------------------------------------'''
# Let's create a single class with a 'def()' function
# that calls itself, using the 'self' attribute. we
# can rename the attribute 'self' into whatever
# name we like, but 'self' is the Python standard
# programmers use. What 'self' does is acts like a
# 'return' statement, using the dunder method '__init__',
# which simply means to initialize the 'self' and
# whatever else inside the 'def()' function's parameters,
# such as the variable 'name'.

class Person:
  def __init__(self,name):
    self.name=name

print(Person('Joseph').name)
'''----------------------------------------------------------------'''
class Person:
  def __init__(self,first_name,middle_name,last_name):
    self.fname=first_name
    self.mname=middle_name
    self.lname=last_name

print(Person('Joseph','C.','Richardson').fname)

# or:

print(Person('Joseph','C.','Richardson').fname,Person('Joseph','C.','Richardson').mname,Person('Joseph','C.','Richardson').lname)

# Let's cut this monstrous line of bulky, ugly
# code down to size by using variables to
# completely mitigate this bulky, ugly code.
# For example:

person=Person('Joseph','C.','Richardson')

# Now this is more like it.

print(person.fname,person.mname,person.lname)

# If you want to completely overkill you can
# do this:

print(
  person.fname,
  person.mname,
  person.lname)

# Most of the time, you won't write code like this.
# That's why it's called 'overkill', because you are
# also adding extra lines of code by doing this,
# which defeats the purpose of shrinking code
# down to size. However, if you really want to
# overkill and reduce code lines. Do this:

overkill=person.fname,person.mname,person.lname

print(overkill[0],overkill[1],overkill[2])

# or:

for i in range(3):
  print(overkill[i],end=' ')
'''----------------------------------------------------------------'''
# Let's create a single class that returns a value
# of the 'def()' function called 'program' that returns
# the string 'Python'. The 'def()' function works
# the same way as before, but it's part of our class.
# The dunder '__init__' assure that the class can
# call its values, that are buried inside the 'def()'
# function. Dunders are called Methods. Remember
# the 'self' variable calls its own function, because
# of the dunder ' __init__'  method. Use two underscore
# lines on each side of the 'init' part of the dunder's
# main operation.

class Person:
  def __init__(self,name):
    self.name=name # the 'name' variable holds the value 'Joseph'

  def program():
    return 'Python'

call_variable=Person('Joseph')

print(call_variable.name,Person.program())

# screen output:    Joseph Python
'''----------------------------------------------------------------'''
# This program example below is the very same
# one as our above example. The only thing that's
# different, is the value 'Josesph' gets overridden
# with the value 'Computer Programming is so-
# -much FUN!'

class Person:
  def __init__(self,name):
    self.name='Computer Programming is so much FUN!' # string value

  def program():
    return 'Python'

call_variable=Person('Joseph') # the string value 'Joseph' is overridden

print(call_variable.name,Person.program())

# screen output:    Computer Programming is so much FUN! Python
'''----------------------------------------------------------------'''
# Let's learn how to create a single class with
# two return 'def()' fonctions inside it. Nothing
# much changes, we are just expanding our
# knowledge about classes.

class Person:
  def __init__(self,name):
    self.name=name # the 'name' variable holds the value 'Joseph'

  def program():
    return 'Python'

  def robot():
    return 'Robomaster S1'

call_variable=Person('Joseph')

print(call_variable.name,Person.program(),Person.robot())

# screen output:    Joseph Python Robomaster S1
'''----------------------------------------------------------------'''
# This program example below is the very same
# one as our above example. The only thing that's
# different, is the value 'Josesph' gets overridden
# with the value 'Robots are FUN!!'

class Person:
  def __init__(self,name):
    self.name='Robots are FUN!' # string value

  def program():
    return 'Python'

  def robot():
    return 'Robomaster S1'

call_variable=Person('Joseph') # the string value 'Joseph' is overridden

print(call_variable.name,Person.program(),Person.robot())

# screen output:    Robots are FUN! Python Robomaster S1
'''----------------------------------------------------------------'''
# Let's learn how to create a single class that
# inherits the properties from another class.
# This is called 'ClassInheritance'. Let's create
# one class called 'Mom' and one called 'Dad'.
# Andfinally, the 'Child' class, which is always
# the last class act. The 'Child' class is where
# all the inheritance magic happens. To make
# some inhertitance magic happen, we simply
# change the class variables from 'Mom.m' and
# 'Dad.d' into 'Child.m' and 'Child.d'. The 'Child'
# class can now be used to call both the 'Mom'
# and the 'Dad' class under one single, last class
# act. This program example below demonstrates
# the basic structure of 'class inheritance.

class Mom:
  mom='I called my Mom class'

print(Mom.mom) # 'I called my Mom class'

class Dad:
  dad='I called my Dad class'

print(Dad.dad) # 'I called my Dad class'

class Child(Mom,Dad): # the Child class inherits the properties of the 'Mom' class and the 'Dad' class
  pass

print(Mom.mom) # 'I called my Mom class'
print(Dad.dad) # 'I called my Dad class'

print(Child.mom) # 'I called my Mom class'
print(Child.dad) # 'I called my Dad class'
'''----------------------------------------------------------------'''
# We can create as many classes we like, but
# there is only one 'Child' class. For example:

class Mom:
  mom='I called my Mom class'

print(Mom.mom) # 'I called my Mom class'

class Dad:
  dad='I called my Dad class'

print(Dad.dad) # 'I called my Dad class'

class Son:
  son='I called my Son class'

print(Son.son) # 'I called my Son class'

class Daughter:
  daughter='I called my Daughter class'

print(Daughter.daughter) # 'I called my Daughter class'

class Child(Mom,Dad,Son,Daughter): # the Child class inherits the properties of the 'Mom' class and the 'Dad' class
  pass

print(Mom.mom) # 'I called my Mom class'
print(Dad.dad) # 'I called my Dad class'
print(Son.son) # 'I called my Son class'
print(Daughter.daughter) # 'I called my Daughter class'

print(Child.mom) # 'I called my Mom class'
print(Child.dad) # 'I called my Dad class'
print(Child.son) # 'I called my Son class'
print(Child.daughter) # 'I called my Daughter class'
'''----------------------------------------------------------------'''
# Let's do the very same class inheritance example
# below, but without the 'print()' function training
# wheels in it.

class Mom:
  mom='I called my Mom class'

class Dad:
  dad='I called my Dad class'

class Son:
  son='I called my Son class'

class Daughter:
  daughter='I called my Daughter class'

class Child(Mom,Dad,Son,Daughter):
  pass

print(Mom.mom) # 'I called my Mom class'
print(Dad.dad) # 'I called my Dad class'
print(Son.son) # 'I called my Son class'
print(Daughter.daughter) # 'I called my Daughter class'

print(Child.mom) # 'I called my Mom class'
print(Child.dad) # 'I called my Dad class'
print(Child.son) # 'I called my Son class'
print(Child.daughter) # 'I called my Daughter class'
'''----------------------------------------------------------------'''
# Let's create the very same class inheritance
# example once again, but this time we will create
# instances inside our class program example.
# We will use what we've learned so far so we
# can get a much betterunderstanding of Python
# classes in general. The only thing different is
# we are now adding an age variable to the mix.

class Mom:
  def __init__(self,name,age): # two arguments: name and age
    self.name=name
    self.age=age

class Dad:
  def __init__(self,name,age):
    self.name=name
    self.age=age

class Son:
  def __init__(self,name,age):
    self.name=name
    self.age=age

class Daughter:
  def __init__(self,name,age):
    self.name=name
    self.age=age

class Child(Mom,Dad,Son,Daughter):
  pass

print(Mom('Joan',35).name) # two argumant values: name and age
print(Mom('Joan',35).age)

print(Child('Joan',35).name) # two argumant values: name and age
print(Child('Joan',35).age)
'''----------------------------------------------------------------'''
# Although the above program example of class
# inheritance works, it has one problem and that
# problem is 'redundant code'. Programmers
# want to reuse code over and over again, not
# rewrite code over and over. So the solution is
# the 'super()' function, which holds temporary
# class attributes, like 'name' and 'age' values for
# example. Let's try using the 'super()' function
# and see what happens to our previous program
# data structure.

class Main_class:
  def __init__(self,name,age): # two arguments: name and age
    self.name=name
    self.age=age

class Sub_class1(Main_class):
  def __init__(self,name,age):
    super().__init__ (name,age)

class Sub_class2(Main_class):
  def __init__(self,name,age):
    super().__init__ (name,age)

class Sub_class3(Main_class):
  def __init__(self,name,age):
    super().__init__ (name,age)

class Sub_class4(Main_class):
  def __init__(self,name,age):
    super().__init__ (name,age)

# As we can clearly see how the 'super()' function
# drastically reduced our program code and it
# allowed us to access values from the other sub
# classes. It's as if we did what we did before, but
# we didn't need all those redundant code blocks
# like we had before.

print(Main_class('Joan',40).name)
print(Main_class('Mary',35).name)
print(Main_class('George',42).name)
print(Main_class('Sam',60).name)

print(Sub_class1('Joan',40).age)
print(Sub_class2('Mary',35).age)
print(Sub_class3('George',42).age)
print(Sub_class4('Sam',60).age)
'''----------------------------------------------------------------'''
# Let's take a break and try some other neat stuff
# with single classes only. Let's create a few functions
# inside it, so we can get a much better understanding
# of why classes can hold multiple objects or instances.
# For example:

class My_functions:
  def function1():
    print("I'm Function One:")
  def function2():
    print("I'm Function Two:")
  def function3():
    print("I'm Function Three:")

My_functions.function1() # class name.value
My_functions.function2() # class name.value
My_functions.function3() # class name.value
'''----------------------------------------------------------------'''
# Let's play hooky and go back to creating a simple
# function without being inside a classroom. Get it?
# Class-room. Here are two program examples
# that will return different values.

def function1(words):
  return 'I love my funtions.' # returns a string value

returned_value=function1('Returned arguments go here.') # function('argument')

print(returned_value) # outputs the returned value

# This program example below is the same exact
# one as the above program example. The only
# difference between the two is how they return
# values from the 'def()' function.

def function1(words):
  return words # words variable overrides 'I love my funtions.' with 'Returned arguments go here.'

returned_value=function1('Returned arguments go here.') # function('argument')

print(returned_value) # outputs the returned value
'''----------------------------------------------------------------'''
# Let's create a class with two return functions
# inside it that will return two different values.

class My_functions:
  def function1(words):
    return 'I love my funtions.' # returns a string value
  
  def function2(words):
    return words # words variable overrides 'I love my funtions.' with 'Returned arguments go here.'

returned_value1=My_functions.function1('Returned arguments go here.') # function('argument')
returned_value2=My_functions.function2('Returned arguments go here.') # function('argument')

print(returned_value1) # outputs the returned value
print(returned_value2) # outputs the returned value

# Not only did we play hooky from classes, but
# we also learned a whole lot about classes and
# how they work. We can create classes to cause
# different instances to occur inside them, just
# like our example above illustrated. Classes are
# great at storing multiple 'def()' functions inside
# them, which drastically reduces redundant code
# on the programmer's part. Remember, we want
# to reuse code over and over again, not rewrite
# it over and over. However, we don't always have
# to create classes. And to be honest, I hardly
# ever use them, unless I know I'm going to possibly
# write redundant code, or I want to group 'def()'
# functions together, like killing lots of birds with
# only a single stone's throw. Classes and functions
# are very powerful and versatile
'''----------------------------------------------------------------'''
# These two class program examples are identicle
# and just as before, all we did was plug the variable
# 'age' inside the second class program example.

# Class program example 1:

class Person:
  def __init__(self, name, age):
    self.name=name
    self.age='Not telling my age.' # string value

  def myfunc(self):
    print("Hello my name is",self.name,str(self.age))

p=Person("Joseph",57) # two arguments:

p.myfunc() # call 'myfunc()'

# Class program example 2:

class Person:
  def __init__(self, name, age):
    self.name=name
    self.age=age # variable value

  def myfunc(self):
    print("Hello my name is",self.name,str(self.age))

p=Person("Joseph",57) # two arguments:

p.myfunc() # call 'myfunc()'
'''----------------------------------------------------------------'''
# Now you know what classes are and how they
# work. However, you must practice, practice
# practice Python each and every single day.

# Object Oriented Programming is a lot different than the type of programming I used to
# know, which was 'BASIC' (Beginner's All-purpose Symbolic Instruction Code. I was also
# into advanced BASIC and 6502 Assembler Language on a Commodore  128 computer
# system from the mid 1980's.However, Object Oriented Programming of any kind is still
# very new to me; I'm only in my fourth, straight year of learning all about Object Oriented
# Programming with Python this Christmas day coming, when I started my trek into Stem
# Robotics and I'm completely hooked. I've started Python programming since Christmas
# day, 2017 and I have learned and relearned how to do programming all over again. Like
# going full circle. I started off as a self taught computer programmer, then quit for a lot of
# years, but in that time, I created my own website that used to be called SPACEUPHORIA.com.
# This website is no longer around, but I did put ten years into created it and programming
# it. Just after it closed in 2018, I was already back into computer programming, so I didn't
# mind losing the website, and I didn't have anything to offer on it, but science concepts and
# aliens. lol Lots of aliens and UFO's; my own works at that.

# But in the end, I find that I completely went back to full circle into computer programming,
# which was how I got into computers in the first place. Thirty-five years later, I'm at it again
# much stronger than I was before. Because in the end, programming for me is truly where
# it's at....
