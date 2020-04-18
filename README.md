# Gameiom Daily Report Collection

## Table Of Contents<br>
**[File Description](#File-Description)**<br>
**[Requirements](#Requirements)**<br>
**[Installation](#Installation)**<br>
**[How to use Scripts](#How-to-use-Scripts)**<br>
**[Run script from Startup]()**

## File Description:
  - **Gameiom-Daily-Report-oneTimeRun.py**
    - From user-defined start date, the program logs into Gameiom account and automates the downloads of all csv files between the start date and today-1 (yesterday). Moves all csv data into single file called 'data.xlsx' and deletes downloaded csv files.
  - **Gameiom-Daily-Report-between-dates.py**
    - From a user-defined start and end date, the program logs into Gameiom account and  automates the downloads of all csv files in gameiom daily reports and moves data into a single excel (xlsx) document
  - **Gameiom-Daily-Report-previous-day.py**
    - Downloads individual daily report for the previous day
    - Moves data into permanent --excel doc--
    - Delete individual daily report
  - **GetData.py**
    - Gets data from temporary csv file that has been downloaded
    - Moves data into permanent location
    - Deletes downloaded file
  - **functions.py**
    - Some functions created to allow the main programs to work correctly
  - **dailyCollect.sh**
    - Bash file to automatically run daily report collection of previous day at 4am every day. This has to be restarted on reboot.
    - Script can be opened automatically on startup --link to how to for windows and mac--
  - **chromedriver**
    - Driver used by Selenium to allow for Google Chrome to automatically open


## Requirements:
  - All code was created on a Mac, therefore there may be some issues with Windows systems
    - For example: The bash files won't work on Windows (Will create .bat files though)
      - Manually run programs with Windows
    - Scripts should work on Unix and MacOS systems
  - Python 3.7.3
    - selenium 3.141.0
      - chromedriver
    - openpyxl 3.0.3
    - pandas 0.25.3
    - numpy 1.15.1
    - xlrd 1.2.0
    - schedule 0.6.0
  - Google Chrome 80.0.3987.163 (Version won't impact program... I think)
    - Make sure the downloads location is the default OS downloads folder, so the program can find the path for each of the downloaded CSV files.


## Installation:
  
  - [**Google Chrome**](https://www.google.co.uk/chrome/?brand=CHBD&gclid=Cj0KCQjw-Mr0BRDyARIsAKEFbef_cgSWiueBquxOAjT_eOyzBFO2-26xPHg1h160mMPW2wHubd3bj5QaAkTeEALw_wcB&gclsrc=aw.ds)<br>
  
  - [**Python (3.7.3)**](https://www.python.org/downloads/release/python-373/)<br>

  - Install [**Pip**](https://pip.pypa.io/en/stable/installing/): Use pip to install all packages for python

  **Once Pip is installed, you can install all Python modules by going into your terminal and typing:**
   ```console
   pip install -r requirements.txt
   ```

  Or

  Individually install (why though...):
  
  - [**Selenium**](https://selenium-python.readthedocs.io/installation.html): 
    - ***Don't install the chromedriver as it is already in the git repository***
    ```console
        pip install selenium
      ```
  
  - [**Openpyxl**](https://openpyxl.readthedocs.io/en/stable/):
    ```console
        pip install openpyxl
      ```
  
  - [**Pandas**](https://pypi.org/project/pandas/)
    ```console
        pip install pandas
      ```
  
  - [**Numpy**](https://www.edureka.co/blog/install-numpy/):
    ```console
        pip install numpy
      ```
    
  - [**Xlrd**](https://pypi.org/project/xlrd/#description):
    ```console
        pip install xlrd
      ```
    
  - [**Schedule**](https://pypi.org/project/schedule/):
    ```console
        pip install openpyxl
      ```
<br>

## How to use Scripts
  ### Collecting Backlog of Daily Reports 
  ----
  On initial install (before running any other scripts), run the Gameiom-Daily-Report-oneTimeRun.py script to load the backlog of daily reports from users chosen start date. To do this, in the terminal, run the oneTimeRun.sh file:
  ```console
          bash oneTimeRun.sh
  ```
  Enter your username and password and the program will begin. All data from each csv file moves to the data.xlsx in the data directory.

  ***IMPORTANT***
  #### ***Depending on your chosen start date, the script could take a very long time to collect all the reports. Therefore it is recommended to either run the script overnight and/or when you are not using your device.***
  
  ### Collection of Daily Report for Previous Day
  ----
  There is not a script to collect for current day because the data is still being collected, therefore the daily collection is for the previous day.<br>
  <br>
  The program is coded to run at 4am and collect for previous day, which allows for any lag in Gameioms servers. Run the dailyCollect.sh script in terminal:
  ```console
          bash dailyCollect.sh
  ```
  Enter your username and password and the program should run in the background and you can close the terminal. The process will be executed at 4am every day.


## Run script from Startup
