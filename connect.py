import socket
import threading
import shuffle as sh
import time
SERVER = '127.0.0.1' # 伺服器IP地址
PORT = 5000  
HEADER = 1024
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = '!DISCONNECT'
server = socket.socket(socket.SOCK_DGRAM)
server.bind(ADDR)
FORMAT = 'utf-8'
allcards = []
IP = []
times = 0


class player:
    def __init__(self,name):
        self.name=name
        #self.poker=poker
    def getcards(self):
        self.poker  = sh.getpoker(sh.deal_card())
        return self.poker


sh.shuffle(52)
#hand = sh.pleyerpoker(1)
"""
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    server.sendto(send_length)
    server.sendto(message)
"""    

def handle_client(conn, addr):
    print(f'[NEW CONNETCION]{addr}connected.')
    user_name = conn.recvfrom(1024)
    pokerplayer = player(user_name)
    cards = pokerplayer.getcards()
    print(cards)
    allcards.append(cards)
    conn.sendto(cards.encode(FORMAT), addr)
    #conn.send('None'.encode(FORMAT))
    #conn.close()
    
    
def start(times):
    server.listen()
    print(f'伺服器等待連接,IP = {SERVER}')
    while True:
        conn, addr = server.accept()
        IP.append(addr)
        handle_client(conn, addr)
        #thread = threading.Thread(target=handle_client, args=(conn, addr))
        #thread.start()
        times += 1
        print(f'[ACTIVE CONNETCIONS]{threading.activeCount()}')
        print(times)
        if times == 2:
            print(allcards[::1])
            print(IP[::1])
            if len(allcards) == 2:  
                if allcards[0] > allcards[1]:
                    conn.sendto('You win'.encode(FORMAT), IP[0])
                    time.sleep(1)
                    conn.sendto('You lose'.encode(FORMAT), IP[1])
                    break
                else:
                    conn.sendto('You win'.encode(FORMAT), IP[1])
                    time.sleep(1)
                    conn.sendto('You lose'.encode(FORMAT), IP[0])
                    break
        

start(times)
server.close()
