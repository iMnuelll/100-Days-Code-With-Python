# TIP CALCULATOR
print("Welcome to the tip Calculator!")
ask_total_bill = float(input("What was the total bill? $"))
ask_tip_percent = int(input("How much tip would you like to give? 10,12, or 15? "))
ask_people = int(input("How many people to split the bill? "))

total_bill = ask_total_bill * (1+(ask_tip_percent/100))
total_billFix = round(total_bill, 2) / ask_people
total_billFix = "{:.2f}".format(total_billFix)
# rumus = (int(total_bill)/int(ask_people))*(1+(int(tip_percent)/100))
print(f"Each person should pay ${total_billFix}")