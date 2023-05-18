import random
n = 52
poker = [i for i in range(n)]

def shuffle(k):
    for i in range(52):
        p1 = random.randrange(0, k-1)
        p2 = random.randrange(0, k-1)
        poker[p1], poker[p2] = poker[p2], poker[p1]

def color(x):
    color = ['♣', '♦', '♥', '♠']
    c = x//13
    if c < 0 or c > 4:
        return 'Error'
    return color[c]

def value(x):
    value = x % 13 + 1
    if value == 1:
        return 'A'
    elif value >= 2 and value <= 10:
        return str(value)
    elif value == 11:
        return 'J'
    elif value == 12:
        return 'Q'
    elif value == 13:
        return 'K'

    
    
def getpoker(x):
    return color(x) + value(x) + ' '

def pleyerpoker(a, b):
    for i in range(a):
        for i in range(b):
            shuffle(52)
            getpoker(poker[0])
            del poker[0]
r=random.randrange(0, 51)
#print(getpoker(r))
player=[]
for i in range(13):
    r=random.randrange(0, 51)
    player.append(getpoker(r))
for j in range(13):
    print(player[j])

player_a=random.randrange(0, 51)
player_b=random.randrange(0, 51)   
def pick(a,b):
    print("player_a got:")
    print(getpoker(a))
    print("player_b got:")
    print(getpoker(b))
    if a>b:
        return 'player_a won'
    elif a<b:
        return 'player_a lost'
    else:
        return '平手'
print(pick(player_a,player_b))

print(poker)
shuffle(52)
print(poker)
for i in range (13):
    print(pick(poker[i],poker[i+1]))
    print("\n")
print()