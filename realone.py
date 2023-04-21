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
def convert(x):
    number=x % 13 + 1
    if(number>10): return 10
    elif number==1: return 11
    else: return number
def points(a):
    su=sum(a)
    if len(a)==2: return su
    elif su>21:
        for i in range (0, len(a), 1):
            if a[i]==11:
                a[i]=1
        su=sum(a)
        return su
    else: return su
def deal_card(com):
    card = random.choice(poker)
    com.append(convert(card))
    poker.remove(card)
    return card
mastertotal=[]
playertotal=[]
master=[]  #存莊家手牌
player=[]  #存玩家手牌
'''shuffle(52)
cntmaster=[] #暫存，判斷點數
cntplayer=[] #暫存
cntmaster.append(poker[0])
cntmaster.append(poker[2])
master.append(getpoker(poker[0]))
master.append(getpoker(poker[2]))
master.append(getpoker(poker[3]))
player.append(getpoker(poker[1]))
mastertotal.append(convert(poker[0]))
mastertotal.append(convert(poker[2]))
mastertotal.append(convert(poker[3]))
print("莊家現在有:",master)
print("玩家現在有:",player)
#print(count(cntmaster))
print(cntmaster)
print(getpoker(poker[0]),"的點數是",convert(poker[0]))
print(points(mastertotal))'''
#先發兩張牌給玩家
for i in range(2):
    player.append(getpoker(deal_card(playertotal)))
    master.append(getpoker(deal_card(mastertotal)))
print(f"玩家的牌：{player}")
print(f"莊家的明牌：{master[1]}")
print(mastertotal)
print(playertotal)
answer=""
while answer != "n":
    answer=input('是否要加牌?(y/n)')
    if answer=="y":
        player.append(getpoker(deal_card(playertotal)))
        playerpoint=points(playertotal)
        #print("你目前的牌:",player)
        if playerpoint>21:
            #print("哈哈你輸了")
            answer="n"
        else: print("加牌後的手牌",player)
    elif answer == "n":
        playerpoint=points(playertotal)
        print(f"你的點數:{playerpoint}")
    else:
        print("請重新輸入！  是否要加牌?(y/n)")
        #算莊家的
    masterpoint=points(mastertotal)
    while masterpoint<17:
        master.append(getpoker(deal_card(mastertotal)))
        masterpoint=points(mastertotal)
print(f"玩家的牌：{player}，共{playerpoint}點")
print(f"莊家的牌：{master}，共{masterpoint}點")
if playerpoint>21:
    print("輸ㄌㄡ")
elif masterpoint>21:
    print("贏ㄌㄡ")
elif playerpoint==masterpoint:
    print("平手ㄌㄡ")
elif playerpoint>masterpoint:
    print("贏ㄌㄡ")
else: print("輸ㄌㄡ")

