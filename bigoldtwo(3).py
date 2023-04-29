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

'''def color(x):
    color = ['♣', '♦', '♥', '♠']
    c = x//13
    if c < 0 or c > 4:
        return 'Error'
    return color[c]
'''
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

'''def check2(c):
    standard = True
    for i in range(len(c)):
        if int(c[i]) > 13 or int(c[i]) < 1:
            standard = False
    return standard
    '''
def check2(c,b):
    standard = True
    for i in range(len(c)):
        if int(c[i]) > len(b) or int(c[i]) < 1:
            standard = False
    return standard
'''def delete(a,b,c):
        print(c)
        for i in range(len(c)):
            #b.remove(c[i])
            print(b)
            print(c)
            index = b.index(c[i])
            print(index)
            b.pop(index)
        a.clear()
        for i in range(len(b)):
            a.append(getpoker(b[i]))
        return a,b
    '''
'''
   e:上一個人的牌 c:傳進來的(現在玩家)(0-51) 
   send:  上一個玩家的judge return 值
   send2: 現在玩家的judge return 值
   b:存玩家手牌(0-51)
   a:玩家手牌(花色)
'''     
'''def compare(e,c,send,send2,b,a):  
    if(len(e) == 0):
        for i in range(len(c)):
            e.append(c[i])     
    
    elif(send == send2):
        if(send == 2):
            if c[0] > e[0]:
                 
                w = delete(a,b,c)
            else: return -1
        elif(send == 3):
            if c[-1] > e[-1]:
                delete(a,b,c)
            else: return -1
        elif(send == 4):
            if c[0] > e[0]:
                delete(a,b,c)
            else: return -1
        elif(send == 5):
            if c[-1] > e[-1]:
                delete(a,b,c)
            else: return -1
        elif (send == 6):
            if(valuenumber(c[0]) == 1 and valuenumber(e[0]) == 1):
                if c[0] > e[0]:
                    delete(a,b,c)
                else: return -1
            elif(c[-1] > e[-1]):
                delete(a,b,c)
            else: return -1
        elif (send == 7):
            if(c[0] > e[0]):
                delete(a,b,c)
            else: return -1
        elif (send == 8):
            if c[-1] > e[-1]:
                delete(a,b,c)
            else: return -1
    elif(send2 == 7 and send !=7):
        delete(a,b,c)
    else:
        return -1
    print(e,'test')
    global_e = e
    print( global_e,'global_e')
    #return e'''
        
'''def game(c,f):
    d=[]
    if(f=='順子'):
   '''     

