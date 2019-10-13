# AI_Lesson2_Homework1 
# Input a year and decide whether the year is a leap year or not
year_no = int(input('Please input the year: '))
if year_no % 4 == 0:
    print('Year ', year_no, ' is a leap year')
else:
    print('Year ', year_no, ' is not a leap year')
