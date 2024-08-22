import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


file_path=".\Input Data\populations.txt"

df=pd.read_csv(file_path)
df["Age Group"]=df["Age Group"].fillna(method="ffill")

df["Males"]=df["Males"].str.replace(",","").astype('int')
df["Females"]=df["Females"].str.replace(",","").astype('int')
df['Females']=df['Females']*-1

filtered=df[df["Year"]==2000]
fig, ax=plt.subplots(figsize=(15,8))
males=plt.barh(y=filtered["Age Group"], width=filtered["Males"])
females=plt.barh(y=filtered["Age Group"], width=filtered["Females"])


ax.bar_label(males,padding= 3, labels=[f'{round(x,-3):,}' for x in filtered['Males']])
plt.show()

