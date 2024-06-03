age = int(input("what is your age?"))

weeks_in_a_month = 4
print("One month is equal to " + str(weeks_in_a_month) + " weeks")

weeks_in_one_year = int(12*weeks_in_a_month)
print("one year is equal to " + str(weeks_in_one_year) + " weeks")
print("A human can live up to 90 years so")

number_of_years_left = int(90 - age)
print("number of years left is " + str(number_of_years_left))

number_of_weeks_left = int(number_of_years_left * weeks_in_one_year)
print("the number of weeks left is equal to " + str(number_of_weeks_left))