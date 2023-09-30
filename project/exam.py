# # number = int(input("Enter a number: "))
# # if number % 2 == 0 and number % 3 == 0 and number % 8 != 0:
# #     print("Yes")
# # else:
# #     print("No")
# # rent = float(input("Enter the monthly rent amount: "))
# # utilities = float(input("Enter the monthly utilities amount: "))
# # security_deposit = float(input("Enter the security deposit amount: "))

# # total_cost = rent + utilities + security_deposit
# # print("The total cost of the apartment is:", total_cost)
# # a = 3 

# # b = (a != 3) 

# # print(b)
# # year = int(input("Enter a year: "))

# # if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
# #     print(year, "is a leap year")
# # else:
# #     print(year, "is not a leap year")


# # Take user inputs
# # num_questions = int(input("Enter the number of questions in the contest: "))
# num_correct = int(input("Enter the number of correct answers given by the contestant: "))

# # Calculate the total marks earned and percentage of total marks earned
# total_marks = num_correct * 5
# percentage_marks = (total_marks / (num_questions * 5)) * 100

# # Determine the final grade
# if percentage_marks >= 91:
#     final_grade = "A"
# elif percentage_marks >= 81:
#     final_grade = "B"
# elif percentage_marks >= 71:
#     final_grade = "C"
# elif percentage_marks >= 61:
#     final_grade = "D"
# else:
#     final_grade = "F"

# # Display the results
# print("Total marks earned:", total_marks)
# print("Percentage of total marks earned:", percentage_marks)
# print("Final grade:", final_grade)



import pyautogui
import time
time . sleep(4)
count = 0
while count<=100 :
    pyautogui.typewrite("happy new year"+str (count))
    pyautogui.press("enter")
    count=count+1











