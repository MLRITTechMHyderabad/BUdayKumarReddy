employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]
# di={}
# for name,salary,rating in employees:
#     if rating > 3:
#             salary+=(salary*10)/100
#     elif rating ==3:
#             salary+=(salary*5)/100
#     elif rating <=2:
#              salary-=(salary*3)/100            
# print(di)
adjust_salary = lambda emp: {
    "name": emp["name"],
    "salary": round(
        emp["salary"] * 1.10 if emp["rating"] >= 4 else
        emp["salary"] * 1.05 if emp["rating"] == 3 else
        emp["salary"] * 0.97, 2
    ),
    "rating": emp["rating"]
}
updateval=list(map(adjust_salary,employees))

print(updateval)
