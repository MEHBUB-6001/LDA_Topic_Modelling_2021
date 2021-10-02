import pandas as pd
country_name=pd.Series(["INDIA","ENGLAND","BANGLADESH","AUSTRALIA"])
runs=pd.Series([231,187,220,250])
wickets=pd.Series([5,10,8,9])
overs=pd.Series([50,47,50,50])
data={"Country_Name":country_name,"Runs":runs,"Wickets":wickets,"Overs":overs}
final_data_format=pd.DataFrame(data)
print(final_data_format)
