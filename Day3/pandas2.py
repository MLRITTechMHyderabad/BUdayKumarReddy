import pandas as pd

data = {
    'Student': ['John', 'Sara', 'Mike', 'Anna', 'David', 'Emily', 'Chris', 'Sophia'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Marks': [85, 72, 90, 65, 78, 88, 92, 55],
    'Attendance': [92, 80, 95, 70, 85, 90, 97, 60]
}

df = pd.DataFrame(data)
print(df)

avg_marks=df.groupby('Subject')['Marks'].mean()
print(avg_marks)

Scored=df[(df['Marks'] > 85) & (df['Attendance'] <= 90 )]
print(Scored[['Student','Subject','Marks','Attendance']])

def Grade(Marks):
    if Marks > 90:
        return "A"
    elif  80 < Marks <= 90 :
        return "B"
    elif 70 < Marks <= 80:
        return "C"
    else:
        return "D"
df['Grade']=df['Marks'].apply(Grade)
print(df[['Student','Subject','Marks','Attendance','Grade']])    