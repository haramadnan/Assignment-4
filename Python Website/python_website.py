import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Student Data Generator", layout="wide")
st.title("Student CSV File Generaator ✨")

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Ahmed", "Haram", "Laiba", "Huzaifa", "Abdulllah", "Rehma", "Arsal", "Arham","Lamiya", "Arfa"]

studnts = []
for i in range(1, 15):
    students = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(15, 20),
        "Grade": random.choice(["A", "B", "C", "D", "E"]),
        "Marks": random.randint(50, 100),
    }
    studnts.append(students)

df = pd.DataFrame(studnts)
st.subheader("Generate Student Data")
st.dataframe(df)

csv_file = df.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV File", data=csv_file, file_name="students.csv", mime="text/csv")
st.success("CSV file generated successfully!")