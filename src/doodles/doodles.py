# as always, Hello World
print("Hello World")
print()

print('################### demo for fundamantal stuffs')

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

print('################### demo for control flow')

number = 23

## how to collect input
# guess = int(input('Enter an integer : '))
guess = 23
if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here
    print('Done')
    # This last statement is always executed,
    # after the if statement is executed.

while guess >= number - 1:
    print("loop again")
    guess -= 1
else:
    print("loop over")

for i in range(1, 5):
    print(i)
else:
    print("for loop is over")

print('################### demo for function')

def sayHello() :
    print("hello world")

sayHello()

def findMax(a, b):
    if a >= b :
        return a
    else:
        return b
print(findMax(3,5))

x=10

def globalTest():
    global x
    print("x is {}".format(x))
    x=20

globalTest()
print("now x is {}".format(x))

def say(message, times=1):
    print(message * times)
say('Hello')
say('World', 5)

def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c=24)
func(c=50, a=100)

print('###VarArgs')
def total(a=5, *numbers, **phonebook):
    print('a', a)
    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)
    #iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
print_max(3, 5)
# same as help(print_max)
print(print_max.__doc__)

print("################### demo for list")
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')
print()
print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)
print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

print("################### demo for tuple")
# I would recommend always using parentheses
# to indicate start and end of tuple
# even though parentheses are optional.
# Explicit is better than implicit.
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
new_zoo = 'monkey', 'camel', zoo # parentheses not required but are a good idea
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
        len(new_zoo)-1+len(new_zoo[2]))

# Tuple with 0 or 1 items
myempty = ()
singleton = (2 , )

print('################### demo for dictionary')
# 'ab' is short for 'a'ddress'b'ook
ab = {
'Swaroop': 'swaroop@swaroopch.com',
'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
print("Swaroop's address is", ab['Swaroop'])

# Deleting a key-value pair
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

print("################## demo for sequence")
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
# Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])           ## banana
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])              ## ['mango', 'carrot']
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# slicing with step
teststr = "abcdefg"
print(teststr[2:5:2])     ## ce
print(teststr[::-1])        ## gfedcba

print("################# demo for set")
bri = set(['brazil', 'russia', 'india'])
print('brazil' in bri)                             ## True
print('brazil' not in bri)                      ## False
bric = bri.copy()                                  
bric.add('china')                                
print(bric.issuperset(bri))                 ## True
bri.remove('russia')

print(bri & bric)                               ## {'brazil', 'india'}
bri.intersection(bric)                       ## {'brazil', 'india'}                     

print("################# demo for string")
# This is a string object
name = 'Swaroop'
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
if 'a' in name:
    print('Yes, it contains the string "a"')
if name.find('war') != -1:
    print('Yes, it contains the string "war"')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

print("################# demo to do system call")
import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
# source = ['"C:\\My Documents"']
# Example on Mac OS X and Linux:
source = ['/Users/swa/notes']
# Notice we have to use double quotes inside a string
# for names with spaces in it. We could have also used
# a raw string by writing [r'C:\My Documents'].

target_dir = '/Users/swa/backup'

# notice, the backslash \ is mandatory, otherwise, there is compile error
target = target_dir + os.sep + \
            time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    # os.mkdir(target_dir) # make directory
    print("making directory")

zip_command = 'zip -r {0} {1}'.format(target,
            ' '.join(source))

# if os.system(zip_command) == 0:
#    print('Successful backup to', target)
# else:
#    print('Backup FAILED')

print('################ demo for oo')

class  Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
print(p)            ## <__main__.Person instance at 0x10171f518>

p.say_hi()

class Robot:
        """Represents a robot, with a name."""
        # A class variable, counting the number of robots
        population = 0
        def __init__(self, name):
                """Initializes the data."""
                self.name = name
                print("(Initializing {})".format(self.name))
                Robot.population += 1

        def say_hi(self):
                """Greeting by the robot.

                Yeah, they can do that."""
                print("Greetings, my masters call me {}.".format(self.name))

        @classmethod
        def how_many(cls):
                """Prints the current population."""
                print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
