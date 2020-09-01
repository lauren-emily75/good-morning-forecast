# good-morning-forecast
A script to greet you with the local weather forecast using the open weather API and ToastNotifier. When run on Windows, a Notification window will be displayed with a greeting and local weather forecast

## 3rd Party Packages:
- ToastNotifier `pip install ToastNotifier`

## Build and Run
To build and run the scrip first install the listed third party packages. Next you will need to get an API key for the open weather API here:
https://openweathermap.org/api

Once you have your API key, save it to a text file called 'key.txt'.
In the script, to display the notification with your own name change <your name> to your own name.
To run the script from the console: `python morning_forecast.py <your location>` eg `python morning_forecast.py Dublin`

You can create a batch file and use the task scheduler to run the script every morning to get the daily weather forecast
