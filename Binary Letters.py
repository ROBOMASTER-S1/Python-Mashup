import time

knowledge=(
"'Knowledge'\
is a free invention of the heart and of the mind itself!\
The only textbooks needed are the heart and the mind.\
The only exam to be written is the key to ponder into wonder.\
For the heart and the mind hold the key to the greatest diploma of all,\
the dream's creation of our imagination.\
For the heart and the mind are thus, the greatest teachers of us...\
Believe in yourself! For you are their greatest student.")

letters=list(knowledge)
for i in range(len(knowledge)):
    print(bin(ord(letters[i])),'=',
    oct(ord(knowledge[i])),'=',
    hex(ord(knowledge[i])).upper(),'=',
    ord(knowledge[i]),'=',knowledge[i])
