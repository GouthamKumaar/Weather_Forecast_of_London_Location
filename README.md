# Weather_Forecast_of_London_Location
API = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22" The above API is the REST GET API Which gives you the response in JSON format and hourly weather forecast of London Location

I want you to write a program to get the option from the user and print the result based on the above API.

Get weather
Get Wind Speed
Get Pressure
Exit
If the user press 1, Prompt the user for the date then print the temp of the input date. If the user press 2, Prompt the user for the date then print the wind.speed of the input date. If the user press 3, Prompt the user for the date then print the pressure of the input date. If the user press 0, Terminate the program.

The program should not terminate until the user press 0. The program should be modular.




1.	API:
•	The code is using a REST GET API to fetch weather data for London.
•	The API provides hourly weather forecast data for specific dates in JSON format.
•	The API URL is specified in the code as api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22".
2.	Requirements:
•	The code is written in Python.
•	The user is presented with a menu to select various options: get weather, get wind speed, get pressure, or exit.
•	For each option (1, 2, or 3), the user is prompted to select a date from the available dates.
•	After the user selects a date, the corresponding weather data (temperature, wind speed, or pressure) for that date is displayed.
•	The program runs until the user selects the "Exit" option (0).
3.	Libraries Used:
•	The code uses the json library to handle JSON data and the requests library to make HTTP GET requests to the API.
4.	Function Explanation:
•	get_weather_data(): This function makes an HTTP GET request to the API URL and fetches the weather data. The data is then parsed from JSON format and returned.
•	print_available_dates(weather_data): This function takes the weather data as input and extracts all unique dates from it. It then prints the available dates along with their corresponding index in the list.
•	get_weather_info(weather_data, date): This function takes the weather data and a specific date as input. It searches for the given date in the weather data and prints the temperature for that date if found.
•	get_wind_speed_info(weather_data, date): Similar to the get_weather_info() function, this function prints the wind speed for the given date.
•	get_pressure_info(weather_data, date): Similar to the above two functions, this function prints the pressure for the given date.
5.	Main Part:
•	The program runs in an infinite loop using while True, so it keeps running until the user selects the "Exit" option (0).
•	The user is presented with the main menu options (1, 2, 3, or 0) using print() statements.
•	The user's choice is taken as input using input() function.
•	Depending on the user's choice (1, 2, 3, or 0), the corresponding function is called, which then shows the available dates.
•	The user is asked to enter the number of the date they want to select.
•	The selected date's weather data is displayed using the corresponding function.
