# keep accounts for one week

week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
income = []
expense = []
for i_day in range(7):
    i_income = int(input('Please input the income for ' + week[i_day] + ': '))
    income.append(i_income)
    i_expense = int(input('Please input the expense for ' + week[i_day] + ': '))
    expense.append(i_expense)

for i_day in range(7):
    print('The income on ', week[i_day], ' was', income[i_day])
    print('The expense on ', week[i_day], ' was', expense[i_day])
    print('The balance on ', week[i_day], ' was', income[i_day]-expense[i_day], '\n')

total_income = sum(income)
total_expense = sum(expense)
total_balance = total_income - total_expense
print('The income of this week was', total_income)
print('The expense of this week was', total_expense)
print('The balance of this week was', total_balance)