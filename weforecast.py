import requests
import json
#1
def get_weather(api_key, city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
#2
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        # Extract relevant weather information
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        print(f"Weather in {city_name}:")
        print("Temperature:", temperature)
        print("Description:", description)
    except requests.exceptions.HTTPError as err:
        print("Error:", err)
    except json.JSONDecodeError:
        print("Error: Failed to parse weather data.")
    except KeyError:
        print("Error: Invalid weather data format.")
#3
def main():
    api_key = "4b463278862eba6e4cbf1df5e2a82d73"  # Replace with your OpenWeatherMap API key
    city_name = input("Enter city name: ")
    get_weather(api_key, city_name)
#4
if __name__ == "__main__":
    main()           
#By: VDMANISH
