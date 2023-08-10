import json
import requests

#'json' for handling JSON data, and 'requests' for making HTTP requests to the API


def get_weather_data():
    api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

    response = requests.get(api_url)
    data = response.json()
    return data["list"]


#The above function is responsible for fetching weather data from the specified API URL
#It makes an HTTP GET request to the API URL using 'requests.get(api_url)'
#Then it converts the JSON response to a Python dictionary using 'response.json()'
#The function returns the "list" key from the API response, which contains hourly weather data


def print_available_dates(weather_data):
    dates = set()
    for item in weather_data:
        date = item["dt_txt"].split()[0]
        dates.add(date)

    print("Available dates:")
    for idx, date in enumerate(dates, 1):
        print(f"{idx}. {date}")
    print("0. Exit")


#The above function takes the weather data as input and prints the available dates for which weather data is available
#It extracts the date from each item in the weather data and stores unique dates in the 'dates' set
#Then it prints the dates along with their indices using 'enumerate()'


def get_weather_info(weather_data, date):
    for item in weather_data:
        if item["dt_txt"].startswith(date):
            temperature = item["main"]["temp"]
            print(f"Temperature on {date}: {temperature} Kelvin")
            break
    else:
        print("Invalid date or data not available for the selected date.")


#The above function takes weather data and a date as input and prints the temperature for that date
#It iterates through the weather data and finds the item with a matching date (the date on which the hourly weather data starts
#Then it extracts the temperature and prints it


def get_wind_speed_info(weather_data, date):
    for item in weather_data:
        if item["dt_txt"].startswith(date):
            wind_speed = item["wind"]["speed"]
            print(f"Wind Speed on {date}: {wind_speed} m/s")
            break
    else:
        print("Invalid date or data not available for the selected date.")


#The above function is similar to 'get_weather_info()', but it prints the wind speed for the given date



def get_pressure_info(weather_data, date):
    for item in weather_data:
        if item["dt_txt"].startswith(date):
            pressure = item["main"]["pressure"]
            print(f"Pressure on {date}: {pressure} hPa")
            break
    else:
        print("Invalid date or data not available for the selected date.")


#The above function prints the atmospheric pressure for the given date


if __name__ == "__main__":
    weather_data = get_weather_data()

    while True:
        print("\n1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")


#In the 'main' section of the code, it first calls 'get_weather_data()' to fetch the weather data from the API and stores it in the 'weather_data' variable
#It then enters a 'while True' loop to repeatedly prompt the user for their choice and display the corresponding weather information


        if choice == "1":
            print_available_dates(weather_data)
            date_choice = input("Enter the number of the date: ")
            if date_choice == "0":
                continue
            date_choice = int(date_choice)
            dates_list = list(set(item["dt_txt"].split()[0] for item in weather_data))
            if date_choice >= 1 and date_choice <= len(dates_list):
                selected_date = dates_list[date_choice - 1]
                get_weather_info(weather_data, selected_date)
            else:
                print("Invalid choice. Please try again.")


#For choice "1" (Get weather), it calls 'print_available_dates()' to show the available dates to the user
#It then takes input from the user for the desired date (by number). If the user selects "0", the loop continues
#After validating the input date choice, it calls 'get_weather_info()' to display the weather information for the selected date


        elif choice == "2":
            print_available_dates(weather_data)
            date_choice = input("Enter the number of the date: ")
            if date_choice == "0":
                continue
            date_choice = int(date_choice)
            dates_list = list(set(item["dt_txt"].split()[0] for item in weather_data))
            if date_choice >= 1 and date_choice <= len(dates_list):
                selected_date = dates_list[date_choice - 1]
                get_wind_speed_info(weather_data, selected_date)
            else:
                print("Invalid choice. Please try again.")


        elif choice == "3":
            print_available_dates(weather_data)
            date_choice = input("Enter the number of the date: ")
            if date_choice == "0":
                continue
            date_choice = int(date_choice)
            dates_list = list(set(item["dt_txt"].split()[0] for item in weather_data))
            if date_choice >= 1 and date_choice <= len(dates_list):
                selected_date = dates_list[date_choice - 1]
                get_pressure_info(weather_data, selected_date)
            else:
                print("Invalid choice. Please try again.")


#The process is similar for choices "2" (Get Wind Speed) and "3" (Get Pressure)
#But the corresponding functions 'get_wind_speed_info()' and 'get_pressure_info()' are called



        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


#For choice "0" (Exit), it prints a message and breaks out of the loop, thus terminating the program
#If the user enters an invalid choice, it prints a message and repeats the loop to prompt for a valid choice again
#The program will continue to run until the user selects "0" to exit

















