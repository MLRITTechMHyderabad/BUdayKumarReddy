customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

ava_dis=lambda emp:{
    "name":emp["name"],
    "age":emp["age"],
    "total_purchase":round(
        emp["total_purchase"]*0.9 if (emp["age"]>=18 and emp["age"]<=28) else
        emp["total_purchase"]*0.95 if (emp["age"]>=26 and emp["age"]<=48) else
        emp["total_purchase"]
    ) 
    
}

updateva=list(map(ava_dis,customers))
print(updateva)




