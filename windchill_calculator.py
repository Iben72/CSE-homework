def calculate_windchill(temperature, speed):
    return 35.74 + 0.6215 * temperature - 35.75 * (speed ** 0.16) + 0.4275 * temperature (speed **0.16)

def convert_fahrenheit(celcius):
    return celcius * 9/5 + 32

for wind_speed in range(5, 65, 5):
    user_temperature = float(input("what is the temperature? ")).strip().lower()
    class_temperature = input("fahrenheit or celcius F/C? ")
    if class_temperature == "fahrenheit":
        windchill = calculate_windchill(temperature, speed)
        print(f"at {temperature:.2f} and {wind_speed}mph, the windchill is {windchill}")

    elif class_temperatue == "celcius":
        temperature = convert_fahrenheit(celcius)
        windchill = calculate_windchill(temperature,speed)
        print(f"at {temperature:.2f} and {wind_speed}mph, the windchill is {windchill}")

    else:
        print("invalid temperature class. please enter either fahrenheit or celcius")

calculate_windchill(user_temperature, wind_speed)