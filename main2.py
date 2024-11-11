import requests
import os
import base64,json,requests
from bs4 import BeautifulSoup
import os, time, sys
import requests,re,pyfiglet
O =  '\033[1;31m' #Red
Z =  '\033[1;37m' #white
F = '\033[1;32m' #Green
B = '\033[2;36m' #Light Blue
X = '\033[1;33m' #Yellow
C = '\033[2;35m' #Purpl
R = '\033[5;31m' #Red
logo = pyfiglet.figlet_format(' gpt plus by omer aker ')

print(F+logo)

G1 = '\x1b[1;92m\x1b[38;5;46m'
G2 = '\x1b[1;92m\x1b[38;5;50m'
G3 = '\x1b[38;5;196m'
G4 = '\x1b[1;92m\x1b[38;5;210m'
G5 = '\x1b[38;5;90m'
G6 = '\x1b[38;5;93m'
G7 = '\x1b[1;92m\x1b[38;5;212m'
G8 = '\x1b[1;92m\x1b[38;5;208m'
G9 = '\x1b[38;5;123m'
while True: T = input(f'{G2}[ {G1}YOU {G2}] {G3}- {G4}Enter Text {G5}> {G6}'); h = {'Host': 'baithek.com', 'Content-Type': 'application/json', 'User-Agent': 'okhttp/4.9.2'}; d = {'name': 'Usama', 'messages': [{'role': 'user', 'content': T}]}; r = requests.post('https://baithek.com/chatbee/health_ai/new_health.php', headers=h, json=d); print(f"{G7}[ {G8}GPT {G7}] {G3}- {G9}{r.json()['choices'][0]['message']['content']}")