# This program says hellos and asks for my name.

print('Hello, world!')
name = input('What is your name? ')
print('It is good to meet you', name)

print('The length of your name is: ', len(name))

# Ask for their age
age = int(input('What is your age? ').strip())
print('You will be ', age + 1, ' in 1 year')