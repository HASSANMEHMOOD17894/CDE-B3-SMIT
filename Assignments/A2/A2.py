# A2.py
#Assignments A2

#1. A company decided to give bonus of 5% to employee if his/her year
# of service is more than 5 years. Ask user for their salary and year
# of service and print the net bonus amount.

bonus_percentage = 0.05
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))
if years_of_service > 5:
    bonus = salary * bonus_percentage
    print("You are eligible for a bonus of: {:.2f}".format(bonus))
else:
    print("You are not eligible for a bonus.")
    
    
# 2.Write a program to check whether a person is eligible for voting or not.
# (accept age from user) if age is greater than 17 eligible otherwise not eligible    

age = int(input("Enter your age: "))
if age > 17:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")
    
    
# 3.Write a program to check whether a number entered by user is even or odd.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
        
        
# 4.Write a program to check whether a number is divisible by 7 or not. Show Answer

number = int(input("Enter a number: "))
if number % 7 == 0:
    print("The number is divisible by 7.")
else:
    print("The number is not divisible by 7.")
           
           
# 5.Write a program to display "Hello" if a number entered by user
# is a multiple of five , otherwise print "Bye".            

number = int(input("Enter a number: "))
if number % 5 == 0:
    print("Hello")
else:
    print("Bye")
    

# 6.Write a program to calculate the electricity bill (accept number of unit from user) 
# according to the following criteria : Unit Price
#uptp 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per
# unit (For example if input unit is 350 than total bill amount is Rs.3500 
# (For example if input unit is 97 than total bill amount is Rs.0 
# (For example if input unit is 150 than total bill amount is Rs.750    

units = int(input("Enter the number of units consumed: "))
if units <= 100:
    bill_amount = 0
elif units <= 300:
    bill_amount = (units - 100) * 5
else:
    bill_amount = (200 * 5) + (units - 300) * 10
print("Total bill amount: Rs.{:.2f}".format(bill_amount))

    
    
# 7.Write a program to display the last digit of a number.
number = int(input("Enter a number: "))
last_digit = number % 10
print("The last digit of the number is:", last_digit)


# 8.Take values of length and breadth of a rectangle from user
# and print if it is square or rectangle.    

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
if length == breadth:
    print("The rectangle is a square.")
else:
    print("The rectangle is not a square.")
    
    
# 9.Take two int values from user and print greatest among them.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print("The greatest number is:", num1)
else:
    print("The greatest number is:", num2)
    
    
# 10.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost 
# for user.

quantity = int(input("Enter the quantity purchased: "))
unit_price = 100
total_cost = quantity * unit_price
if total_cost > 1000:
    discount = total_cost * 0.10
    total_cost -= discount
    print("You received a discount of {:.2f}".format(discount))
print("Total cost after discount: {:.2f}".format(total_cost))

# 11.A school has following rules for grading system:
#a. Below 25 - F

#b. 25 to 45 - E

#c. 45 to 50 - D

#d. 50 to 60 - C

#e. 60 to 80 - B

#f. Above 80 - A

#Ask user to enter marks and print the corresponding grade.

marks = float(input("Enter your marks: "))
if marks < 25:
    grade = 'F'
elif 25 <= marks < 45:
    grade = 'E'
elif 45 <= marks < 50:
    grade = 'D'
elif 50 <= marks < 60:
    grade = 'C'
elif 60 <= marks < 80:
    grade = 'B'
else:
    grade = 'A'
print("Your grade is:", grade)


# 13.Take input of age of 3 people by user and determine oldest and youngest among them.
age1 = int(input("Enter the age of the first person: "))
age2 = int(input("Enter the age of the second person: "))
age3 = int(input("Enter the age of the third person: "))
ages = [age1, age2, age3]
oldest = max(ages)
youngest = min(ages)
print("The oldest person is:", oldest)
print("The youngest person is:", youngest)



#  14.A student will not be allowed to sit in exam if his/her attendence is less than 75%.

#Take following input from user

#Number of classes held

#Number of classes attended.

#And print

#percentage of class attended

#Is student is allowed to sit in exam or not.

classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))
attendance_percentage = (classes_attended / classes_held) * 100
print("Attendance percentage: {:.2f}%".format(attendance_percentage))
if attendance_percentage < 75:
    print("You are not allowed to sit in the exam.")
else:
    print("You are allowed to sit in the exam.")
    
    
# 15.Modify the above question to allow student to sit if he/she has medical cause. 
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly. 

if attendance_percentage < 75:
    medical_cause = input("Do you have a medical cause? (Y/N): ")
    if medical_cause.upper() == 'Y':
        print("You are allowed to sit in the exam due to medical cause.")
    else:
        print("You are not allowed to sit in the exam.")
    print("You are allowed to sit in the exam.")
else:
    print("You are allowed to sit in the exam.")
    
# 16.Write a program to check if a year is leap year or not.
#If a year is divisible by 4 then it is leap year but if the year is century year
# like 2000, 1900, 2100 then it must be divisible by 400.   

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("{} is a leap year.".format(year))
else:
    print("{} is not a leap year.".format(year))
    
    
# 17.Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then 
# using following rules print their place of service.
#if employee is female, then she will work only in urban areas.

#if employee is a male and age is in between 20 to 40 then he may work in anywhere

#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

#And any other input of age should print "ERROR"    

age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
marital_status = input("Enter your marital status (Y/N): ")
if(gender.upper() == 'M'):
    if 20 <= age <= 40:
        place_of_service = "anywhere"
    elif 40 < age <= 60:
        place_of_service = "urban areas only"
    else:
        place_of_service = "ERROR"
else:
    place_of_service = "urban areas only"
    print("You will work in:", place_of_service)
    
    





    