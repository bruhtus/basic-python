def shout(word='yes'):
    return word.capitalize() + '!'

print(f'shuot function: {shout()}')

scream = shout #as an object you can assign the function to a variable like any other object

#notice that we don't use parentheses? we are not calling the function,
#we're putting the function 'shout' into the variable 'scream'.
#it means you can call 'shout' from 'scream'.

print(f'scream function: {scream()}')

#more than that, you can remove the old name 'shout',
#and the function still accessible from 'scream'.

del shout

try:
    print(f'shout function: {shout()}')
except NameError as e:
    print(e)

print(f'scream function: {scream()}')
