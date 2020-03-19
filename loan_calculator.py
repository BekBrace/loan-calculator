# Import tkinter
from tkinter import *


class LoanCalculator:
    def __init__(self):

        window = Tk()  # Create a window
        # Set title
        window.title("Loan Calculator")
        window.geometry("400x200")  # set the dimensions
        # create the input boxes.
        Label(window, text="Annual Interest Rate").grid(row=1,
                                                        column=1, sticky=W)
        Label(window, text="Number of Years").grid(row=2,
                                                   column=1, sticky=W)
        Label(window, text="Loan Amount").grid(row=3,
                                               column=1, sticky=W)
        Label(window, text="Monthly Payment").grid(row=4,
                                                   column=1, sticky=W)
        Label(window, text="Total Payment").grid(row=5,
                                                 column=1, sticky=W)

        # for taking inputs
        # StringVar is a class from tkinter , used so that you can easily monitor changes to tkinter variables if they occur.
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar,
              justify=LEFT).grid(row=1, column=2)

        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable=self.numberOfYearsVar,
              justify=LEFT).grid(row=2, column=2)

        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar,
              justify=LEFT).grid(row=3, column=2)

        # Output of monthly payment and total payment
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable=self.monthlyPaymentVar).grid(row=4,
                                                                                    column=2, sticky=E)

        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable=self.totalPaymentVar).grid(row=5,
                                                                                column=2, sticky=E)

        # create Compute Payment button
        btComputePayment = Button(window, text="Compute Payment",
                                  command=self.computePayment).grid(
            row=6, column=3, sticky=E)
        window.mainloop()  # Create an event loop - To run the program

    # compute the total payment. 2
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberOfYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int(self.numberOfYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    # compute the monthly payment.1
    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / \
            (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

        # create the widget . The root window is a main application window in our programs. It has a title bar and borders. These are provided by the window manager.
        root = Tk()

 # call the class to run the program.
LoanCalculator()
