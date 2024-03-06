import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

f = open(r"C:\Users\Imanuel Uneputty\Documents\Study-Machine-Learning\Bangkit\Belajar Analisis Data Dengan Python\Proyek-Akhir\dasboard\day_df.csv")
day_df = pd.read_csv(f)


colors = ["#D3D3D3", "#D3D3D3", "#72BCD4"]

customer_in_2012_df = day_df[day_df['yr'] == 2012].groupby("season").cnt.sum().sort_values(ascending=False).reset_index()
fig = plt.subplots(figsize=(10, 6))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x='season', y='cnt', data=customer_in_2012_df, hue='season', palette=colors)
plt.title("Customer Count in 2012")
plt.ylabel("Customer Count")
plt.xlabel("Season")
st.pyplot(plt)

compare_working_and_holiday_df = day_df.groupby("workingday").cnt.sum().sort_values(ascending=False).reset_index()
fig = plt.subplots(figsize=(10, 5))
sns.barplot(x='workingday', y='cnt', data=compare_working_and_holiday_df, hue='workingday', palette=colors)
plt.title("Customer Count by Workingday")
plt.ylabel("Customer Count")
plt.xlabel("Working Day")
plt.show()

st.pyplot(plt)
