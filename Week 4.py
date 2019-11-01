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
#1 center        aStr.center(w)-center the string within specified width  with optionalfill characters
#2 ljust         aStr.ljust(w)-left justify the string in the provided width with optiona fill characters
#3 rjust         aStr.rjust(w)-right justifies the string in the provided width
#4 upper         aStr.upper()-returns uppercased strings
#5 lower         aStr.lower()-returns lowercase strings
#6 index         aStr.index(item)-returns the substring index
#7 rindex        aStr.rindex(item)-return substrings highest index
#8 find          aStr.find(item)-returns substrings first occuring index
#9 rfind         aStr.rfind(item)-returns subsrtings highest index
#10 replace       aStr.replace(old, new)- Replaces substring

# Be sure to include multiple examples of all of them in use

#1 for i in range(hen(chicken)
    str="Orange Chicken"
    firstChar = str[0]
    print(str.center(i))



#Character Function

print(ord('8'))
print(chr(98-14))


star = "pizza"
print(star.rjust(4))

print(star.rjust(8))

star = "ree"
print(star.upper())

print(star.upper())

star = "BLAH"
print(star.lower())

print(star.lower())


#Character Functions

print(ord('B'))
print(chr(98-14))


#Testing Functions From Mapper.py
from mapper import *
print(letterToIndex('a'))

from mapper import *
print(letterToIndex('A'))

from mapper import *
print(indexToLetter(10))



from Crypto import *

print(scramble2Encrypt("Poker Face, Ppppp, poker face"))
print(scramble2Decrypt("oe ae pp,pkrfcPkrFc,Ppp oe ae"))





#Character Functions

print(ord('5'))

print(chr(104))

print(chr(97+13))

print(str(12572))


#Write a strip space function here

def StripSpace(text):
    return text.replace("","")

print(StripSpace("Happy Birthday"))


#write a stripeSpaces(text) function here

#write a caesarEncrypt(plaintext, shift)
#write a caesarDecrypt(cipherText, shift)


#encrypt and decrypt a text using a simple algorithm of offsetting the letters

key = "abcdefghijklmnopqrstuvwxyz"

def encrypt(n,plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ""

    for i in plaintext.lower():
        try:
            result=(key.index(1)+n) % 26
            result += key[i]
        except ValueError:
             result +=1

    return result.lower()
def decrypt(n,ciphertext):
    """Decrypt rhw string and return the plaintext"""
    result = ''

    for i in ciphertext:
      try:
          i = (key.index(1) - n) % 26
          result += key[i]
      except ValueError:
            result += 1

    return result

text = "I am coding Python on SoloLearn"
offset = 5

encrypt = encrypt(offset, text)
print('Encrypt:', encrypt)

decrypt = decrypt(offset,encrypt)
print('decrypt', decrypt)



















