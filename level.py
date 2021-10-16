import pandas as pd
import plotly.graph_objects as pg
df=pd.read_csv("data107.csv")
roll=input("enter the student id : ")
studentdf=df.loc[df["student_id"]==roll]
allMean=studentdf.groupby("level")["attempt"].mean()
print(allMean)
graph=pg.Figure(pg.Bar(x=["Level 1","Level 2","Level 3","Level 4"],y=allMean))
graph.show()
