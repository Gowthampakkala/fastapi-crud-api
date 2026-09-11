import pandas as pd
df= {"name":["Anil","Rahul","Priya","Amit","Neha"],
     "Id": [101,102,103,104,105],
     "salary":[62000,43000,50000,37000,77000]
}
df=pd.DataFrame(df, 
                index=["employee 1","employee 2","employee 3","employee 4","employee 5"])
df["departmenrt"]=["cse","ece","iot","bba","eee"]
print(df)
print(df[df["salary"]>50000])
print(df.sort_values(by="salary"))
print(df["salary"].mean)
print(df["salary"].max)
print(df["salary"].min)
