# loan-calculator
This is a loan calculator programmed in Python 3.7.6 and using Tkinter library for GUI interface

Few points for better understanding ...

tkinter module contains the tk toolkit. Here in this example, we are importing the whole module of tkinter in the firstline. 
Next, We are creating a user-defined Class named LoanCalculator which holds it’s own data member and member functions.
def__init__(self) is a special method in Python Class. It is a constructor of a Python class, then we create a window using Tk(). 
The label function creates a display box to take input and use grid method to give it a table like structure.

Why we used sticky argument?
By default, widgets are created in the center, using sticky arguments we can change it. It takes 4 values: N, S, E, W. i.e. North, East, South, West.

Then we create some object named self.annualInterestRateVar, self.numberOfYearsVar, self.loanAmountVar, self.monthlyPaymentVar, self.totalPaymentVar and for the first 3 object we take the input using entry() function.
Then we create the button namely compute payment, when you click the button it calls the compute payment function which belongs to the class loan calculator. Using mainloop function we run our application program.
Create a function computepayment() inside the class. Here we store our inputs of the object in some variables, to simplify our mathematical calculation.

In the next step, we create another function named getMonthlyPayment() inside the class. After getting the required inputs it computes the monthly payment using the simple mathematical function given in the program.
Now root=Tk() means to initialize tkinter , we have to create a widget which is a window. Note that root widget must be created before any other widget.
