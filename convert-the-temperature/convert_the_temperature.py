def convertTemperature(celsius: float) -> list[float]:
    temperatures = []

    kelvin = celsius + 273.15
    temperatures.append(kelvin)

    fahrenheit = celsius * 1.80 + 32
    temperatures.append(fahrenheit)

    return temperatures


print(convertTemperature(36.50))
print(convertTemperature(122.11))
