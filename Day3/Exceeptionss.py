
def calculator(a,b,operator):
   

    if operator=='+':    
        return a+b
    elif operator=='-':
        return a-b
    elif operator=='*':
        return a*b
    elif operator=='/':
        if b==0:
            try:
                a/b
            except ZeroDivisionError as e:
                print(e)       
        return a/b
    elif operator=='%':
        if b==0:
            try:
                a/b
            except ZeroDivisionError as e:
                print(e)
        return a%b
    elif operator=='**':
        return a**b
    else:
        raise ValueError("unsupported error")
    
               
a=input("enter the first number")
b=int(input("enter the second number"))
operator=str(input("enter a character"))
result=calculator(a,b,operator)
print(result)