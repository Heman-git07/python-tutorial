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

print "Ah, so your name is %s, your quest is %s, " \
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







