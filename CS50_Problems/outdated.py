# outdated.py
# Converts different date input formats into YYYY-MM-DD format.

import re

# List of valid month names
list_of_months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date_input = input("Date: ")   # user input (can be 9/8/1636 or September 8, 1636)
        
        # split input on spaces, commas, or slashes → removes separators
        date = re.split(r'[ ,/]', date_input)

        # remove empty strings from split result
        cleaned_date = [d for d in date if d]

        year = cleaned_date[2]

        if year.isnumeric():
            month = cleaned_date[0]

            # Case 1: Month is written in words (e.g., "September 8, 1636")
            if month in list_of_months:
                # require a comma in original input when month is written out
                if "," not in date_input:
                    continue

            # Case 2: Month is numeric (e.g., "9/8/1636")
            elif 1 <= int(month) <= 12:
                month = list_of_months[int(month) - 1]
            else:
                continue

            # Validate the day
            if 1 <= int(cleaned_date[1]) <= 31:
                if month in list_of_months:
                    month_in_num = list_of_months.index(month) + 1
                    
                    # Print year-month-day in ISO format (YYYY-MM-DD)
                    print(year, end="-")

                    # Ensure month is two digits
                    print(f"{month_in_num:02}", end="-")

                    # Ensure day is two digits
                    print(f"{int(cleaned_date[1]):02}")
                    
                    break
            else:
                continue
    except ValueError:
        continue
    except IndexError:
        continue
