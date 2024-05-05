from flat import Bill, Flatmate
from reports import PDFReport

while True:
    bill_amount_input = float(input("Enter bill amount: "))
    period_input = input("What is the bill period? Example: November 2020: ")
    the_bill = Bill(amount=bill_amount_input, period=period_input)

    flatmate1_name_input = input("What is your name? ")
    flatmate1_days_input = int(input(f"How many days did {flatmate1_name_input} stay in the house during the bill period? "))
    flatmate1 = Flatmate(name=flatmate1_name_input, days_in_house=flatmate1_days_input)

    flatmate2_name_input = input("What is the name of the other flatmate? ")
    flatmate2_days_input = int(input(f"How many days did {flatmate2_name_input} stay in the house during the bill period? "))
    flatmate2 = Flatmate(name=flatmate2_name_input, days_in_house=flatmate2_days_input)

    print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
    print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1))

    pdf = PDFReport(f"{period_input}.pdf")
    pdf.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
    print(f"PDF has been created at files/{period_input}.pdf")

    choice = input("Do you want to run the program again? y or n: ")
    if choice == "y":
        continue
    if choice == "n":
        print("Thank you for using the program!")
        break

