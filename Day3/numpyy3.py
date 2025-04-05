import numpy as np

players=np.random.uniform(10,45,size=(5,10)).astype(int)
print(players)
avg_player=np.mean(players,axis=1)
print("Average points per game:")
print(avg_player )

max_val=np.sum(players,axis=1)
best_player=np.argmax(max_val)
worst_player=np.argmin(max_val)

print(f"\nBestperformance player:player{best_player+1}(total:{max_val[best_player]} points)")
print(f"\nworstperformance player:player{worst_player+1}(total:{max_val[worst_player]} points)")

print("\n Games with above score of 30")
for i,player_score in enumerate(players):
    high_score=np.where(player_score>30)[0]+1
    if high_score.size>0:
        print(f"player{i+1}:Games{list(high_score)}")
sortess=np.argsort(players)[::-1]
print("\n sorted values")
for rank,idx in enumerate(sortess,1):
    print(f"{rank}.player{idx+1}-{max_val[idx-1]} players")