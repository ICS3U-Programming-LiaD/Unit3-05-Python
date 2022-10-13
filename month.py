
#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: October 13th 2022
# This program asks the user for a number
#between 1-12 and then tells them the corresponding month

def find_month(month):
    months = {
# What each number represents
        1: "{} represents January.". format(month),
        2: "{} represents February.". format(month),
        3: "{} represents March.". format(month),
        4: "{} represents April.". format(month),
        5: "{} represents May.". format(month),
        6: "{} represents June.". format(month),
        7: "{} represents July.". format(month),
        8: "{} represents August.". format(month),
        9: "{} represents September.". format(month),
        10: "{} represents October.". format(month),
        11: "{} represents November.". format(month),
        12: "{} represents December.". format(month),
    }
    return months.get(month, "error. {} does not correspond to a month.".
                format(month))

if __name__ == "__main__":

        # Getting the user input
    user_month = int(input("Enter the number for a month: "
                        ))
    # Displaying what month the user's number represents
print(find_month(user_month))