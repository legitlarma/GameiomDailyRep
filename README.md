# Gameiom Daily Report Collection

Files:
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
  - **chromedriver**
    - Driver used by Selenium to allow for Google Chrome to automatically open


Requirements:
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


Installation:
  
  - Google Chrome:
    - https://www.google.co.uk/chrome/?brand=CHBD&gclid=Cj0KCQjw-Mr0BRDyARIsAKEFbef_cgSWiueBquxOAjT_eOyzBFO2-26xPHg1h160mMPW2wHubd3bj5QaAkTeEALw_wcB&gclsrc=aw.ds
  
  - Python (3.7.3)
    - Download and install appropriate file: https://www.python.org/downloads/release/python-373/
    
  - Install Pip: Use pip to install all packages for python
    - https://pip.pypa.io/en/stable/installing/

  **Once Pip is installed, you can install all Python modules by going into your terminal and typing:**
   ```console
   pip install -r requirements.txt
   ```

  Or

  Individually install (why though...):
  
  - Selenium installation: 
    - https://selenium-python.readthedocs.io/installation.html
    - ***Don't install the chromedriver as it is already in the git repository***
  
  - Openpyxl:
    - ```console
        pip install openpyxl
      ```
    - https://openpyxl.readthedocs.io/en/stable/
  
  - Pandas
    - 'pip install pandas'
    - https://pypi.org/project/pandas/
  
  - Numpy:
    - 'pip install numpy'
    - https://www.edureka.co/blog/install-numpy/
    
  - Xlrd:
    - 'pip install xlrd'
    - https://pypi.org/project/xlrd/#description
    
  - Schedule:
    - 'pip install schedule'
    - https://pypi.org/project/schedule/
