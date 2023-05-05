import random
import socket
from shuffle import *
from concurrent.futures import ThreadPoolExecutor

# 创建线程池，设置大小为 10
executor = ThreadPoolExecutor(max_workers=10)
player_names = ["dealer", "player1", "player2", "player3"]
connected_players = {}  # 记录已连接的玩家

def handle_client(player_name,connected_clients, client_socket):
    player_cards = []
    player_names.remove(player_name)
    
    # 如果是庄家，发牌给自己
    if player_name == "dealer":
        client_socket.send('You are a DEALER.'.encode())
    else:
        client_socket.send(f'You are {player_name}.'.encode())

    # 记录已连接的玩家
    connected_players[player_name] = client_socket
    
    # 等待所有玩家连接完毕
    if len(connected_players) == 2:
        start_game(client_socket, connected_clients, dealer_cards)
    else:
        client_socket.send('Waiting for other pLayers'.encode())
        
            
    
def start_game(client_socket, connected_clients, dealer_cards):
    # 所有玩家连接完毕后开始游戏
    
    # 发牌给庄家
    dealer_cards.append(draw_card())
    dealer_cards.append(draw_card())
    
    # 发牌给每个玩家
    for i in range(len(connected_players)-1, -1, -1):
        dealer_cards = hit_or_stand(connected_clients[i], client_socket, dealer_cards)
    # message = f"Your win {w}people, lose {l}people." 
    message = "Game over!"
    connected_players['dealer'].send(message.encode())
    
    client_socket.close()

def draw_card():
    # 随机抽一张牌
    return random.randint(1, 10)

def get_result(player_cards, dealer_cards):   
    player_sum = sum(player_cards)
    dealer_sum = sum(dealer_cards)
    if player_sum > 21:
        return "You bust! You lose."
    elif dealer_sum > 21:
        return "Dealer bust! You win."
    elif player_sum > dealer_sum:
        return "You win!"
    elif player_sum == dealer_sum:
        return "Tie! You lose."
    else:
        return "You lose."

def hit_or_stand(player_name, client_socket, dealer_cards):
    if player_name == "dealer":
        message = "Your cards: " + str(dealer_cards) + "\nPlease choose 'hit' or 'stand': "
        connected_players[player_name].send(message.encode())
        response = connected_players[player_name].recv(1024).decode()
        while response.lower() == "hit":
            dealer_cards.append(draw_card())
            message = "Your cards: [" + ",".join([str(card) for card in dealer_cards]) + "]\n"
            connected_players[player_name].send(message.encode())
            if sum(dealer_cards) >= 21:
                return dealer_cards
            message = "Please choose 'hit' or 'stand':" 
            connected_players[player_name].send(message.encode())
            response = connected_players[player_name].recv(1024).decode()
            
            
        return dealer_cards
    else:
        player_cards = []
        player_cards.append(draw_card())
        player_cards.append(draw_card())
        ans = dealer_card(dealer_cards)
        message = "Your turn!\n\nYour cards: " + str(player_cards) + "\nDealer's card: " + str(ans)
        connected_players[player_name].send(message.encode())
        # 玩家回合
        while True:
            # 接收玩家的选择
            message = "Please choose 'hit' or 'stand':"
            connected_players[player_name].send(message.encode())
            choice = connected_players[player_name].recv(1024).decode().strip().lower()
            if choice == "hit":
                player_cards.append(draw_card())
                ans = dealer_card(dealer_cards)
                message = "Your turn!\n\nYour cards:" + str(player_cards) + "\nDealer's card: " + str(ans)
                connected_players[player_name].send(message.encode())
                if sum(player_cards) >= 21:
                    allresult(player_cards, client_socket, dealer_cards)
                    break
            elif choice == "stand":
                allresult(player_cards, client_socket, dealer_cards)
                break
            else:
                ans = dealer_card(dealer_cards)
                message = "Invalid choice. Please choose 'hit' or 'stand'.\n\nYour cards: " + str(player_cards) + "\nDealer's card: " + str(ans)
                connected_players[player_name].send(message.encode())

 
def allresult(player_cards, client_socket, dealer_cards):
    result = get_result(player_cards, dealer_cards)
    message = "Game over!\n\nYour cards: " + str(player_cards) + "\nDealer's cards: " + str(dealer_cards) + "\nResult: " + result
    client_socket.send(message.encode())

def dealer_card(dealer_cards):
   final_cards = []
   for i in range(len(dealer_cards)-1):
       final_cards.append(dealer_cards[i])

   return final_cards


