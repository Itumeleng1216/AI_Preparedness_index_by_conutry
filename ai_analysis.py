import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#Importing the dataset and creating the visualizations
df = pd.read_csv('ai_master.csv')
top10 = df.sort_values("aipi_score", ascending=False).head(10)


#plottinmg the top 10 and bottom 10 countries by AI performance index, as well as the average scores for each component and the relationship between each component and the overall AI performance index.
plt.figure()
plt.bar(top10["country"],
        top10["aipi_score"],
        color='blue')
plt.xticks(rotation=90)
plt.title("Top 10 Countries by AI Performance Index")
plt.xlabel("Country")
plt.ylabel("AI Performance Index Score")
plt.savefig('figure1.png')
plt.show()

bottom10 = df.sort_values("aipi_score", ascending=True).head(10) 
plt.figure()
plt.bar(bottom10["country"],
        bottom10["aipi_score"],
        color='red')
plt.xticks(rotation=90)
plt.title("Bottom 10 Countries by AI Performance Index")
plt.xlabel("Country")
plt.ylabel("AI Performance Index Score")
plt.savefig('figure2.png')
plt.show() 

means = df[["aipi_score","digital_score", "innovation_score", "human_capital_score", "regulation_score"]].mean()
plt.figure()
plt.bar(means.index, means.values, color='green')
plt.xticks(rotation=10)
plt.title("Average AI Component Scores")
plt.savefig('figure3.png')
plt.show()


plt.figure()
plt.scatter(df["digital_score"],df["aipi_score"])
plt.xlabel("Digital infrastructure")
plt.ylabel("AI preparedness")
plt.title("Digital infrastructure Index vs AI Preparedness")
plt.savefig("figure4.png")
plt.show()

plt.figure()
plt.scatter(df["innovation_score"],df["aipi_score"])
plt.xlabel("Innovation & economic performance")
plt.ylabel("AI preparedness")
plt.title("innovation_score vs AI Preparedness")
plt.savefig("figure5.png")
plt.show()

plt.figure()
plt.scatter(df["human_capital_score"],df["aipi_score"])
plt.xlabel("human capital")
plt.ylabel("AI preparedness")
plt.title("human_capital_score vs AI Preparedness")
plt.savefig("figure6.png")
plt.show()

plt.figure()
plt.scatter(df["regulation_score"],df["aipi_score"])
plt.xlabel("regulation and policies")
plt.ylabel("AI preparedness")
plt.title("regulation_score Index vs AI Preparedness")
plt.savefig("figure7.png")
plt.show()



