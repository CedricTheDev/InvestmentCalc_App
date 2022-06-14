
"""
Program: GUItemplate.py (page 251)
Author: George 6/2/2022
Template code for all GUI-based applications

GUI based version of the invesment program from chapter 3

"""
from breezypythongui import EasyFrame
# other imports

class TextAreaDemo(EasyFrame):
	
	# definition of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame version of __init__
		EasyFrame.__init__(self, title = "Investment Calculator")
		self.addLabel(text = "initial Amount", row = 0, column = 0)
		self.addLabel(text = "Number of years", row = 1, column = 0)
		self.addLabel(text = "Interest Rate in %", row = 2, column = 0)
		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1, width = 20)
		self.rate = self.addFloatField(value = 0.0, row = 2, column = 1)
		self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
		self.button = self.addButton(text = "compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		# change the button color
		self.button["background"] = "yellow"

	# event handling method for the button
	def compute(self):
		"""computes the investment report based on the inputs and outputs the full report"""
		# Obtain and validate the inputs
		startBalance =  self.amount.getNumber()
		rate = self.rate.getNumber()
		years = self.period.getNumber()

		# If any of the inputs are zero, just exit the funtion
		if startBalance == 0 or rate == 0 or years == 0:
			self.outputArea.setText("please make sure that none of the input \nfields contain a zero")
			""" worked without return statement?"""

		# Calculation phase
		rate = rate / 100

		# Initiate the accumulator variable for the intrest
		totalInterest = 0.0

		# Display the header for the table in tabular notation
		result = "%4s%18s%10s%16s\n" % ("Year", "Starting Blance", "Interest", "Ending Balance")

		# Loop to compute and display the results for each year
		for year in range(1, years + 1): 
			interest = startBalance * rate
			endBalance = startBalance + interest
			result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest

		# Append the totals to the result string for the entire report
		result += "Ending balance: $%0.2f\n" % endBalance
		result+= "Total interest earned: $%0.2f\n" % totalInterest

		# Output the result while preserving read-only status
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"



# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	TextAreaDemo().mainloop()
# global call to the main() method
main()