# 启动服务器
HOST = '192.168.178.173'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
dealer_cards = []
print("Server started on " + HOST + ":" + str(PORT))


def main():
    connected_clients = []
    while True:
        client_socket, address = server_socket.accept()
        # 将任务提交给线程池
        print("New connection from " + str(address))
        if len(connected_clients) == 0:
            player_name = "dealer"
        elif len(connected_clients) > 0:
            player_name = f"player{len(connected_clients)}"
        else:
            message = "The game has already started. Please try again later."
            client_socket.send(message.encode())
            client_socket.close()
            continue
          
        connected_clients.append(player_name)
        executor.submit(handle_client, player_name,connected_clients , client_socket)

if __name__ == '_main_':
    main()

# 启动服务器
"""
import random
import socket
from concurrent.futures import ThreadPoolExecutor

# 创建线程池，设置大小为 10
executor = ThreadPoolExecutor(max_workers=10)
#player_names = ["dealer","player1", "player2", "player3"]

def handle_client(player_name, client_socket):
    player_cards = []
    #player_names.remove(player_name)
    # 如果是庄家，发牌给自己
    if player_name == "dealer":
        dealer_cards = []
        client_socket.send('You are a DEALER.'.encode())
        dealer_cards.append(draw_card())
        dealer_cards.append(draw_card())
        message = "Your cards: [" + str(dealer_cards[0]) + "," + str(dealer_cards[1]) + "]" 
        print('5')
        client_socket.send(message.encode())
        print('6')
    # 如果是玩家，发牌给玩家
    else:
        client_socket.send(f'You are {player_name}.'.encode())
        player_cards.append(draw_card())
        player_cards.append(draw_card())
        message = "Welcome to 21 game!\n\nYour cards: " + str(player_cards) + "\nDealer's card: " + str(dealer_cards[0])
        client_socket.send(message.encode())
    
    # 玩家回合
    while True:
        # 接收玩家的选择
        message = "Please choose 'hit' or 'stand':"
        client_socket.send(message.encode())
        choice = client_socket.recv(1024).decode().strip().lower()
        
        if choice == "hit":
            player_cards.append(draw_card())
            message = "Your cards: " + str(player_cards) + "\nDealer's card: " + '[' + str(dealer_cards[0]) + ']\n'
            client_socket.send(message.encode())
            if sum(player_cards) >= 21:
                break
        elif choice == "stand":
            #player_names.append(player_name)
            break
        else:
            message = "Invalid choice. Please choose 'hit' or 'stand'.\n\nYour cards: " + '[' + str(player_cards)  
            + ']' + "\nDealer's card: " + '[' + str(dealer_cards[0]) + ']\n'
            client_socket.send(message.encode())
    
HOST = '127.0.0.1'
PORT = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Server started on " + HOST + ":" + str(PORT))

players = ["player1", "player2", "player3"]
dealer_cards = []
def main():
    while True:
        client_socket, address = server_socket.accept()
        # 将任务提交给线程池
            
        print("New connection from " + str(address))
        message = "Please enter your name (" + "/".join(player_names) + "):"
        client_socket.send(message.encode())
        player_name = client_socket.recv(1024).decode().strip().lower()
        if player_name in players or player_name == "dealer":
            print('確定')
            executor.submit(handle_client, player_name, client_socket, players, dealer_cards)
        else:
            message = "Invalid player name. Please try again."
            client_socket.send(message.encode())
            #client_socket.close()

if _name_ == '_main_':
    main()

 player_cards.append(draw_card())
        player_cards.append(draw_card())
        message = "Welcome to 21 game!\n\nYour cards:" + "[" + str(player_cards[0]) + "," + str(player_cards[1]) + "]"
        client_socket.send(message.encode())
        message = "\nDealer's card:" + "[" + str(dealer_cards[0]) +"]"
        client_socket.send(message.encode())
"""

import socket

HOST = '192.168.178.173'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# 接收 "Please enter your name (player1/player2/player3):" 消息
message = client_socket.recv(1024).decode().strip()
print(message)

# 发送玩家名称
#player_name = input()
#client_socket.send(player_name.encode())

# 接收游戏数据
while True:
    data = client_socket.recv(1024).decode().strip()
    if data:
        print(data)
        if "Please choose 'hit' or 'stand':" in data:
            # 接收玩家选择并发送到服务器
            choice = input()
            while choice not in ["hit", "stand"]:
                choice = input("Invalid choice. Please choose 'hit' or 'stand': ")
            client_socket.send(choice.encode())
    else:
        break

client_socket.close()