#先發兩張牌給玩家
'''for i in range(13):
    player_1.append(getpoker(deal_card(playertotal)))
    master.append(getpoker(deal_card(mastertotal)))
    '''
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
            if(c[0] == 'p'):
                #print(c)
                return c
            while ((len(c)!=1 and len(c)!=2 and len(c)!=5) or(check(c) or not check2(c,b))) :
                c = input('請重新輸入:').split()
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
                c[i] = int(b[int(c[i])-1])
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
            '''if len(c)==1:
                return ('你選了',c[0],'一張')
            if len(c)==2:
                if c[0]==c[1]:
                    return ('你選了',c[0],'一對')
                else:
                    return -1
            else:
                if(c[0] == c[1] and c[1] == c[2] and c[2] != c[3] and c[3] == c[4]):
                    return ('你選了',c[0],'葫蘆')
                elif(c[0] == c[1] and c[1] != c[2] and c[2] == c[3] and c[3] == c[4]):
                    return ('你選了',c[2],'葫蘆')
                elif(c[0] == c[1] and c[1] == c[2] and c[2] == c[3] and c[3] != c[4]):
                    return ('你選了',c[0],'鐵支')
                elif(c[1]-c[0] == c[2]-c[1] and c[3]-c[2] == c[2]-c[1] and c[4]-c[3] == c[3]-c[2]):
                    return ('你選了','順子')
                else :
                    return -1             '''
            temp=[]
            for i in range(len(c)):
                temp.append(valuenumber(c[i]))
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
                elif(temp[-1] >= 6):
                    if(temp[1]-temp[0] == temp[2]-temp[1] and temp[3]-temp[2] == temp[2]-temp[1] and temp[4]-temp[3] == temp[3]-temp[2]):
                        return 6
                    elif(temp[0] == 1):
                        temp[0] == 9
                        if(temp[1]-temp[0] == temp[2]-temp[1] and temp[3]-temp[2] == temp[2]-temp[1] and temp[4]-temp[3] == temp[3]-temp[2]):
                            return 9
                    else:
                        return -1
                
                else :
                    return -1
        def compare(self,e,c,send,send2,b,a):  
            if(len(e) == 0):
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
                elif(send == 4):
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
                elif(send == 5):
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
                    if(valuenumber(c[0]) == 1 and valuenumber(e[0]) == 1):
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
                elif(send2 == 7 and send !=7):
                    player_2.delete(a,b,c,send2)
                    e.clear()
                    for i in range(len(c)):
                        e.append(c[i])
                    #delete(a,b,c)
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
                elif(send == 4 and send2 == 5):    #4-->前面三個一樣
                    if c[-1] < 8 and e[0] >= 8:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #w = delete(a,b,c)
                    if c[-1] > e[0]:
                        player_2.delete(a,b,c,send2)
                        for i in range(len(c)):
                            e[i] = c[i]
                        #delete(a,b,c)
            else:
                return -1
        def delete(self,a,b,c,send2):
            #print(c)
            for i in range(len(c)):
                print('b',b)
                print('c',c)
                b.remove(c[i])
                print('b after',b)
                print('c after',c)
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
            elif(send2 == 6):
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
    #global global_e
    e=[] 
        
    a = input("請輸入名字:")
    player_2=player(a,poker,player_1)
    playername.append(a)
    #print (player_2.name,"的牌:",player_2.getcard(player_1,playertotal))
    #print('playertotal',playertotal)
    #print('player_1',player_1)
    #userinputarray = player_2.receive(playertotal,userinputarray)
    #returnvalue = player_2.judge(userinputarray)     #send值
    #player_2.compare(e,userinputarray,returnvalue,returnvalue,playertotal,player_1)
    #print('player_1',player_1)
    b = input("請輸入名字:")
    playername.append(b)
    player_4=player(b,poker,player_3)

    c = input("請輸入名字:")
    playername.append(c)
    player_6=player(c,poker,player_5)

    #print (player_4.name,"的牌:",player_4.getcard(player_3,player1total))
    '''b = input("請輸入名字:")player_4=player(b,poker,player_3)
    print (player_4.name,"的牌:",player_4.getcard(player_3,player1total))
    c = input("請輸入名字:")
    player_6=player(c,poker,player_5)
    print (player_6.name,"的牌:",player_6.getcard(player_5,player2total))
    answer = -1'''

    #print(player_2.receive(playertotal,userinputarray))

    #userinputarray2 = player_4.receive(player1total,userinputarray2)
    #print(userinputarray,'測試')
    '''while True:
        if(player_2.judge(userinputarray) != -1):
            print(player_2.judge(userinputarray))
            break
        else:
            while player_2.judge(userinputarray) == -1:
                print('Oh no!沒有這樣的牌型')
                userinputarray = player_2.receive(playertotal,userinputarray)
                '''

    #returnvalue2 = player_4.judge(userinputarray2)   #send2值
    #print(player1total,'')
    #print(userinputarray2,'')

    #player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
    #print('player_3',player_3)
    #userinputarray = player_2.receive(playertotal,userinputarray)
    #returnvalue = player_2.judge(userinputarray)     #send值
    #player_2.compare(e,userinputarray,returnvalue,returnvalue,playertotal,player_1)
    #print('e',e)

    #w = delete(player_1,player1total,userinputarray2)
    #print(w)
    #print('player_1',player_1)
    #print('player1total',player1total)
    #print('userinputarray2',userinputarray2)



    '''while True:
        if(player_2.judge(userinputarray) != -1):
            player_2.judge(userinputarray)
            break
        else:
            while player_2.judge(userinputarray) == -1:
                print('Oh no!沒有這樣的牌型')
                userinputarray = player_2.receive(playertotal,userinputarray)'''
    #print(returnvalue)
    #while player_2.judge(player_2.receive(playertotal,userinputarray))
    '''while player_2.judge(userinputarray) == -1:
        print(player_2.receive(playertotal,userinputarray))
        #print()'''
        
    '''處存上一個人的
        判斷大小
        單張用b判斷
        兩張用b判斷
        葫蘆用三張的c判斷   2>1>13>12>11.....
        鐵支用四張的c判斷   2>1>13>12>11.....
        順子用    最後一張為A--->最大  若一樣則比b
                
        前提: 張數不一樣 return -1
        例外 鐵支 桐花順
        手牌更新 a b print
        
    
    
    
    
    
宣告一個空陣列e   暫存上一個玩家出的牌
compare(e,c):
如果 len(e) == 0  --> c就進去e  
     len(e) != 0  --> c要跟e比大小
                            if(c>e) --> e要改成c 且玩家減掉手牌 return e
                              (c<e) --> return 錯誤 並重新輸入牌型 或 pass
                            compare():
                              
while 玩家手牌 != 0                             
    for i in range (玩家) :
        if(count == 3) :(前面三個人都pass)
            可以隨便出
            count = 0(歸零)
            e[] = 0 (歸零)
            continue
        玩家[i] 出牌
        if 玩家[i] = pass
            count++
            continue       
        else:
            if compare(玩家[i]) return 錯誤:
                叫他重輸入
            else:
                把 return 的牌給下個玩家看
                              
                              
                              
                              
                              '''
    print (player_2.name,"的牌:",player_2.getcard(player_1,playertotal))
    print (player_4.name,"的牌:",player_2.getcard(player_3,player1total))
    print (player_6.name,"的牌:",player_2.getcard(player_5,player2total))
    count = 0
    playerrecord = [0,0,0]   #0--> 有出牌     1--> pass
    while len(player1total) !=0 or len(playertotal) !=0 :

        print(a,'出牌')
        userinputarray = player_2.receive(playertotal,userinputarray)    #收第一位玩家訊息
        print('userinputarray',userinputarray)
        if(playerrecord[1] == 1 and playerrecord[2] == 0):                       #若第二位玩家的狀態為1 (pass) 則把狀態改回0 把e清空
            while(userinputarray[0] == 'p'):
                print('你不能pass了,輪到你出牌!')
                userinputarray = player_2.receive(playertotal,userinputarray)  
            playerrecord[1] = 0
            playerrecord[2] = 0
            e = []
            returnvalue = player_2.judge(userinputarray)
            '''t = player_2.compare(e,userinputarray,returnvalue,returnvalue2,player1total,player_3)
            print(t)
            while (t == -1):
                #print('enter')
                userinputarray = player_2.receive(playertotal,userinputarray)
                returnvalue2 = player_2.judge(userinputarray2)     #send值
                #print('l')
                t = player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
                returnvalue = player_2.judge(userinputarray)         '''#send值
            while (player_2.compare(e,userinputarray,returnvalue,returnvalue,playertotal,player_1) == -1):
                userinputarray = player_2.receive(playertotal,userinputarray)
                returnvalue = player_2.judge(userinputarray)     #send值
                player_2.compare(e,userinputarray,returnvalue,returnvalue,playertotal,player_1)
         
            print('e',e)
            print('player_1',b,player_1)                 
       
        else:
            if (userinputarray[0] == 'p'):
                #count += 1
                playerrecord[0] = 1                         #把第一位玩家的狀態設為1
                print(a,'pass!')
                print('userinputarray',userinputarray)
            else:
                returnvalue = player_2.judge(userinputarray)         #send值
                t = player_2.compare(e,userinputarray,returnvalue,returnvalue,playertotal,player_1)
                print(t)
                while (t == -1):
                    #print('enter')
                    userinputarray = player_2.receive(playertotal,userinputarray)
                    returnvalue = player_2.judge(userinputarray)     #send值
                    #print('l')
                    t = player_2.compare(e,userinputarray,returnvalue,returnvalue,playertotal,player_1)
            
            print('e',e)                                         #檢查
            print('player_1',a,player_1)                         #剩下的手牌
        
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
                returnvalue2 = player_2.judge(userinputarray2)     #send值
                #print('l')
                t = player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
            print('e',e)
            print('player_3',b,player_3)                 
       
            #continue
        else:
            if (userinputarray2[0] == 'p'):
                playerrecord[1] = 1                         #把第二位玩家的狀態設為1
                print(b,'pass!') 
                #continue               
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
                        #continue
                    else:
                        returnvalue2 = player_2.judge(userinputarray2)     #send值
                    #print('l')
                        t = player_2.compare(e,userinputarray2,returnvalue,returnvalue2,player1total,player_3)
                print('e',e)
                print('player_3',b,player_3)                 
        
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
                returnvalue3 = player_2.judge(userinputarray3)     #send值
                #print('l')
                t = player_2.compare(e,userinputarray3,returnvalue2,returnvalue3,player2total,player_5)
            print('e',e)
            print('player_5',b,player_5)                 
       
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
                    returnvalue3 = player_2.judge(userinputarray3)     #send值
                    #print('l')
                    t = player_2.compare(e,userinputarray3,returnvalue2,returnvalue3,player2total,player_5)
                print('e',e)
                print('player_5',c,player_5)     
    
        
        
        
main()    