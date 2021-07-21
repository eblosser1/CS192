print("ABC Inc., Gross Pay Calculator!")
name = 1
while name != "0":
    name = input("Enter employee's name or 0 to quit: ")
    if name == "0":
        print("Exiting program...")
        break
    hours = int(input("Enter hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    print("Employee Name: " + name)
    if hours <= 40:
        gross_pay = hours * pay_rate
        print("Gross pay: " + str(gross_pay))
    elif hours > 40:
        regular_hours = 40
        overtime_hours = hours - 40
        overtime_pay = (1.5 * pay_rate) * overtime_hours
        gross_pay = (regular_hours * pay_rate) + overtime_pay
        print("Gross pay: " + str(gross_pay))
        print("(overtime pay: " + str(overtime_pay) + ")")





