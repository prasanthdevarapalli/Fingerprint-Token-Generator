import pandas as pd
from pathlib import Path
x=21
file1=Path('templunch'+str(x)+'.csv')
if (file1.is_file()==True):
    x=file1.is_file()
    print(x)
    print("yes")

df=pd.read_csv("templunch21.csv")
print(df["Name"].count())
df.set_value(0,'Name','saraaaa')
pos="prasanth"
val=df.query('Name not in @pos')
print(val)
