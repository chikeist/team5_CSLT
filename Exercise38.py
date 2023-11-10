month = input("Enter the month name : ")

if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
  print("Number of days in that month: 31")

elif month == "April" or month == "June" or month == "September" or month == "November":
  print("Number of days in that month: 30")
  
elif month == "February":
  print("Number of days in that month: 28 or 29")

else:
  print("Invalid month name!!!")