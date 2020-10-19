import pandas as pd 

countryStats = pd.read_csv('Resources/CleanCountryStats.csv')
countryStats.to_html('CountryStats.html')