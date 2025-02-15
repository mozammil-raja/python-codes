months = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

print("Month Numbers:")
for num, name in months.items():
    print(f"{name} - {num}")

month = int(input("\nEnter month number (1-12): "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"{months[month]} has 31 days.")
elif month in [4, 6, 9, 11]:
    print(f"{months[month]} has 30 days.")
elif month == 2:
    print("February has 28 or 29 days (Leap year dependent).")
else:
    print("Invalid month number")
