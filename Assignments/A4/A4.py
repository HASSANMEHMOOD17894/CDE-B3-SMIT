                                  # Assignments A4

# 1. Write a program that accepts a list from user and print 
# the alternate element of list
'''
list = input("enter a list of elements seperated by spaces:").split();

print("Alternate elements in the list are: ", list[::2]);

# 2. Write a program that accepts a list from user. 
# Your program should reverse the content of list and display it. 
# Do not use reverse() method. 

list = input("enter a list of elements seperated by spaces: ").split();
print(list[::-1]);


# 3. Find and display the largest number of a list without using 
# built-in function max(). Your program should ask the user to input 
# values in list from keyboard. 
nums = list(map(int, input("enter a list of numbers seperated by spaces: ").split()));

largest = nums[0];
for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i];
    
print("Largest number in the list is:", largest);        


#  4. Write a program that rotates the element of a list so that the element at the first
# index moves to the second index, the element in the second index moves to the third index, 
# etc., and the element in the last index moves to the first index. 

elements = input("enter a list of elements seperated by spaces: ").split();
rotated_list = elements[-1:] + elements[:-1]
print("Rotated list is:", rotated_list);


# 5. Write a program that input a string and ask user to delete a given word from a string. 
string = input("enter a sentence: "); # my name is hassan mehmood
del_word = input("enter a word to delete from the sentence: ");
for word in string.split():
    if word == del_word:
        string = string.replace(word, "");
print("String after deleting the word is:", string);


# 6. Write a program that reads a string from the user containing a date in the
# form mm/dd/yyyy. It should print the date in the form March 12, 2021.

string = input("enter a date like this mm/dd/yyyy: ");
print("the required date form is: ",string.replace('/'," "));


#  7. Write a program with a function that accepts a string from keyboard and create
# a new string after converting character of each word capitalized. For instance, 
# if the sentence is "stop and smell the roses." the output should be "Stop And Smell The Roses" 


string = input("enter a sentence: ");
new_string = string.upper();
print("New string with capitalized characters is:", new_string);


# 8. Find the sum of each row of matrix of size m x n. For example for the following matrix output will be
#like this :
#           2 11 7 5
#           8 1  5 6
#           9 10 3 4
           
#Sum of row 1 = 32
#Sum of row 2 = 31
#Sum of row 3 = 63 

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

#list_matrix [rows][cols]=0; hum c++ mein aise karte hain
list_matrix = [[0 for j in range(cols)] for i in range(rows)]; # python mein aise karte hain
for i in range(rows):
    for j in range(cols):
        list_matrix[i][j] = int(input("Enter element "+ str(i) +"," + str(j) + ": "));
        
for i in range(rows):
    r_sum = 0;
    for j in range(cols):
        r_sum += list_matrix[i][j];
        
    print("Sum of row" , i + 1 , " = " , r_sum)
'''

# 9.Write a program to add two matrices of size n x m. 

matrix1 =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 =[
    [9 ,3 ,5],
    [6 ,4 ,2],
    [1 ,7 ,8]
]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j];
for r in result:
    print(r);
    
# 10. Write a program to multiply two matrices of size n x m.

matrix1 =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 =[
    [9 ,3 ,5],
    [6 ,4 ,2],
    [1 ,7 ,8]
]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j];
for r in result:
    print(r);
    
