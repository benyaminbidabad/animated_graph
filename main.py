import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


file_path=".\Input Data\populations.txt"

df=pd.read_csv(file_path)
df["Age Group"]=df["Age Group"].fillna(method="ffill")

df["Males"]=df["Males"].str.replace(",","").astype('int')
df["Females"]=df["Females"].str.replace(",","").astype('int')
df['Females']=df['Females']*-1


fig, ax=plt.subplots(figsize=(15,8))
def animate(year):
    ax.clear()
    filtered=df[df["Year"]==year]
    ax.set_xlim(-2_000_000,2_000_000)
    males=plt.barh(y=filtered["Age Group"], width=filtered["Males"],color="blue")
    females=plt.barh(y=filtered["Age Group"], width=filtered["Females"],color="red")

    ax.get_xaxis().set_visible(False)
    for edge in ["left","right","bottom","top"]:
        ax.spines[edge].set_visible(False)
    ax.tick_params(left=False)

    ax.bar_label(males, padding=3, labels=[f'{round(x,-3):,}' for x in filtered['Males']])
    ax.bar_label(females,padding= 3, labels=[f'{-1*round(x,-3):,}' for x in filtered['Females']])

    ax.legend([males,females],["Males","Females"])

    ax.set_title(f"Canada's Poulation in {year}",size=18,weight="bold")

animation=FuncAnimation(fig, animate,frames=df["Year"].unique())
animation.save("./output/Population Distribution.gif",dpi=300,writer=PillowWriter(fps=5))


