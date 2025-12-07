import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("/home/user456/CommonRuntime/PYL1001_Updated_Tutorial_Marks(1).xlsx")
cols = df.columns.tolist()
cols[0] = "id"   
df.columns = cols
print(df.head())
df2=pd.read_excel("/home/user456/CommonRuntime/PYL1001_PMT_Marks_PDF.xlsx")
cols = df2.columns.tolist()
cols[0] = "id"  
df2.columns = cols
df3=pd.merge(df,df2,on="id",how="outer")
df3.to_excel("final.xlsx",index=False)
print(df3.head())