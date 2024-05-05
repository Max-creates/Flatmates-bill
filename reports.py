from fpdf import FPDF
import os
import webbrowser


class PDFReport:
    """
    Creates a PDF file that contains data about
    the flatmates such as their names, due amounts and the period of
    the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        # Calculate and round the amount each flatmate pays and store in variable
        flatmate1_pay = round(flatmate1.pays(bill, flatmate2), 2)
        flatmate2_pay = round(flatmate2.pays(bill, flatmate1), 2)

        # Create PDF file and add data to it
        pdf = FPDF(orientation='P', unit='pt', format='A4')

        # Add page
        pdf.add_page()

        # Add icon
        pdf.image(name="files/house.png", w=30, h=30)

        # Set font
        pdf.set_font("Times", size=24, style='B')
        # Add title
        pdf.cell(0, 30, txt="Flatmates Bill", border=0, align="C", ln=1)
        # Add bill value
        pdf.cell(300, 30, txt=f"Bill amount: {bill.amount}", border=0, ln=1)
        # Add bill period
        pdf.cell(300, 30, txt=f"Bill period: {bill.period}", border=0, ln=2)
        # Change font
        pdf.set_font("Times", size=16)
        # Add name and due amount of the first flatmate
        pdf.cell(300, 20, txt=f"{flatmate1.name} pays: {flatmate1_pay}",
                 border=0, ln=1)
        # Add name and due amount of the second flatmate
        pdf.cell(300, 20, txt=f"{flatmate2.name} pays: {flatmate2_pay}",
                 border=0, ln=1)

        # Change directory
        os.chdir("files")
        # Save PDF file
        pdf.output(self.filename)
        # Open pdf
        webbrowser.open(self.filename)


