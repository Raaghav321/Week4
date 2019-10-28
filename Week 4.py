# Strings
#    data that falls within " " marks

# Concatenation
#  Put 2 or more strings together

firstName = "Fred"
lastName = "Flintstone"

fullName = firstName + " " + lastName

print(fullName)

# Repetition
#  repetition operator: *

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + 'your boat')
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowYourBoat()

#Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])

print(name[-1])

for i in range(len(name)):
    print(name[i])

#Slicing and Dicing
#   slicing operator:
#   slicing lets us make substrings

print(name[0:3])
print(name[:5])
print(name[6:9])
print(name[6:])

for i in range(1, len(name)):
    print(name[0:i])

# Searching inside of Strings

print("Biv" in name)
print("v" not in name)

if "y" in name:
    print("the letter y is in name")
else:
    print("the letter why is not in name")

def littlelamb():
    print("mary had a little""2")
    print("it was white as snow")
    print("everywhere""3")
    print("mary went")

#  Your Task:
#  Modify the simulation to plot points in the entire circle.  You will have to
#    adjust the calculated value of pi accordingly.

# String Methods to investigate:
# Method        Use Example         Explanation
#1 center        aStr.center(w)-
#2 ljust         aStr.ljust(w)
#3 rjust         aStr.rjust(w)
#4 upper         aStr.upper()
#5 lower         aStr.lower()
#6 index         aStr.index(item)
#7 rindex        aStr.rindex(item)
#8 find          aStr.find(item)
#9 rfind         aStr.rfind(item)
#10 replace       aStr.replace(old, new)

# Be sure to include multiple examples of all of them in use

#Character Functions

print(ord('B'))

print(chr(104))

print(chr(97+13))

print(str(12548))



