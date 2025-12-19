#script that promts user for hours worked and hourly rate and calculates pay
worked_hours = int(input('how many hours did you work this week? '))
hourly_rate = int(input('how much is your hourly rate? '))
weekly_earning = worked_hours * hourly_rate
print('you earned', weekly_earning, 'this week!')