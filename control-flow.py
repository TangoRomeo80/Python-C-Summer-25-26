# marks = 0
# # if marks >= 50:
# if marks:
#     print("Passed")
# elif marks >= 40:
#     print("Reappear")
# else:
#     print("Failed")

# is_raining = True
# is_moroccan = True
# if is_raining:
#     print("Take an umbrella")
#     if is_moroccan:
#         print("Wear a djellaba")
#     else:
#         print("Wear a raincoat")
# else:
#     print("Enjoy the sun")

day = 3
match day:
    # case 1 | 2 | 3 | 4 | 5:
    #     print("Weekday")
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

