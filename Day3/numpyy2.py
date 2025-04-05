import numpy as np

resources=np.random.uniform(15,50,size=(6,3)).astype(int)
print(resources)

total=np.sum(resources,axis=0)
total_oxygen,total_water,total_food=total
print(f"Total resources needed(tons) : oxygen :{total_oxygen},water :{total_water},food :{total_food} ")

max_val=np.max(resources,axis=0)
max_oxygen, max_water, max_food = max_val
max_monthly=np.max(resources)
max_month_index = np.unravel_index(np.argmax(resources), resources.shape)
print(f"Highest consumption in a month: Water ({max_water} tons in month {max_month_index[0] + 1})")

stand=np.std(resources,axis=0)
stand_oxygen,stand_water,stand_food=stand

print(f"Standard deviation of consumption: Oxygen: {stand_oxygen:.2f}, Water: {stand_water:.2f}, Food: {stand_food:.2f}")
print(stand)