# class method can be invoked by objects
droid2.how_many()

# following  statements  do nothing, methods are not invoked
# they are typos obviously, lack of parenthesis, but surprisingly there were no errors
droid1.say_hi
Robot.how_many

class SchoolMember:
        '''Represents any school member.'''
        def __init__(self, name, age):
                self.name = name
                self.age = age
                print('(Initialized SchoolMember: {})'.format(self.name))
        def tell(self):
                '''Tell my details.'''
                print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")
class Teacher(SchoolMember):
        '''Represents a teacher.'''
        def __init__(self, name, age, salary):
                SchoolMember.__init__(self, name, age)
                self.salary = salary
                print('(Initialized Teacher: {})'.format(self.name))
        def tell(self):
                SchoolMember.tell(self)
                print('Salary: "{:d}"'.format(self.salary))

t = Teacher('Mrs. Shrividya', 40, 30000)
t.tell()

print("###############  demo for input and output")

# something = input("Enter text: ")

# print(reverse(something))

poem = '''
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''
# Open for 'w'riting
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()
# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('poem.txt')
while True:
        line = f.readline()
        # Zero length indicates EOF
        if len(line) == 0:
            break
        # The `line` already has a newline
        # at the end of each line
        # since it is reading from a file.
        print(line, end='')
# close the file
f.close()

print("############### demo for pickle")

import pickle
# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']
# Write to the file
f = open(shoplistfile, 'wb')
# Dump the object to a file
pickle.dump(shoplist, f)
f.close()
# Destroy the shoplist variable
del shoplist
# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)

# encoding=utf-8
import io
f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text)

print("################ demo for exception handle")  

class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    #text = input('Enter something --> ')
    text = "ah"
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:                     # Press ctrl + d
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:       # Press ctrl + c
    print('You cancelled the operation.')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
                    '{0} long, expected at least {1}')
                    .format(ex.length, ex.atleast))
else:                                           # if no exception, this is executed
    print('You entered {}'.format(text))
finally:
    print('do some clearup in finally')

f = None
try:
    f = open("poem1.txt")
except FileNotFoundError:
    print("file doesn't exists")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")

with open("poem.txt") as f:
    for line in f:
        print(line, end='')

print("################# demo for standard library")

import os
import platform
import logging
if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                                os.getenv('HOMEPATH'),
                                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                            'test.log')
print("Logging to", logging_file)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")


print("################# demo for more tricks")

print("return tuple")
def get_error_details():
    return (2, 'details')

errnum, errstr = get_error_details()

a = 5; b = 8
a, b = b, a

print("single statement block")
flag = True
if flag: print('Yes')

print("### demo for lambda forms")
points = [{'x': 2, 'y': 3},
                    {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)                   # [{'x': 4, 'y': 1}, {'x': 2, 'y': 3}]

listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)

print("list comprehansion")
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)                      # [6, 8]


def powersum(power, *args):
    '''Return the sum of each argument raised to the specified power.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total

print(powersum(2, 3, 6))


mylist = ['item']
assert len(mylist) >= 1

print("#################### demo for decorator")
from time import sleep
from functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger("retry")
def retry(f):
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception("Attempt %s/%s failed : %s",
                                            attempt,
                                            MAX_ATTEMPTS,
                                            (args, kwargs))
            sleep(1 * attempt)
        log.critical("All %s attempts failed : %s",
                                MAX_ATTEMPTS,
                                (args, kwargs))
    return wrapper_function
counter = 0

@retry
def save_to_database(arg):
    print("Write to a database or make a network call or etc.")
    print("This will be automatically retried if exception is thrown.")
    global counter
    counter += 1
    # This will throw an exception in the first call
    # And will work fine in the second call (i.e. a retry)
    if counter < 2:
        raise ValueError(arg)
    print("save is done")
if __name__ == '__main__':
    save_to_database("Some bad value")