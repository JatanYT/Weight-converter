print("Please enter the weight: ")
weight = int(input())
print("(L)bs or (K)gs")
unit_weight = input()

if unit_weight.upper() == "L":
    converted_weight = weight * 0.45
    print(f"{weight} lbs is {converted_weight} kgs")
elif unit_weight.upper() == "K":
     converted_weight = weight /  0.45
     print(f"{weight} kgs is {converted_weight} lbs")
else:
    print("Unit or weight unvalid")