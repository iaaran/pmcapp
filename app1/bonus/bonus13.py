feet_inches = input("Enter feet and inches: ")


def parse(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet,inches):
    meters = round((feet * 0.3048 + inches * 0.0254), 2)
    return meters


parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']}  inches is equal to {result} meters")
if result < 1.3:
    print("Kid is too small")
else:
    print("Kid can use the slide")