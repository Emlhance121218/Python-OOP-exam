temperature = float(input("Enter temperature (°C): "))

if temperature >= 35:
    print("Hot Day")
elif temperature >= 20:
    print("Warm Day")
elif temperature >= 10:
    print("Cool Day")
else:
    print("Cold Day")
