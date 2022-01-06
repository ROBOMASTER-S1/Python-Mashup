c=186000
energy='"mc2" is awesome! '

def return_math_result(first_name,last_name,mc2,expon=2):
    return first_name+last_name+energy+str(mc2**expon)

get_math_result=return_math_result('Albert ',"Einstein's ",c)

albert_einstein=get_math_result+' is double the speed of light.'

print(albert_einstein)
