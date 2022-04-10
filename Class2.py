'''
# Functions
def GrossPay(hours, ratePerHour):
    grossPay = hours * ratePerHour
    print("Hourly Wage: ", grossPay)

def OverTimePay(hours, ratePerHour):
    newhours = hours - 40
    grossPay = 40 * ratePerHour
    overtime = newhours * (ratePerHour*1.5)
    print("Hourly Wage more than 40 hours: ", grossPay + overtime)

try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate per Hour: "))

    if hrs > 40:
        OverTimePay(hrs, rate)
    else:
        grossPay()

except e:
    print("Please enter only Numbers.")
'''



'''
# While loop
table = int(input("Table of: "))
n = 1
while n <= 10:
    print(f"{table} x {n} = {table*n}")
    n += 1
'''




'''
# break statement
myList = []
while True:
    try:
        userInput = int(input("Enter items into the list: "))
        myList.append(userInput)
        choice = input("Press 'N' to Exit.\n")
        choice = choice.lower()
        if choice == 'n':
            break
    except:
        print("Please enter a legal character.")
count = 0
mysum = 0
for i in myList:
    mysum += i
    average = mysum / len(myList)
    count += 1

print("List: ", myList)
print("Sum: ", mysum)
print("Average: ", average)
print("Count: ", count)

'''



'''
# Find out Even Numbers
for i in range(1, 101):
    if i % 2 != 0:
        continue
    else:
        print(i)
'''



'''
# find out min from the List
smallest = None
myList = [23, 32, 65, 120, 12]
print("List: ", myList)
for i in myList:
    if smallest is None or i < smallest:
        smallest = i
    print("Loop: ", i)
    print("Smallest Number: ", smallest)
'''



'''
# Strings
firstName = "Twinkle Twinkle "
lastName = 'Little Stars'
# print(firstName + lastName)

# String Slicing
newstr = firstName[:4]  # -> This will return characters starting from index 0 to index 3.
print(newstr)
'''


'''
# String Comparison
word = "Pinnapple"

if word < "Banana":
    print("Banana is less than", word)
elif word > "Banana":
    print("Banana is greater than", word)
else:
    print("All right Bananas")
'''


'''
# Activity
def employees(email, old_domain, new_domain):
    if old_domain in email:
        email = email.replace(old_domain, new_domain)

    return email
try:
    email = input("Enter Email: ")
    email = email.lower()
    old_domain = email.split("@")
    old_domain = old_domain[1]
    new_domain = "corvit.com"

    new_email = employees(email, old_domain, new_domain)
    print("New Domain:", new_email)
except:
    print("Incorrect email or domain, Please try again.")
'''


'''
# File Handling
#   - Read File
f  = open("file1.txt")
readFile = f.read()
print(readFile)
print(type(readFile))
'''
