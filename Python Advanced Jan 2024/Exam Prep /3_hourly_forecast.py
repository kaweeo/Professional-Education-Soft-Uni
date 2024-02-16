def forecast(*weather_data):
    result = ""
    weather_dict = {
        "Sunny": [],
        "Rainy": [],
        "Cloudy": []
    }

    for data in weather_data:
        location, weather = data
        weather_dict[weather].append(location)

    for value in weather_dict.values():
        value.sort()

    for weather in ["Sunny", "Cloudy", "Rainy"]:
        for location in weather_dict[weather]:
            result += f"{location} - {weather}\n"

    return result

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))