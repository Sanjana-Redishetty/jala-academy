#Print gender (Male/Female) program according to given M/F using switch

gender = input("Enter gender (M/F): ").upper()
switch = {
    "M": "Male",
    "F": "Female"
}
print(switch.get(gender, "Invalid Input"))
