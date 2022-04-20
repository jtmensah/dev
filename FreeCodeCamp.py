
'''
#List functions
friends = ["Kevin", "Karen", "Jim"]
lucky_numbers = [34, 24, 64, 65, 56, 7, 8]
lucky_numbers2 = lucky_numbers.copy()
lucky_numbers2.sort()       #sorts list in asc order
randos = [True, 34.5, "Hello"]
randos.reverse()        #reverses list (reverse of sort - desc order)
friends.append("Ama")       #adds new input to end of list
lucky_numbers.insert(3, 11)     #inserts 2nd arg into 1st arg's index
friends.insert(0, "Mary")
lucky_numbers.extend(friends)       #appends friends list to lucky_numbers list
randos.clear()      #clears list
randos.append("This replaces list")
lucky_numbers.pop()     #removes last item from list

print(friends)
print(lucky_numbers)
print(randos)
print(lucky_numbers.index(11))      #finds position/index of arg in list
print(friends.count("Jim"))     #counts how many times "Jim" appears in friends list
print(lucky_numbers2)     #sort in asc order
'''

'''
def calculator():
    x = ["+", "-", "*", "/"]
    i = input("Please input desired operation (Add - a, Subtract - s, Multiply - m, Divide - d): ")
    y = float(input("Please enter a number: "))
    z = float(input("Please enter another number: "))

    if i == "a":
        return y+z
    elif i == "s":
        return y-z
    elif i == "m":
        return y*z
    elif i == "d":
        return y/z
    else:
        return "Please enter a valid operator (a, s, m, d)"

print(calculator())
'''

'''
monthconv = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March"
}

print(monthconv["Feb"])
print(monthconv.get("Jan"))     #get function can have a 2nd arg as a default response when key doesnt exist
'''

'''
i = 0

while i <= 20:
    print(i)
    i += 2

print("While loop completed")
'''

'''
import random
from words import word

random_word = random.choice(word).upper()
print(random_word)
tries = 4

while tries >= 0:
    user_guess = input(f"Enter your guess: ").upper()
    if user_guess != random_word:
        print(f"Wrong guess, you have {tries} attempts remaining.")
        tries -= 1
    else:
        print(f"Yay! You've guessed the correct word {random_word}")
        break
print("Game over")

'''

'''
def exponent(base_num, power_num):
    result = 1
    for i in range(power_num):
        result *= base_num
    return result

print(exponent(2, 3))
'''

'''
list_2d = [
    [1, 3, 6],
    [5, 2, 0],
    [8, 1, 4],
    [45]
]

for row in list_2d:
    for col in row:
        print(col)
'''

'''
vowels = "aeiou"

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in vowels:
            translation += "J"
        else:
            translation += letter
    return translation

print(translate(input("Please enter a phrase for translation: ")))
'''

'''
try:
    #answer = 10/0
    number = int(input("Please enter a number: "))
    print(number)

except ZeroDivisionError as Error:
    print(Error)

except ValueError as Error2:
    print(Error2)
'''

'''
#r+ arg in open function is read and write, a is append, and x id create
employee_file = open(r"C:\Users\agya_\Documents\AWS\LearnToCloud\Python\employees.txt", "r")

#employee_file.write("Kwasi - HR\n"
#                    "Osei - Accounts")
#employee_file.write("\nKwasi - HR")

#for employee in employee_file:
#    print(employee)

#print(employee_file.readable())
print(employee_file.read())
#print(employee_file.readlines())
#print(employee_file.readlines()[2])

employee_file.close()
'''
