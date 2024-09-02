skill_completed="Python Syntax"
exercises_completed=13
points_per_exercise=5
point_total=100
point_total+=exercises_completed*points_per_exercise
#The amount of points for each exercise may change, because points don't exist yet
print "i got",point_total,"points"

# Set the variable brian on line 3!
brian = "Hello life!"

# Assign your variables below, each on its own line!
caesar="Graham"
praline="John"
viking="Teresa"
# Put your variables above this line

print caesar
print praline
print viking
# The string below is broken. Fix it using the escape backslash!

'This isn\'t flying, this is falling with style!'
#On line 13, assign the variable fifth_letter equal to the fifth letter of the string “MONTY”.

fifth_letter ="MONTY"[4]

print fifth_letter
#On line 1, create a variable named parrot and set it to the string "Norwegian Blue"
parrot="Norwegian Blue"
print len(parrot)

#You can use the lower() method to get rid of all the capitalization in your strings. You call lower() like so:
parrot = "Norwegian Blue"

print parrot.lower()

#Call upper() on parrot (after print on line 3) in order to capitalize all the characters in the string!
parrot = "norwegian blue"

print parrot.upper()

"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14
print  str(pi)

#On line 3, call the len() function with the argument ministry.On line 4, invoke the ministry‘s .upper() function.
ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes="Ping!"
print the_machine_goes

# Print the concatenation of "Spam and eggs" on line 3!
print "Spam "+"and "+"eggs"
# Turn 3.14 into a string on line 3!

print "The value of pi is around " + str(3.14)
#Take a look at the code in the editor. What do you think it’ll do? Click Run when you think you know.
string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

#You need the same number of %s terms in a string as the number of variables in parentheses:
name = "Alex"
quest = "Teaching Python"
color = "Blue"

print "Ah, so your name is %s, your quest is %s, " 
"and your favorite color is %s." % (name, quest, color)
# Write your code below, starting on line 3!

my_string="heman"
print len(my_string)
print my_string.upper()
#final task
meal=44.50
tax=6.75/100
tip=15.0/100
meal=meal+meal*tax
total=meal+meal*tip
print total
#datetime library
from datetime import datetime
now=datetime.now()
print now

#print the year,date,time
from datetime import datetime
now=datetime.now()
print now.year
print now.month
print now.day
#method2
from datetime import datetime
now = datetime.now()
print "%02d/%02d/0%4d" % (now.month,now.day,now.year)

#hour,time,second
from datetime import datetime
now = datetime.now()

print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

#print both date and time together
from datetime import datetime
now = datetime.now()

print "%02d/%02d/%04d %2d:%02d:%02d" % (now.month,now.day,now.year,now.hour,now.minute,now.second)
#conditional and control flow
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False

# Assign True or False as appropriate on the lines below!

# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = False

# 1**2 <= -1
bool_three = False

# 40 * 4 >= -4
bool_four = True

# 100 != 10**2
bool_five = False

# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 4 > 5

# Make me true!
bool_three = 2==2

# Make me false!
bool_four = 5!=5

# Make me true!
bool_five = 6>=5

bool_one = False and False

bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5

bool_three = 19 % 4 != 300 / 10 / 10 and False

bool_four = -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2

bool_five = True and True

#boolean operator or
bool_one = 2 ** 3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or False

bool_three = 100 ** 0.5 >= 50 or False

bool_four = True or True

bool_five = 1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1

#boolean operator not
bool_one = not True

bool_two = not 3 ** 4 < 4 ** 3

bool_three = not 10 % 3 <= 10 % 2

bool_four = not 3 ** 2 + 4 ** 2 != 5 ** 2

bool_five = not not False

bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)

# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = (5==5) or (5>6)

# Make me false!
bool_three = (6>7) and (5!=5)

# Make me true!
bool_four = not (4>5)

# Make me true!
bool_five = (5>4) or (6==6)

response = "Y"

answer = "Left"
if answer == "Left":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    
# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.
def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print using_control_once()
print using_control_again()
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return  False    # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False     # Make sure this returns False
    
    #elif
    def greater_less_equal_5(answer):
    if answer>5:
        return 1
    elif answer<5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

# Complete the if and elif statements!
def grade_converter(grade):
    if grade>=90:
        return "A"
    elif grade>=80 and grade<=89:
        return "B"
    elif grade>=70 and grade<=79:
        return "C"
    elif grade>=65 and grade<=69:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print grade_converter(92)

# This should print a "C"
print grade_converter(70)

# This should print an "F"
print grade_converter(61)

#if else
e_string="heman"
if len(e_string):
  print e_string
else:
  print "embty"
# to check the sring only contains characters
e_string="heman"
if len(e_string) and e_string.isalpha():
  print e_string
else:
  print "embty"

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word=original.lower()
  first=original[0]
  print original
else:
  print 'empty'  
  
pyg = 'ay'
original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
  word=original.lower()
  first=original[0]
  new_word=word+first+pyg
  print original
else:
  print 'empty'
  
pyg = 'ay'
original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
  word=original.lower()
  first=original[0]
  new_word=word+first+pyg
  new_word= new_word[1:len(new_word)]
  print original
else:
  print 'empty'
def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print "With tax: %f" % bill
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print "With tip: %f" % bill
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)  
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared
  
# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.

square(10)

def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!

#First, def a function called cube that takes an argument called number. Don’t forget the parentheses and the colon!
def cube(number):
  return number * number * number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False
 Ask Python to print sqrt(25) on line 3.
import math
print math.sqrt(25)

# Import *everything* from the math module on line 3!

from math import *






