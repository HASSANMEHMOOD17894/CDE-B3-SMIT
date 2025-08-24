                                     
                                     #Assignments A3
                                     
#1. Write a program that accepts a string from user.
# Your program should count and display number of
#vowels in that string. 

name=input("enter your name :");
text=name.lower();
vowels="aeiou";
count=0;
for char in text:
    if char in vowels:
        count+=1;
print("number of vowels in your name is :",count);

#2. Write a program that reads a string from keyboard and display:
#* The number of uppercase letters in the string
#* The number of lowercase letters in the string
#* The number of digits in the string
#* The number of whitespace characters in the string


string = input("enter a string: ");
upper=0;
lower=0;
digit=0;
space=0;

for char in string:
    if char.isupper():
        upper+=1;
    elif char.islower():
        lower+=1;
    elif char.isdigit():
        digit+=1;
    elif char.isspace():
        space+=1;
print("Uppercase letters:", upper);
print("Lowercase letters:", lower);
print("Digits:", digit);
print("Whitespace characters:", space);


# 3. Write a Python program that accepts a string from user. Your program should 
# create and display a new string where the first and last characters have been exchanged.
#For example if the user enters the string 'HELLO' then new string would be 'OELLH'
                                     
string = input("Enter a word: like 'hello' ");

length_of_word=len(string);

for i in range(length_of_word):
    if i == 0:
        first_char=string[i];
        for j in range(length_of_word):
          if j == length_of_word-1:
              last_char=string[j];
              temp=first_char;
              first_char=last_char;
              last_char=temp;
              new_string=last_char+string[1:length_of_word-1]+first_char;
              print("New string after exchanging first and last character is:",new_string);
              break;
          
# gpt code simple and clean 
# new_string = string[-1] + string[1:-1] + string[0]

# 4. Write a Python program that accepts a string from user. Your program should 
# create a new string in reverse of first string and display it.
#For example if the user enters the string 'EXAM' then new string would be 'MAXE' 

string = input("Enter a word: like 'exam' ");
reversed_string = string[::-1];
print("Reversed string is:", reversed_string);

# 5. Write a Python program that accepts a string from user. Your program should 
# create a new string by shifting one position to left.
# For example if the user enters the string 'examination 2021' then new string would be 
# 'xamination 2021e'
string = input("Enter a word: like 'examination 2021' "); 
shifted_string = string[1:] + string[0];
print("String after shifting one position to left is:", shifted_string);


# 6. Write a program that asks the user to input his name and print its initials.
# Assuming that the user always types first name, middle name and last name and does 
# not include any unnecessary spaces. For example, if the user enters Ajay Kumar Garg 
# the program should display A. K. G. Note:Don't use split() method 

name = input("Enter your full name (first, middle, last): ");
initials = [];
length_of_name = len(name);
for i in range (length_of_name):
    if i == 0 and name[i] != ' ':
        initials.append(name[i].upper());
    elif name[i] == ' ' and i+1 < length_of_name:
        initials.append(name[i+1].upper());
    
          
print(initials[0]+". "+initials[1]+". "+initials[2]+".");


# 7. A palindrome is a string that reads the same backward as forward.
# For example, the words dad, madam and radar are all palindromes.
# Write a programs that determines whether the string is a palindrome.
# Note: do not use reverse() method 

string = input("Enter a word: like 'madam' ");
if string == string[::-1]:
    print(string, "is a palindrome");
else:
    print(string, "is not a palindrome");
    
# 8. Write a program that display following output:
# SHIFT ,HIFTS ,IFTSH ,FTSHI ,TSHIF, SHIFT 

string = "SHIFT";

for i in range(len(string)):
    shifted_string = string[i:] + string[:i];
    print(shifted_string);
    
#  9. Write a program in python that accepts a string to setup a passwords.
# Your entered password must meet the following requirements:
#The password must be at least eight characters long.
#It must contain at least one uppercase letter.
#It must contain at least one lowercase letter.
#It must contain at least one numeric digit.
#Your program should should perform this validation. 


password = input("Enter a password: ");
if len(password) < 8:
    print("Password must be at least 8 characters long.");
elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.");
elif not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter.");
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one numeric digit.");
else:
    print("Password is valid.");
    
        
    




        
  
        
       
                                     