student=[("Alice",[85,90,78,92]),
         ("Bob",[60,65,70,75]),
         ("charlie",[40,45,50,55]),
         ("David",[95,100,98,92])]
di={}

for name,marks in student:
    di[name]=marks   
print(di)    

avg_marks={}
for name,marks in di.items():
    avg_marks[name]=sum(marks)/len(marks)
    if name =='Bob':
         print("average marks of bob :",avg_marks[name])
    
    highest=max(avg_marks,key=avg_marks.get)
print(avg_marks)            
print(highest)    

c=0

for avgmarks in avg_marks.values():
    
    if avgmarks > 50:
        c+=1
print("no of students passed",c)