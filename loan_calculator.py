# Get details of loan
money_owned = float(input("How much money do you owe, in dollars?\n")) # $50,000
yearly_interest = float(input("How much yearly interest you have?\n")) # 3%
monthly_payment = float(input("How much will you pay off each month in dollars?\n")) # $1,000
total_duration_in_months = int(input("How many months you want to repay the loan?\n")) #24

# Calculate monthly interest
monthly_interest_rate = yearly_interest /100 /12

for i in range(total_duration_in_months):

    # Calculate monthly interest value
    monthly_interest_paid = money_owned * monthly_interest_rate

    # Add in interest
    money_owned = money_owned + monthly_interest_paid

    if(money_owned - monthly_payment < 0):
        print('The last payment is', money_owned)
        print('You paid off the loan in', i+1, 'months')
        break
        
    # Make payment
    money_owned = money_owned - monthly_payment

    print('Paid', monthly_payment,'of which',monthly_interest_paid,'was interest')
    print('Now I owe', money_owned)