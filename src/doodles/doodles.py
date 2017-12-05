# as always, Hello World
print("Hello World")

print()
content1='What\'s your name?'
content2="What's your name?"
print(content1)
print(content2)

# raw string
print()
str_raw=r'hi\there\nyou\n\tare'
str_plain='hi\there\nyou\n\tare'
print(str_raw)
print(str_plain)

print()
str_multiline='''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
print(str_multiline)

print()
str_span_multi_line="This is the first sentence. \
This is the second sentence."
print(str_span_multi_line)

print()
num1 = 52.3E-4
age=20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
# note that the numbers are optional, so it can  be written as 
print('{} was {} years old when he wrote this book'.format(name, age))
print(name+' is ' + str(age) + ' years old')
print('{:.7f}'.format(num1))
# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print()
# Output is:
# ab c
print('a', end='')
print('b', end=' ')
print('c')

# line ending
i = 5
print(i)
i = 5;
print(i);
i = 5;print(i)