

# 365 days in a year  
# 24 hours in a day
# 60 minutes in an hour
# 60 seconds in a minute

days_in_a_year = 365
hours_in_a_day = 24
minutes_in_an_hour = 60     
seconds_in_a_minute = 60

# Calculate the total number of seconds in a year

def calculate_seconds_in_year():
    total_seconds = days_in_a_year * hours_in_a_day * minutes_in_an_hour * seconds_in_a_minute
        


    print(f"The total number of seconds in a year is: {total_seconds}")

if __name__ == "__main__":
    calculate_seconds_in_year()