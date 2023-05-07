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
    c = x%4
    return color[c]

def value(x):
    value = x // 4 + 1
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
def valuenumber(x):
    value = x // 4 + 1
    return value
    

def getpoker(x):
    return color(x) + value(x) + ' '
def deal_card():
    card = random.choice(poker)
    poker.remove(card)
    return card
def check(c):    #檢查是否有重複元素，避免重複輸入
        return len(c) != len(set(c))

 
def check2(c,b):
    standard = True
    for i in range(len(c)):
        if int(c[i]) > len(b) or int(c[i]) < 1 or len(c) < 1:
            standard = False
    return standard
'''def check3(c):
    if len(c) == 1:
        if c[0] == 'p':
            return True
        elif c[0].isdigit:
            print(c[0])
            print('result')
            return True
        else:
            return False
    else:    
        for i in range(len(c)):
            if ~c[i].isdigit():
                return False
        
        return True'''
    
 
#先發兩張牌給玩家

def main():
    class player:
        def __init__(self,name,poker,a):
            self.name=name
            self.poker=poker
            self.a = a
        def getcard(self, a,b): #b是暫存數字的list
            #print('getcard enter',a,b)
            for i in range(13):
                b.append(deal_card())
            b.sort()               #把b排好
            for i in range(13):
                a.append(getpoker(b[i]))       #把玩家手牌由小到大排好
            #playertotal.clear()
            #print('getcard exit',a,b)
            return a     
            
        def receive(self,b,c):
            c = input('請輸入牌型:(若要第一張 --> 1 第二張 --> 2 以此類推，中間以空格間隔)').split()
            #print(c)
            #print(len(c))
            if(len(c) != 0):             #避免玩家一直按enter
                if(c[0] == 'p'):
                    #print(c)
                    return c
            '''print(check3(c))
            while(check3(c) == False):
                print(check3(c))
                c = input('請重新輸入:').split()
            print('test')'''
            while ((len(c)!=1 and len(c)!=2 and len(c)!=5)  or (check(c) or not check2(c,b))) :         #避免玩家亂輸入
                c = input('請重新輸入:').split()
                #print(check3(c))
                #print((len(c)!=1 and len(c)!=2 and len(c)!=5))
                #print((check(c) or not check2(c,b)))
                if(len(c) != 0):
                    if(c[0] == 'p'):
                        #print(c)
                        return c
                #print(len(c))
            #print(c)
            #print(check(c))
            d=len(c)
            for i in range(d):
                #b.remove(b[c[i]])
                #c[i] = int(valuenumber(b[int(c[i])-1]))
                c[i] = int(b[int(c[i])-1])                      #把玩家輸入的位置找出來 以0-51表示
                #c.append(int(valuenumber(b[int(c[i])-1])))
            #print(c)
            return c
        
            

        def judge(self,c):       #a是儲存玩家輸入的數字的list    b是玩家牌
        #先傳入陣列(x[])
        #讀取陣列元素，長度 5 -> 鐵支 葫蘆 順子 2 -> 一對   1 -> 單張
        #判斷牌型
        #是否比前一個大
        #return牌型 ex:    33344,3葫蘆
        #輸入
            #print(c)
            #if(c[0] == 'p'):
                
                    
            c.sort()
            
            temp=[]
            for i in range(len(c)):
                temp.append(valuenumber(c[i]))           #轉成純數字(黑桃13 -->13  紅心A --> 1)
            if len(c)==1:
                return 2
            if len(c)==2:
                if temp[0]==temp[1]:
                    return 3
                else:
                    return -1
            else:
                if(temp[0] == temp[1] and temp[1] == temp[2] and temp[2] != temp[3] and temp[3] == temp[4]):
                    return 4
                elif(temp[0] == temp[1] and temp[1] != temp[2] and temp[2] == temp[3] and temp[3] == temp[4]):
                    return 5
                elif(temp[0] == temp[1] and temp[1] == temp[2] and temp[2] == temp[3] and temp[3] != temp[4]):
                    return 7
                elif(temp[0] != temp[1] and temp[1] == temp[2] and temp[2] == temp[3] and temp[3] == temp[4]):
                    return 8
                elif(temp[0] == 2 and temp[1] == 3 and temp[2] == 4 and temp[3] ==5 and temp[4] == 6):
                    return 10                              #----> 最大的順子 2 3 4 5 6
                elif(temp[-1] >= 5):
                    if(temp[1]-temp[0] == temp[2]-temp[1] and temp[3]-temp[2] == temp[2]-temp[1] and temp[4]-temp[3] == temp[3]-temp[2]):
                        return 6                                #1 2 3 4 5      ~   9 10 11 12 13 
                    elif(temp[0] == 1 and temp[1] == 10 and temp[2] == 11 and temp[3] == 12 and temp[4] == 13):
                        return 9                                #10 11 12 13 1
                    else:
                        return -1
                
                else :
                    return -1
        def compare(self,e,c,send,send2,b,a):  
            if(len(e) == 0):
                if send2 == -1:
                    return -1
                else:
                    for i in range(len(c)):
                        e.append(c[i])     
                player_2.delete(a,b,c,send2)
            elif(send == send2):
                if(send == 2):
                    if c[0] < 8 and e[0] >= 8:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #w = delete(a,b,c)
                    elif c[0] >= 8 and e[0] < 8:
                        return -1
                    elif c[0] > e[0]:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #w = delete(a,b,c)
                    else: return -1
                elif(send == -1):
                    return -1
                elif(send == 3):
                    if c[-1] < 8 and e[-1] > 8:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #w = delete(a,b,c)
                    elif c[-1] > 8 and e[-1] < 8:
                        return -1
                    elif c[-1] > e[-1]:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #delete(a,b,c)
                    else: return -1
                elif(send == 4):                       #前三張一樣
                    if c[0] < 8 and e[0] >= 8:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #w = delete(a,b,c)
                    elif c[0] >= 8 and e[0] < 8:
                        return -1
                    elif c[0] > e[0]:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #delete(a,b,c)
                    else: return -1
                elif(send == 5):                           #後三張一樣
                    if c[-1] < 8 and e[-1] > 8:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #w = delete(a,b,c)
                    elif c[-1] > 8 and e[-1] < 8:
                        return -1
                    if c[-1] > e[-1]:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #delete(a,b,c)
                    else: return -1
                elif (send == 6):                          #順子
                    if c[-1] < 8 and e[-1] > 8:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #w = delete(a,b,c)
                    elif c[-1] > 8 and e[-1] < 8:
                        return -1
                    elif(c[-1] > e[-1]):
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #delete(a,b,c)
                    else: return -1
                elif(send == 9):
                     
                    if c[0] > e[0]:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                             e[i] = c[i]
                        #delete(a,b,c)
                    else: return -1
                elif(send == 10):
                    
                    if c[0] > e[0]:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                             e[i] = c[i]
                        #delete(a,b,c)
                    else: return -1    
                elif (send == 7):                   #鐵支
                    if c[0] < 8 and e[0] >= 8:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #w = delete(a,b,c)
                    elif c[0] > 8 and e[0] < 8:
                        return -1
                    elif(c[0] > e[0]):
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #delete(a,b,c)
                    else: return -1
                elif (send == 8):
                    if c[-1] < 8 and e[-1] > 8:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #w = delete(a,b,c)
                    elif c[-1] > 8 and e[-1] < 8:
                        return -1
                    elif c[-1] > e[-1]:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #delete(a,b,c)
                    else: return -1
            elif(send2 == 7 or send2 ==8 and send !=7 and send !=8):
                player_2.delete(a,b,c,send2)
                e.clear()
                for i in range(len(c)):                       
                    e.append(c[i])
                    #delete(a,b,c)
            elif(send2 == 7 and send ==8):
                if c[0] < 8 and e[-1] >= 8:
                    player_2.delete(a,b,c,send2)
                    for i in range(len(c)):
                        e[i] = c[i]
                            #w = delete(a,b,c)
                elif c[0] > e[-1]:
                    player_2.delete(a,b,c,send2)
                    for i in range(len(c)):
                        e[i] = c[i]
                        #delete(a,b,c)
                else: return -1
            elif(send == 7 and send2 == 8):    #4-->前面三個一樣
                if c[-1] < 8 and e[0] >= 8:
                    player_2.delete(a,b,c,send2)
                    for i in range(len(c)):
                        e[i] = c[i]
                        #w = delete(a,b,c)
                elif c[-1] > e[0]:
                    player_2.delete(a,b,c,send2)
                    for i in range(len(c)):
                        e[i] = c[i]
                        #delete(a,b,c)
                else: return -1
            elif(send == 5 and send2 == 4):     #5-->後面三個一樣
                if c[0] < 8 and e[-1] >= 8:
                    player_2.delete(a,b,c,send2)
                    for i in range(len(c)):
                        e[i] = c[i]
                            #w = delete(a,b,c)
                elif c[0] > e[-1]:
                    player_2.delete(a,b,c,send2)
                    for i in range(len(c)):
                        e[i] = c[i]
                        #delete(a,b,c)
                else: return -1
            elif(send == 4 and send2 == 5):    #4-->前面三個一樣
                if c[-1] < 8 and e[0] >= 8:
                    player_2.delete(a,b,c,send2)
                    for i in range(len(c)):
                        e[i] = c[i]
                        #w = delete(a,b,c)
                elif c[-1] > e[0]:
                    player_2.delete(a,b,c,send2)
                    for i in range(len(c)):
                        e[i] = c[i]
                        #delete(a,b,c)
                else: return -1
            elif((send == 6  or send == 9 or send == 10) and (send2 == 9 or send2 == 10 or send2 ==6)):    #6-->前面三個一樣     
                if (send < send2):
                    player_2.delete(a,b,c,send2)
                    for i in range(len(c)):
                        e[i] = c[i]
                        #w = delete(a,b,c)
                else:
                    return -1
            else:
                return -1
        def delete(self,a,b,c,send2):
            #print(c)
            for i in range(len(c)):
                #print('b',b)
                #print('c',c)
                b.remove(c[i])
                #print('b after',b)
                #print('c after',c)
                #index = b.index(c[i])
                #print(index)
                #b.pop(index)
                
            a.clear()
            for i in range(len(b)):
                a.append(getpoker(b[i]))
            for i in range(len(c)):
                print(getpoker(c[i]),end='')
            if(send2 == 2):
                print('單張')
            elif(send2 == 3):
                print('一對')
            elif(send2 == 4 or send2 == 5):
                print('葫蘆')
            elif(send2 == 7 or send2 == 8):
                print('鐵支')
            elif(send2 == 6 or send2 ==9 or send2 == 10):
                print('順子')
            


    #print(e,'test')
    #lobal_e = e
    #print( global_e,'global_e')
    #return e
    playername=[]
    userinputarray=[]  #c
    userinputarray2 = []  #c
    userinputarray3=[]
    playertotal=[] #b
    player1total=[]  #b
    player2total=[]
    master=[]  #存莊家手牌
    player_1=[]  #存玩家手牌
    player_3=[]
    player_5=[]
    boss = 0
    status = 0
    returnvalue = 0
    returnvalue2 = 0
    returnvalue3 = 0

    #global global_e
    e=[] 
        
    a = input("請輸入名字:")
    player_2=player(a,poker,player_1)
    playername.append(a)
    
    
    b = input("請輸入名字:")
    while(b == a):
        print('該名字已被使用')
        b = input("請重新輸入名字:")
    playername.append(b)
    player_4=player(b,poker,player_3)

    c = input("請輸入名字:")
    while(c == a or c == b):
        print('該名字已被使用')
        c = input("請重新輸入名字:")
    playername.append(c)
    player_6=player(c,poker,player_5)
 
    print (player_2.name,"的牌:",player_2.getcard(player_1,playertotal))
    print (player_4.name,"的牌:",player_2.getcard(player_3,player1total))
    print (player_6.name,"的牌:",player_2.getcard(player_5,player2total))
    count = 0
    playerrecord = [0,0,0]   #0--> 有出牌     1--> pass
    playerrecord2 = [playertotal, player1total , player2total]
    #print(player1total[12])
    for i in range(13):
        #print(i)
        if playertotal[i] >= 8:
            boss = playertotal[i]
            status = 1
            break
    
    for i in range(13):
        if player1total[i] >= 8 and player1total[i] < boss:
            boss = player1total[i]
            status = 2
            break
    for i in range(13):
        if player2total[i] >= 8 and player2total[i] < boss:
            boss = player2total[i]
            status = 3
            break
    print(status,boss)
    if status ==  1:
        while len(player1total) !=0 and len(playertotal) !=0 and len(player2total) != 0 :
            
            print('player_1',a,player_1)
            print(a,'出牌')
            userinputarray = player_2.receive(playertotal,userinputarray)    #收第一位玩家訊息
            print('userinputarray',userinputarray)
            if (playerrecord[1] == 1 and playerrecord[2] == 1):                       #若第二位玩家的狀態為1 (pass) 則把狀態改回0 把e清空
                while(userinputarray[0] == 'p'):
                    print('你不能pass了,輪到你出牌!')
                    userinputarray = player_2.receive(playertotal,userinputarray)  
                playerrecord[1] = 0
                playerrecord[2] = 0
                e = []
                returnvalue = player_2.judge(userinputarray)
                #send值
                t = player_2.compare(e,userinputarray,returnvalue,returnvalue,playertotal,player_1)
                while (t == -1):
                    userinputarray = player_2.receive(playertotal,userinputarray)
                    while(userinputarray[0] == 'p'):
                        print('你不能pass了,輪到你出牌!')
                        userinputarray = player_2.receive(playertotal,userinputarray)  
                    returnvalue = player_2.judge(userinputarray)     #send值
                    t = player_2.compare(e,userinputarray,returnvalue,returnvalue,playertotal,player_1)
            
                print('e',e)
                print('player_1',a,player_1)
                if len(playertotal) == 1:
                    print('player_1',a,'只剩一張!!')
                elif len(playertotal) == 0:
                    break         
                       
            elif(playerrecord[2] == 1):              #若上一個玩家pass
                if (userinputarray[0] == 'p'):
                    playerrecord[0] = 1                         #把第二位玩家的狀態設為1
                    print(a,'pass!')
                else:
                    playerrecord[2] = 0
                    returnvalue = player_2.judge(userinputarray)
                    t = player_2.compare(e,userinputarray,returnvalue2,returnvalue,playertotal,player_1)
                    #print(t)
                    while (t == -1):
                        print('enter')
                        userinputarray = player_2.receive(playertotal,userinputarray)
                        if (userinputarray[0] == 'p'):
                                playerrecord[0] = 1                         #把第二位玩家的狀態設為1
                                print(a,'pass!') 
                                break
                                #print('hi')
                                #continue
                        else:
                            returnvalue = player_2.judge(userinputarray)     #send值
                            
                            #print('l')
                            t = player_2.compare(e,userinputarray,returnvalue2,returnvalue,playertotal,player_1)
                print('e',e)
                print('player_1',a,player_1)  
                if len(playertotal) == 1:
                    print('player_1',a,'只剩一張!!')
                elif len(playertotal) == 0:
                    break         
                       
            else:
                if count == 0:
                    print('第一',returnvalue3)
                    while(userinputarray[0] == 'p'):
                        print('你是第一個出牌的,不要pass啦!')
                        userinputarray = player_2.receive(playertotal,userinputarray)
                    returnvalue = player_2.judge(userinputarray)         #send值
                    t = player_2.compare(e,userinputarray,returnvalue,returnvalue,playertotal,player_1)
                    #print(t)
                    while (t == -1):
                        #print('enter')
                        userinputarray = player_2.receive(playertotal,userinputarray)
                        while(userinputarray[0] == 'p'):
                            print('你是第一個出牌的,不要pass啦!')
                            userinputarray = player_2.receive(playertotal,userinputarray)
                        
                        returnvalue = player_2.judge(userinputarray)     #send值
                        #print('l')
                        t = player_2.compare(e,userinputarray,returnvalue,returnvalue,playertotal,player_1)
                    count = 1
                elif (userinputarray[0] == 'p'):
                    #count += 1
                    playerrecord[0] = 1                         #把第一位玩家的狀態設為1
                    print(a,'pass!')
                    print('userinputarray',userinputarray)
               
                
                else:
                    print('後來',returnvalue3)
                    returnvalue = player_2.judge(userinputarray)         #send值
                    t = player_2.compare(e,userinputarray,returnvalue3,returnvalue,playertotal,player_1)
                    #print(t)
                    while (t == -1):
                        #print('enter')
                        userinputarray = player_2.receive(playertotal,userinputarray)
                        if (userinputarray[0] == 'p'):
                            playerrecord[0] = 1                         #把第一位玩家的狀態設為1
                            print(a,'pass!') 
                            break
                            #continue
                        else:
                            returnvalue = player_2.judge(userinputarray)     #send值
                            #print('l')
                            t = player_2.compare(e,userinputarray,returnvalue3,returnvalue,playertotal,player_1)
                
                print('e',e)                                         #檢查
                print('player_1',a,player_1)                         #剩下的手牌
                if len(playertotal) == 1:
                    print('player_1',a,'只剩一張!!')
                elif len(playertotal) == 0:
                    break         
                       
            print('player_3',b,player_3) 
            print(b,'出牌')
            userinputarray2 = player_2.receive(player1total,userinputarray2)   #收第二位玩家訊息
            if(playerrecord[0] == 1 and playerrecord[2] == 1):                       #若第一位玩家的狀態為1 (pass) 則把狀態改回0 把e清空
                while(userinputarray2[0] == 'p'):
                    print('你不能pass了,輪到你出牌!')
                    userinputarray2 = player_2.receive(player1total,userinputarray2) 
                playerrecord[0] = 0
                playerrecord[2] = 0
                e = []
                returnvalue2 = player_2.judge(userinputarray2)
                t = player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
                print(t)
                while (t == -1):
                    #print('enter')
                    userinputarray2 = player_2.receive(player1total,userinputarray2)
                    while(userinputarray2[0] == 'p'):
                        print('你不能pass了,輪到你出牌!')
                        userinputarray2 = player_2.receive(player1total,userinputarray2) 
                    returnvalue2 = player_2.judge(userinputarray2)     #send值
                        
                        #print('l')
                    t = player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
                print('e',e)
                print('player_3',b,player_3)        
                if len(player1total) == 1:
                    print('player_3',b,'只剩一張!!')
                elif len(player1total) == 0:
                    break         
                       
            elif(playerrecord[0] == 1):              #若上一個玩家pass
                if (userinputarray2[0] == 'p'):
                    playerrecord[1] = 1                         #把第二位玩家的狀態設為1
                    print(b,'pass!')
                else:
                    playerrecord[0] = 0
                    returnvalue2 = player_2.judge(userinputarray2)
                    t = player_2.compare(e,userinputarray2,returnvalue3,returnvalue2,player1total,player_3)
                    #print(t)
                    while (t == -1):
                        print('enter')
                        userinputarray2 = player_2.receive(player1total,userinputarray2)
                        if (userinputarray2[0] == 'p'):
                            playerrecord[1] = 1                         #把第二位玩家的狀態設為1
                            print(b,'pass!') 
                            break
                                #print('hi')
                                #continue
                        else:
                            returnvalue2 = player_2.judge(userinputarray2)     #send值
                            
                            #print('l')
                            t = player_2.compare(e,userinputarray2,returnvalue2,returnvalue3,player1total,player_3)
                print('e',e)
                print('player_3',b,player_3)         
                if len(player1total) == 1:
                    print('player_3',b,'只剩一張!!')
                elif len(player1total) == 0:
                    break 
                #continue
            else:
                if (userinputarray2[0] == 'p'):
                    playerrecord[1] = 1                         #把第二位玩家的狀態設為1
                    print(b,'pass!') 
                    #continue               
                else:
                    returnvalue2 = player_4.judge(userinputarray2)
                    t = player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
                    #print(t)
                    while (t == -1):
                        #print('enter')
                        userinputarray2 = player_2.receive(player1total,userinputarray2)
                        if (userinputarray2[0] == 'p'):
                            playerrecord[1] = 1                         #把第二位玩家的狀態設為1
                            print(b,'pass!') 
                            break
                            #continue
                        else:
                            returnvalue2 = player_2.judge(userinputarray2)     #send值
                        #print('l')
                            t = player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
                print('e',e)
                print('player_3',b,player_3)      
                if len(player1total) == 1:
                    print('player_3',b,'只剩一張!!')
                elif len(player1total) == 0:
                    break     
                        
            print('player_5',c,player_5) 
            print(c,'出牌')
            userinputarray3 = player_2.receive(player2total,userinputarray3)   #收第二位玩家訊息
            if(playerrecord[0] == 1 and playerrecord[1] == 1):                       #若第一位玩家的狀態為1 (pass) 則把狀態改回0 把e清空
                while(userinputarray3[0] == 'p'):
                    print('你不能pass了,輪到你出牌!')
                    userinputarray3 = player_2.receive(player2total,userinputarray3) 
                playerrecord[0] = 0
                playerrecord[1] = 0
                e = []
                returnvalue3 = player_2.judge(userinputarray3)
                t = player_2.compare(e,userinputarray3,returnvalue2,returnvalue3,player2total,player_5)
                print(t)
                while (t == -1):
                    #print('enter')
                    userinputarray3 = player_2.receive(player2total,userinputarray3)
                    while(userinputarray3[0] == 'p'):
                        print('你不能pass了,輪到你出牌!')
                        userinputarray3 = player_2.receive(player2total,userinputarray3) 
                       
                    returnvalue3 = player_2.judge(userinputarray3)     #send值
                        #print('l')
                    t = player_2.compare(e,userinputarray3,returnvalue2,returnvalue3,player2total,player_5)
                print('e',e)
                print('player_5',c,player_5)        
                if len(player2total) == 1:
                    print('player_5',c,'只剩一張!!')
                elif len(player2total) == 0:
                    break 
                
            elif(playerrecord[1] == 1):              #若上一個玩家pass
                if (userinputarray3[0] == 'p'):
                    playerrecord[2] = 1                         #把第二位玩家的狀態設為1
                    print(c,'pass!')
                else:
                    playerrecord[2] = 0
                    returnvalue3 = player_2.judge(userinputarray3)
                    t = player_2.compare(e,userinputarray3,returnvalue,returnvalue3,player2total,player_5)
                    #print(t)
                    while (t == -1):
                        print('enter')
                        userinputarray3 = player_2.receive(player2total,userinputarray3)
                        if (userinputarray3[0] == 'p'):
                                playerrecord[2] = 1                         #把第二位玩家的狀態設為1
                                print(c,'pass!') 
                                break
                                #print('hi')
                                #continue
                        else:
                            returnvalue3 = player_2.judge(userinputarray3)     #send值
                            
                            #print('l')
                            t = player_2.compare(e,userinputarray3,returnvalue,returnvalue3,player2total,player_5)
                print('e',e)
                print('player_5',c,player_5)  
                if len(player2total) == 1:
                    print('player_5',c,'只剩一張!!')
                elif len(player2total) == 0:
                    break
                #continue
            else:
                if (userinputarray3[0] == 'p'):
                    playerrecord[2] = 1                         #把第二位玩家的狀態設為1
                    print(c,'pass!') 
                    #continue               
                else:
                    returnvalue3 = player_2.judge(userinputarray3)
                    t = player_2.compare(e,userinputarray3,returnvalue2,returnvalue3,player2total,player_5)
                    #print(t)
                    while (t == -1):
                        #print('enter')
                        userinputarray3 = player_2.receive(player2total,userinputarray3)
                        if (userinputarray3[0] == 'p'):
                            playerrecord[2] = 1                         #把第三位玩家的狀態設為1
                            print(c,'pass!') 
                            break
                            #continue
                        else:
                            returnvalue3 = player_2.judge(userinputarray3)     #send值
                            #print('l')
                            t = player_2.compare(e,userinputarray3,returnvalue2,returnvalue3,player2total,player_5)
                print('e',e)
                print('player_5',c,player_5)
                if len(player2total) == 1:
                    print('player_5',c,'只剩一張!!')
                elif len(player2total) == 0:
                    break     
    elif status ==2:
        while len(player1total) !=0 and len(playertotal) !=0 and len(player2total) !=0 :
            
            print('player_3',b,player_3) 
            print(b,'出牌')
            userinputarray2 = player_2.receive(player1total,userinputarray2)   #收第二位玩家訊息
            if(playerrecord[0] == 1 and playerrecord[2] == 1):                       #若第一位玩家的狀態為1 (pass) 則把狀態改回0 把e清空
                while(userinputarray2[0] == 'p'):
                    print('你不能pass了,輪到你出牌!')
                    userinputarray2 = player_2.receive(player1total,userinputarray2) 
                playerrecord[0] = 0
                playerrecord[2] = 0
                e = []
                returnvalue2 = player_2.judge(userinputarray2)
                t = player_2.compare(e,userinputarray2,returnvalue2,returnvalue2,player1total,player_3)
                #print(t)
                while (t == -1):
                    print('enter')
                    userinputarray2 = player_2.receive(player1total,userinputarray2)
                    while(userinputarray2[0] == 'p'):
                        print('你不能pass了,輪到你出牌!')
                        userinputarray2 = player_2.receive(player1total,userinputarray2)
                    
                    returnvalue2 = player_2.judge(userinputarray2)     #send值  
                        #print('l')
                    t = player_2.compare(e,userinputarray2,returnvalue2,returnvalue2,player1total,player_3)
                print('e',e)
                print('player_3',b,player_3)          
            elif(playerrecord[0] == 1):              #若上一個玩家pass
                if (userinputarray2[0] == 'p'):
                    playerrecord[1] = 1                         #把第二位玩家的狀態設為1
                    print(b,'pass!')
                else:
                    playerrecord[0] = 0
                    returnvalue2 = player_2.judge(userinputarray2)
                    t = player_2.compare(e,userinputarray2,returnvalue3,returnvalue2,player1total,player_3)
                    #print(t)
                    while (t == -1):
                        print('enter')
                        userinputarray2 = player_2.receive(player1total,userinputarray2)
                        if (userinputarray2[0] == 'p'):
                                playerrecord[1] = 1                         #把第二位玩家的狀態設為1
                                print(b,'pass!') 
                                break
                                #print('hi')
                                #continue
                        else:
                            returnvalue2 = player_2.judge(userinputarray2)     #send值
                            
                            #print('l')
                            t = player_2.compare(e,userinputarray2,returnvalue2,returnvalue3,player1total,player_3)
                print('e',e)
                print('player_3',b,player_3)     
        
                #continue
            else:
                if (count == 0):
                    while(userinputarray2[0] == 'p'):
                        print('你是第一個出牌的,不要pass啦!')
                        userinputarray2 = player_2.receive(player1total,userinputarray2)
                    returnvalue2 = player_2.judge(userinputarray2)
                    print(returnvalue2)
                    t = player_2.compare(e,userinputarray2,returnvalue2,returnvalue2,player1total,player_3)
                    print('b',t)
                    while (t == -1):
                        print(t)
                        userinputarray2 = player_2.receive(player1total,userinputarray2)
                        while(userinputarray2[0] == 'p'):
                            print('你是第一個出牌的,不要pass啦!')
                            userinputarray2 = player_2.receive(player1total,userinputarray2)
                        returnvalue2 = player_2.judge(userinputarray2)     #send值
                        #print('l')
                        t = player_2.compare(e,userinputarray2,returnvalue2,returnvalue2,player1total,player_3)
                    count = 1      
                elif(userinputarray2[0] == 'p'):                 #第二位玩家pass
                    playerrecord[1] = 1                         #把第二位玩家的狀態設為1
                    print(b,'pass!') 
                    #continue     
                else:
                    returnvalue2 = player_2.judge(userinputarray2)
                    print(returnvalue2)
                    t = player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
                    print('b',t)
                    while (t == -1):
                        print(t)
                        userinputarray2 = player_2.receive(player1total,userinputarray2)
                        if (userinputarray2[0] == 'p'):
                            playerrecord[1] = 1                         #把第二位玩家的狀態設為1
                            print(b,'pass!') 
                            break
                            #continue
                        else:
                            returnvalue2 = player_2.judge(userinputarray2)     #send值
                        #print('l')
                            t = player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
            print('e',e)
            print('player_3',b,player_3)         
            
            
            
            print('player_5',c,player_5) 
            print(c,'出牌')
            userinputarray3 = player_2.receive(player2total,userinputarray3)   #收第二位玩家訊息
            if(playerrecord[0] == 1 and playerrecord[1] == 1):                       #若第一位玩家的狀態為1 (pass) 則把狀態改回0 把e清空
                while(userinputarray3[0] == 'p'):
                    print('你不能pass了,輪到你出牌!')
                    userinputarray3 = player_2.receive(player2total,userinputarray3) 
                playerrecord[0] = 0
                playerrecord[1] = 0
                e = []
                returnvalue3 = player_2.judge(userinputarray3)
                t = player_2.compare(e,userinputarray3,returnvalue2,returnvalue3,player2total,player_5)
                #print(t)
                while (t == -1):
                    #print('enter')
                    userinputarray3 = player_2.receive(player2total,userinputarray3)
                    while(userinputarray3[0] == 'p'):
                        print('你不能pass了,輪到你出牌!')
                        userinputarray3 = player_2.receive(player2total,userinputarray3)
                    
                    returnvalue3 = player_2.judge(userinputarray3)     #send值
                    #print('l')
                    t = player_2.compare(e,userinputarray3,returnvalue2,returnvalue3,player2total,player_5)
                print('e',e)
                print('player_5',c,player_5)            
                
            elif(playerrecord[1] == 1):              #若上一個玩家pass
                if (userinputarray3[0] == 'p'):
                    playerrecord[2] = 1                         #把第二位玩家的狀態設為1
                    print(c,'pass!')
                else:
                    playerrecord[2] = 0
                    returnvalue3 = player_2.judge(userinputarray3)
                    t = player_2.compare(e,userinputarray3,returnvalue,returnvalue3,player2total,player_5)
                    #print(t)
                    while (t == -1):
                        print('enter')
                        userinputarray3 = player_2.receive(player2total,userinputarray3)
                        if (userinputarray3[0] == 'p'):
                                playerrecord[2] = 1                         #把第二位玩家的狀態設為1
                                print(c,'pass!') 
                                break
                                #print('hi')
                                #continue
                        else:
                            returnvalue3 = player_2.judge(userinputarray3)     #send值
                            
                            #print('l')
                            t = player_2.compare(e,userinputarray3,returnvalue,returnvalue3,player2total,player_5)
                print('e',e)
                print('player_5',a,player_5)  
             
        
                #continue
            else:
                if (userinputarray3[0] == 'p'):
                    playerrecord[2] = 1                         #把第二位玩家的狀態設為1
                    print(c,'pass!') 
                    #continue               
                else:
                    returnvalue3 = player_2.judge(userinputarray3)
                    t = player_2.compare(e,userinputarray3,returnvalue2,returnvalue3,player2total,player_5)
                    print(t)
                    while (t == -1):
                        #print('enter')
                        userinputarray3 = player_2.receive(player2total,userinputarray3)
                        if (userinputarray3[0] == 'p'):
                            playerrecord[2] = 1                         #把第三位玩家的狀態設為1
                            print(c,'pass!') 
                            break
                            #continue
                        else:
                            returnvalue3 = player_2.judge(userinputarray3)     #send值
                            #print('l')
                            t = player_2.compare(e,userinputarray3,returnvalue2,returnvalue3,player2total,player_5)
                    print('e',e)
                    print('player_5',c,player_5)
            
            
            print('player_1',a,player_1)
            print(a,'出牌')
            userinputarray = player_2.receive(playertotal,userinputarray)    #收第一位玩家訊息
            print('userinputarray',userinputarray)
            if(playerrecord[1] == 1 and playerrecord[2] == 1):                       #若第二位玩家的狀態為1 (pass) 則把狀態改回0 把e清空
                while(userinputarray[0] == 'p'):
                    print('你不能pass了,輪到你出牌!')
                    userinputarray = player_2.receive(playertotal,userinputarray)  
                playerrecord[1] = 0
                playerrecord[2] = 0
                e = []
                returnvalue = player_2.judge(userinputarray)
                                                                            #send值
                t = player_2.compare(e,userinputarray,returnvalue3,returnvalue,playertotal,player_1)
                while (t == -1):
                    userinputarray = player_2.receive(playertotal,userinputarray)
                    while(userinputarray[0] == 'p'):
                        print('你不能pass了,輪到你出牌!')
                        userinputarray = player_2.receive(playertotal,userinputarray)
                    
                    returnvalue = player_2.judge(userinputarray)     #send值
                    t = player_2.compare(e,userinputarray,returnvalue3,returnvalue,playertotal,player_1)
            
                print('e',e)
                print('player_1',a,player_1)    
                             
            elif(playerrecord[2] == 1):              #若上一個玩家pass
                if (userinputarray[0] == 'p'):
                    playerrecord[0] = 1                         #把第二位玩家的狀態設為1
                    print(a,'pass!')
                else:
                    playerrecord[2] = 0
                    returnvalue = player_2.judge(userinputarray)
                    t = player_2.compare(e,userinputarray,returnvalue2,returnvalue,playertotal,player_1)
                    #print(t)
                    while (t == -1):
                        print('enter')
                        userinputarray = player_2.receive(playertotal,userinputarray)
                        if (userinputarray[0] == 'p'):
                                playerrecord[0] = 1                         #把第二位玩家的狀態設為1
                                print(a,'pass!') 
                                break
                                #print('hi')
                                #continue
                        else:
                            returnvalue = player_2.judge(userinputarray)     #send值
                            
                            #print('l')
                            t = player_2.compare(e,userinputarray,returnvalue2,returnvalue,playertotal,player_1)
                print('e',e)
                print('player_1',a,player_1)  
        
            else:
                if (userinputarray[0] == 'p'):
                    #count += 1
                    playerrecord[0] = 1                         #把第一位玩家的狀態設為1
                    print(a,'pass!')
                    print('userinputarray',userinputarray)
                else:
                    returnvalue = player_2.judge(userinputarray)         #send值
                    t = player_2.compare(e,userinputarray,returnvalue3,returnvalue,playertotal,player_1)
                    print(t)
                    while (t == -1):
                        #print('enter')
                        userinputarray = player_2.receive(playertotal,userinputarray)
                        if (userinputarray[0] == 'p'):
                            playerrecord[0] = 1                         #把第一位玩家的狀態設為1
                            print(a,'pass!') 
                            break
                            #continue
                        else:
                            returnvalue = player_2.judge(userinputarray)     #send值
                            #print('l')
                            t = player_2.compare(e,userinputarray,returnvalue3,returnvalue,playertotal,player_1)
                
                print('e',e)                                         #檢查
                print('player_1',a,player_1)                         #剩下的手牌
                
    else:
        while len(player1total) !=0 and len(playertotal) !=0 and len(player2total) != 0 :
            
                        
            print('player_5',c,player_5) 
            print(c,'出牌')
            userinputarray3 = player_2.receive(player2total,userinputarray3)   #收第二位玩家訊息
            if(playerrecord[0] == 1 and playerrecord[1] == 1):                       #若第一位玩家的狀態為1 (pass) 則把狀態改回0 把e清空
                while(userinputarray3[0] == 'p'):
                    print('你不能pass了,輪到你出牌!')
                    userinputarray3 = player_2.receive(player2total,userinputarray3) 
                playerrecord[0] = 0
                playerrecord[1] = 0
                e = []
                returnvalue3 = player_2.judge(userinputarray3)
                t = player_2.compare(e,userinputarray3,returnvalue3,returnvalue3,player2total,player_5)
                print(t)
                while (t == -1):
                    #print('enter')
                    userinputarray3 = player_2.receive(player2total,userinputarray3)
                    while(userinputarray3[0] == 'p'):
                        print('你不能pass了,輪到你出牌!')
                        userinputarray3 = player_2.receive(player2total,userinputarray3)
                    
                    returnvalue3 = player_2.judge(userinputarray3)     #send值
                    #print('l')
                    t = player_2.compare(e,userinputarray3,returnvalue3,returnvalue3,player2total,player_5)
                print('e',e)
                print('player_5',c,player_5)      
                           
            elif(playerrecord[1] == 1):              #若上一個玩家pass
                if (userinputarray3[0] == 'p'):
                    playerrecord[2] = 1                         #把第二位玩家的狀態設為1
                    print(c,'pass!')
                else:
                    playerrecord[2] = 0
                    returnvalue3 = player_2.judge(userinputarray3)
                    t = player_2.compare(e,userinputarray3,returnvalue,returnvalue3,player2total,player_5)
                    #print(t)
                    while (t == -1):
                        print('enter')
                        userinputarray3 = player_2.receive(player2total,userinputarray3)
                        if (userinputarray3[0] == 'p'):
                                playerrecord[2] = 1                         #把第二位玩家的狀態設為1
                                print(c,'pass!') 
                                break
                                #print('hi')
                                #continue
                        else:
                            returnvalue3 = player_2.judge(userinputarray3)     #send值
                            
                            #print('l')
                            t = player_2.compare(e,userinputarray3,returnvalue,returnvalue3,player2total,player_5)
                print('e',e)
                print('player_5',a,player_5)  
        
                #continue
            else:
                if (count == 0):
                    while(userinputarray3[0] == 'p'):
                        print('你是第一個出牌的,不要pass啦!')
                        userinputarray3 = player_2.receive(player2total,userinputarray3)
                    returnvalue3 = player_2.judge(userinputarray3)
                    t = player_2.compare(e,userinputarray3,returnvalue3,returnvalue3,player2total,player_5)
                    print(t)
                    while (t == -1):
                        #print('enter')
                        userinputarray3 = player_2.receive(player2total,userinputarray3)
                        while(userinputarray3[0] == 'p'):
                            print('你是第一個出牌的,不要pass啦!')
                            userinputarray3 = player_2.receive(player2total,userinputarray3)
                         
                         
                        returnvalue3 = player_2.judge(userinputarray3)     #send值
                        #print('l')
                        t = player_2.compare(e,userinputarray3,returnvalue3,returnvalue3,player2total,player_5)
                    count = 1           
                elif (userinputarray3[0] == 'p'):
                    playerrecord[2] = 1                         #把第二位玩家的狀態設為1
                    print(c,'pass!') 
                    #continue     
                else:
                    returnvalue3 = player_2.judge(userinputarray3)
                    t = player_2.compare(e,userinputarray3,returnvalue2,returnvalue3,player2total,player_5)
                    print(t)
                    while (t == -1):
                        #print('enter')
                        userinputarray3 = player_2.receive(player2total,userinputarray3)
                        if (userinputarray3[0] == 'p'):
                            playerrecord[2] = 1                         #把第三位玩家的狀態設為1
                            print(c,'pass!') 
                            break
                            #continue
                        else:
                            returnvalue3 = player_2.judge(userinputarray3)     #send值
                            #print('l')
                            t = player_2.compare(e,userinputarray3,returnvalue2,returnvalue3,player2total,player_5)
            print('e',e)
            print('player_5',c,player_5)  
            
            
            
            
            
            print('player_1',a,player_1)
            print(a,'出牌')
            userinputarray = player_2.receive(playertotal,userinputarray)    #收第一位玩家訊息
            print('userinputarray',userinputarray)
            if(playerrecord[1] == 1 and playerrecord[2] == 1):                       #若第二位玩家的狀態為1 (pass) 則把狀態改回0 把e清空
                while(userinputarray[0] == 'p'):
                    print('你不能pass了,輪到你出牌!')
                    userinputarray = player_2.receive(playertotal,userinputarray)  
                playerrecord[1] = 0
                playerrecord[2] = 0
                e = []
                returnvalue = player_2.judge(userinputarray)       #send值
                while (player_2.compare(e,userinputarray,returnvalue3,returnvalue,playertotal,player_1) == -1):
                    userinputarray = player_2.receive(playertotal,userinputarray)
                    while(userinputarray[0] == 'p'):
                        print('你不能pass了,輪到你出牌!')
                        userinputarray = player_2.receive(playertotal,userinputarray)
                    
                    returnvalue = player_2.judge(userinputarray)     #send值
                    player_2.compare(e,userinputarray,returnvalue3,returnvalue,playertotal,player_1)
            
                print('e',e)
                print('player_1',a,player_1)      
            
            elif(playerrecord[2] == 1):              #若上一個玩家pass
                if (userinputarray[0] == 'p'):
                    playerrecord[0] = 1                         #把第二位玩家的狀態設為1
                    print(a,'pass!')
                else:
                    playerrecord[2] = 0
                    returnvalue = player_2.judge(userinputarray)
                    t = player_2.compare(e,userinputarray,returnvalue2,returnvalue,playertotal,player_1)
                    #print(t)
                    while (t == -1):
                        print('enter')
                        userinputarray = player_2.receive(playertotal,userinputarray)
                        if (userinputarray[0] == 'p'):
                                playerrecord[0] = 1                         #把第二位玩家的狀態設為1
                                print(a,'pass!') 
                                break
                                #print('hi')
                                #continue
                        else:
                            returnvalue = player_2.judge(userinputarray)     #send值
                            
                            #print('l')
                            t = player_2.compare(e,userinputarray,returnvalue2,returnvalue,playertotal,player_1)
                print('e',e)
                print('player_1',a,player_1)  
                   
        
            else:
                if (userinputarray[0] == 'p'):
                    #count += 1
                    playerrecord[0] = 1                         #把第一位玩家的狀態設為1
                    print(a,'pass!')
                    print('userinputarray',userinputarray)
                else:
                    returnvalue = player_2.judge(userinputarray)         #send值
                    t = player_2.compare(e,userinputarray,returnvalue3,returnvalue,playertotal,player_1)
                    print(t)
                    while (t == -1):
                        #print('enter')
                        userinputarray = player_2.receive(playertotal,userinputarray)
                        if (userinputarray[0] == 'p'):
                            playerrecord[0] = 1                         #把第一位玩家的狀態設為1
                            print(a,'pass!') 
                            break
                            #continue
                        else:
                            returnvalue = player_2.judge(userinputarray)     #send值
                            #print('l')
                            t = player_2.compare(e,userinputarray,returnvalue3,returnvalue,playertotal,player_1)
                    
                print('e',e)                                         #檢查
                print('player_1',a,player_1)                         #剩下的手牌
                
            print('player_3',b,player_3) 
            print(b,'出牌')
            userinputarray2 = player_2.receive(player1total,userinputarray2)   #收第二位玩家訊息
            if(playerrecord[0] == 1 and playerrecord[2] == 1):                       #若第一位玩家的狀態為1 (pass) 則把狀態改回0 把e清空
                while(userinputarray2[0] == 'p'):
                    print('你不能pass了,輪到你出牌!')
                    userinputarray2 = player_2.receive(player1total,userinputarray2) 
                playerrecord[0] = 0
                playerrecord[2] = 0
                e = []
                returnvalue2 = player_2.judge(userinputarray2)
                t = player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
                print(t)
                while (t == -1):
                    #print('enter')
                    userinputarray2 = player_2.receive(player1total,userinputarray2)
                    while(userinputarray2[0] == 'p'):
                        print('你不能pass了,輪到你出牌!')
                        userinputarray2 = player_2.receive(player1total,userinputarray2)
                    
                    returnvalue2 = player_2.judge(userinputarray2)     #send值
                    #print('l')
                    t = player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
                print('e',e)
                print('player_3',b,player_3)             
                
            elif(playerrecord[0] == 1):              #若上一個玩家pass
                if (userinputarray2[0] == 'p'):
                    playerrecord[1] = 1                         #把第二位玩家的狀態設為1
                    print(b,'pass!')
                else:
                    playerrecord[0] = 0
                    returnvalue2 = player_2.judge(userinputarray2)
                    t = player_2.compare(e,userinputarray2,returnvalue3,returnvalue2,player1total,player_3)
                    #print(t)
                    while (t == -1):
                        print('enter')
                        userinputarray2 = player_2.receive(player1total,userinputarray2)
                        if (userinputarray2[0] == 'p'):
                                playerrecord[1] = 1                         #把第二位玩家的狀態設為1
                                print(b,'pass!') 
                                break
                                #print('hi')
                                #continue
                        else:
                            returnvalue2 = player_2.judge(userinputarray2)     #send值
                            
                            #print('l')
                            t = player_2.compare(e,userinputarray2,returnvalue2,returnvalue3,player1total,player_3)
                print('e',e)
                print('player_3',b,player_3)         
            
        
                #continue
            else:
                if (userinputarray2[0] == 'p'):
                    playerrecord[1] = 1                         #把第二位玩家的狀態設為1
                    print(b,'pass!') 
                    #continue  8             
                else:
                    returnvalue2 = player_4.judge(userinputarray2)
                    t = player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
                    print(t)
                    while (t == -1):
                        #print('enter')
                        userinputarray2 = player_2.receive(player1total,userinputarray2)
                        if (userinputarray2[0] == 'p'):
                            playerrecord[1] = 1                         #把第二位玩家的狀態設為1
                            print(b,'pass!') 
                            break
                            #continue
                        else:
                            returnvalue2 = player_2.judge(userinputarray2)     #send值
                        #print('l')
                            t = player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
                    print('e',e)
                    print('player_3',b,player_3)          
                   
    if len(playertotal) == 0:
        print(a,'win!')
    elif len(player1total) == 0:    
        print(b,'win!')
    else:
        print(c,'win!')
main()    