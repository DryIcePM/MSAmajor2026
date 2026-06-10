while (True):
    try:
        user_hours_daily = float(input("Enter the amount of hours you work a day: "))
        if user_hours_daily > 24 or user_hours_daily <= 0:
            print("ERROR: Please answer from numbers 1-24. Try again.\n")
            continue
        break
    except:
        print("ERROR: Please answer in numerical terms.\n")
        continue


while (True):
    try:
         user_hourly_wage = float(input("Enter your hourly wage: "))
         if user_hourly_wage <= 0 or user_hourly_wage == 0:
          print("ERROR: Please enter an amount of income greater than 0.\n")
          continue
         break
    except:
         print("ERROR: Please answer in numerical terms.\n")
         continue

wages_earned_in_a_day = (user_hourly_wage * user_hours_daily)

annual_wage = wages_earned_in_a_day * 350

tax_amount = annual_wage * 0.12

wage_after_taxes = annual_wage - tax_amount

print(f"Pay Advise:\n--------------\nHours worked per day: {user_hours_daily:.2f}\nHourly wage: {user_hourly_wage:.2f}\nWages before taxes: {annual_wage:.2f}\nTax amount: {tax_amount:.2f}\nAnnual wage after taxes: {wage_after_taxes:.2f}")
