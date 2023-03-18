import pandas as pd
data=pd.read_csv("data/Test.csv")
rule1=data['column1'].isnull().sum()==0
rule2=data['column2'].astype(str).str.isnumeric().all()
rule3=data(['column3']>=0).all() and (data['column3']<=100.all()
if rule1 and rule2 and rule3:
                                      print("Validation Passed!")
else:
                                      print("Validation Failed")
