# 3. Play Computer & evaluate each line.

year = int(input("What is your year of birth? "))

if year > 1980 and year < 1994:
    print("You are a Millennial.")
elif year >= 1994:
    print("You are a Gen Z.")

# In case of year 1994 it is exiting the code. Because year 1994 is not include in the statement to check. 
# To process the year 1994 add equal to in any of the statement.
