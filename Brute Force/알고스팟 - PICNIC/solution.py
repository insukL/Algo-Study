def findFriendship(friends, friendship):
    if all(friendship):
        return 1
    
    idx = friendship.index(False)
    cnt = 0
    for i in range(idx + 1, len(friendship)):
        if not friendship[i] and friends[idx][i]:
            friendship[i], friendship[idx] = True, True
            cnt += findFriendship(friends, friendship)
            friendship[i], friendship[idx] = False, False
    
    return cnt

def run(n, m):
    friends = [[False for _ in range(n)] for _ in range(n)]
    friendship = [False for _ in range(n)]
    
    couple_list = list(map(int, input().split()))
    for i in range(0, m * 2, 2):
        a, b = couple_list[i], couple_list[i + 1]
        friends[a][b], friends[b][a] = True, True
    
    return findFriendship(friends, friendship)
    

def solution():
    tc = int(input())
    for _ in range(tc):
        n, m = map(int, input().split())
        print(run(n, m))
        
solution()
    