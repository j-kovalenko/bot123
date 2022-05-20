# bot123
## installing
### downloading requirements.txt:
* Change directory to the project directory: ``` cd <path>. ```
* Install required libraries: ``` pip install -r requirements.txt ```
### setting webhook
info about it in telegram api: https://core.telegram.org/bots/api#setwebhook
### creating a token for weather
i use https://weatherstack.com for getting weather info. you have to register and get your personal token there(it's free, but limited)
### making secret_files.py
in the app.py i have an import from secret_files.py. you have to create this file and set variables ```TOKEN``` with your telegram token and ```WEATHER_TOKEN``` with your weatherstack token
## technologies
I used **flask** for handling and **requests** for requests :) to telegram api.
## sources
[currency parser](https://itproger.com/news/programma-na-python-dlya-otslezhivaniya-kursa-valyuti)
