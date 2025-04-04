li=[5,6,3,2,1,5,7,8,9]

min_val = li[0]  # Initialize min with the first element
max_val = li[0]  # Initialize max with the first element

for i in range(len(li)):  
    if li[i] < min_val:  
        min_val = li[i]  # Update min if a smaller value is found
    if li[i] > max_val:
        max_val = li[i]  # Update max if a larger value is found

print("Min:", min_val)
print("Max:", max_val)



