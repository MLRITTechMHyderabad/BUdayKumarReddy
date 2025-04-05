import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
    'Age': [25, 32, 29, 41, 37, 45, 26, 38],
    'Salary': [50000, 70000, 65000, 80000, 75000, 90000, 62000, 85000],
    'Experience': [2, 7, 5, 15, 10, 20, 3, 12]
}

df = pd.DataFrame(data)

print(df)
avg_salary = df.groupby('Department')['Salary'].mean()
print("1. Average Salary by Department:\n", avg_salary)
high=df.loc[df.groupby('Department')['Salary'].idxmax()]
print("\n2. Highest Paid Employee in Each Department:\n", high[['Department', 'Employee', 'Salary']])

qualified_employees = df[(df['Experience'] > 5) & (df['Salary'] > 65000)]
print("\n3. Employees with >5 years experience and salary > 65,000:\n", qualified_employees[['Employee', 'Experience', 'Salary']])
print(f"Total count: {len(qualified_employees)}")

def seniority(exp):
    if exp < 5:
        return "Junior" 
    elif exp>=5 & exp<=10:
        return "Mid-Level"
    else:
        return "Senior"
df['seniority']=df['Experience'].apply(seniority)
print(df[['Employee','Experience','Salary','seniority']])    
