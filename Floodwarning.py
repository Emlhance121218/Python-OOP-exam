water_level = float(input("Enter current water level (m): "))
threshold = 5.0

if water_level >= threshold:
    print("Flood Warning: Evacuate the area!")
else:
    print("Safe: Water level is normal.")
