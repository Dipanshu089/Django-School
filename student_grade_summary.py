# student_grade_summary.py
import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Chetan", "John", "Sara"],
    "Marks": [85, 92, 78, 88, 69]
}
df = pd.DataFrame(data)
df["Grade"] = pd.cut(df["Marks"], bins=[0, 70, 80, 90, 100], labels=["C", "B", "A", "A+"])
print("📊 Student Grades Summary:")
print(df)
print("\nAverage Marks:", df["Marks"].mean())
