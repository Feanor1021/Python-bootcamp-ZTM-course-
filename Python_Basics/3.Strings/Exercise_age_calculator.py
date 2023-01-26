
cur_date=[17,1,2023]

birth_year_list = input("Please enter your born date (D.M.Y) = ")
birth_year_list = birth_year_list.split(".")

birth_day=int(birth_year_list[0])
birth_month=int(birth_year_list[1])
birth_year=int(birth_year_list[2])

age = int((cur_date[2] - birth_year) + (cur_date[1] - birth_month) * 0.083 - (birth_day -cur_date[0])*0.0027) #I've created this formula to calculate exact age.
#first we calculate the difference between the years, then the contribution of the month difference to the age, and finally the contribution of the day to the age
#most probably formula is wrong.

print(f"Your age is = {age}") 

