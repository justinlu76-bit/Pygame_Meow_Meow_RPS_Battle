import pygame
import random

def check_winner(player,computer):
    if player == computer:
        return "平手"
    elif player == "石頭" and computer == "剪刀":
        return "勝利"
    elif player == "剪刀" and computer == "布":
        return "勝利"
    elif player == "布" and computer == "石頭":
        return "勝利"
    else:
        return "失敗"

def play(player):
    choice = ["剪刀","石頭","布"]
    computer = random.choice(choice)
    if player == "剪刀":
        player_img = pygame.image.load("player_scissor.png")
    elif player == "石頭":
        player_img = pygame.image.load("player_rock.png")
    elif player == "布":
        player_img = pygame.image.load("player_paper.png")
    player_img = pygame.transform.smoothscale(player_img,(400,300)) 
    if computer == "剪刀":
        computer_img = pygame.image.load("computer_scissor.png")
    elif computer == "石頭":
        computer_img = pygame.image.load("computer_rock.png")
    elif computer == "布":
        computer_img = pygame.image.load("computer_paper.png")
    computer_img = pygame.transform.smoothscale(computer_img,(400,300)) 
    result =  check_winner(player,computer) # 勝負結果
    return result,player_img,computer_img 
    


pygame.init() #初始化
WIDTH = 1200 #寬度
HEIGHT = 850 #高度
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #建立遊戲視窗
pygame.display.set_caption("貓咪剪刀石頭布大戰") 

background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.smoothscale(background_img,(WIDTH,HEIGHT))
screen.blit(background_img, (0,0))

FPS = 60 #每一秒跟新60次
clock = pygame.time.Clock() #用來追蹤時間
running = True



button_rock = pygame.Rect(250,650,200,180) #按鈕石頭(x,y,寬度,高度)
button_paper = pygame.Rect(500,650,200,180) #按鈕布
button_scissor = pygame.Rect(750,650,200,180) #按鈕剪刀

player_score = 0
computer_score = 0

while running:

    for event in pygame.event.get(): # 檢查事件觸發
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #滑鼠左鍵           
                pos = pygame.mouse.get_pos() #滑鼠座標
                if button_rock.collidepoint(pos): #玩家點到rock的按鈕 
                    result,player_img,computer_img = play("石頭")
                elif button_paper.collidepoint(pos):
                    result,player_img,computer_img = play("布")
                elif button_scissor.collidepoint(pos):
                    result,player_img,computer_img = play("剪刀")
                screen.blit(background_img, (0,0))
                screen.blit(player_img,(150,200))
                screen.blit(computer_img,(650,200))
                if result == "平手":
                    player_score += 5
                    computer_score += 5
                elif result == "勝利":
                    player_score += 10
                else:
                    computer_score += 10
                font = pygame.font.SysFont("microsoftjhenghei", 40,bold=True) # 1. 建立字體
                text = font.render( f"{player_score}", True, (100, 60, 60) ) # 2. 把文字轉成可以顯示的 Surface 
                screen.blit( text, (180, 100) ) # 3. 顯示在畫面上 
                text2 = font.render( f"{computer_score}", True, (100, 60, 60) )
                screen.blit( text2, (980, 100) )
    pygame.display.flip()
pygame.quit()
