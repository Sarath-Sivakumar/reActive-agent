from datetime import datetime


# -----------------------------------------
# WEATHER TOOL
# -----------------------------------------

def get_weather(city: str):

    weather_data = {
        "chennai": "Sunny, 34°C",
        "bangalore": "Rainy, 22°C",
        "mumbai": "Cloudy, 29°C"
    }

    return weather_data.get(
        city.lower(),
        f"No weather data available for {city}"
    )


# -----------------------------------------
# TIME TOOL
# -----------------------------------------

def get_current_time():

    return datetime.now().strftime("%I:%M %p")


# -----------------------------------------
# CALCULATOR TOOL
# -----------------------------------------

def calculate(expression: str):

    try:
        result = eval(expression)
        return str(result)

    except Exception:
        return "Invalid expression"