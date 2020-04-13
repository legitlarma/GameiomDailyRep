# Gameiom Daily Report Collection

Files:
  - **Qeetoto_BacklogScript_CSV.py**
    - From a user-defined start and end date, the program logs into Gameiom account and  automates the downloads of all csv files in gameiom daily reports and moves data into a single excel (xlsx) document
  - **Qeetoto_Daily_CSVFile.py**
    - Downloads individual daily report for chosen day
    - Moves data into permanent location
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

  - Python 3.7.3
    - selenium 3.141.0
      - chromedriver
    - openpyxl 3.0.3
    - pandas 0.25.3
    - numpy 1.15.1
    - xlrd 1.2.0
  - Google Chrome 80.0.3987.163 (Version won't impact program... I think)
    - Make sure the downloads location is the default OS downloads folder, so the program can find the path for each of the downloaded CSV files.


Installation:
  
  - Google Chrome:
    - https://www.google.co.uk/chrome/?brand=CHBD&gclid=Cj0KCQjw-Mr0BRDyARIsAKEFbef_cgSWiueBquxOAjT_eOyzBFO2-26xPHg1h160mMPW2wHubd3bj5QaAkTeEALw_wcB&gclsrc=aw.ds
  
  - Python (3.7.3)
    - Downlaod and install appropriate file: https://www.python.org/downloads/release/python-373/
    
  - Install Pip: Use pip to install all packages for python
    - https://pip.pypa.io/en/stable/installing/
    
  - Selenium installation: 
    - https://selenium-python.readthedocs.io/installation.html
    - ***Don't install the chromedriver as it is already in the git repository***
  
  - Openpyxl:
    - 'pip install openpyxl'
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
