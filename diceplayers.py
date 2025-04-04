import random

li1=[1,2,3,4,5,6]
li2=[1,2,3,4,5,6]
li=[]
for i in li1:
    for j in li2:
        li.append((i,j))
print(li)
di={}       

for i in range(2,13):
    c=0
    for j in li:
        if i==j[0]+j[1]:
          c+=1
    
    prob=float(c/36)*100
    di[str(i)]=prob
print(di)

def player_1():
    a = random.randint(1, 6)  
    b = random.randint(1, 6)
    sum_roll = a + b
    return sum_roll  

def player_2():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    sum_roll = a + b
    return sum_roll  

def player_3(player_1_u, player_2_u):
    if player_1_u > player_2_u:
        print(f"Player 1 wins with score {player_1_u}")
    elif player_1_u < player_2_u:
        print(f"Player 2 wins with score {player_2_u}")
    else:
        print("The match is a draw")

# Simulating the game
def run_game(rounds):
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        player_1_u = player_1()
        player_2_u = player_2()

      
        print(f"Player 1 rolled: {player_1_u}")
        print(f"Player 2 rolled: {player_2_u}")
        
        
        result = player_3(player_1_u, player_2_u)
        print(result)


rounds = int(input("Enter the number of rounds you want to play: "))


run_game(rounds)