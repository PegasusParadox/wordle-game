#追加功能:顯示已用字元作為提示(confirm)
#追加功能:隔秒輸出(confirm)
#追加功能:顯示結果，以供分享(confirm)
import time
import random
import sys
import threading
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
correct=set()#提示字元儲存處
wrong_position=set()#提示字元儲存處
fail=set()#提示字元儲存處
flag=0#判斷是否全對時用
print("want to play?(y or n or setting):",end="")
tmp=input()#輸入上述其中一個指令
length=int(5)
times=int(6)
times_tmp=times
share=[]
while True:
    if(tmp=="y"):
        correct.clear()
        wrong_position.clear()
        fail.clear()
        lines=open(str(length)+".txt","r").read().splitlines()
        s=random.choice(lines)
        #print("ans:",end="")
        #print(s)#顯示答案
        times=times_tmp
        while True:
            if(times==0):#次數用完
                time.sleep(0.25)
                print("The answer is:",end="")
                print(s)
                print("You lose")
                print("")
                share.clear()
                break
            print("")
            print("You have used follwing characters:")
            print(bcolors.OK + "correct:" + bcolors.RESET,end="")
            print(correct)
            print(bcolors.WARNING + "exit,but wrong position:" + bcolors.RESET,end="")
            print(wrong_position)
            print(bcolors.FAIL + "does not exit:" + bcolors.RESET,end="")
            print(fail)
            print("Please enter a word which contains five character(remain %d chance):"% times,end="")
            tmp_str=input()
            player_str=tmp_str.upper()
            if(player_str=="FUCK THIS GAME"):#小彩蛋(玩到一半結束遊戲)
                print(bcolors.FAIL + "( •́ω•̩̥̀ )" + bcolors.RESET)
                break
            if(len(player_str)!=length):#輸入錯誤格式，忽略這次並不刪減挑戰次數
                print("wrong length")
                continue
            if(not(player_str in lines)):#輸入非資料庫的單字，忽略這次並不刪減挑戰次數
                print("This word does not exit")
                continue
            for j in range(length):
                sys.stdout.flush()#強制輸出(sleep會讓整隻程式睡著)
                if(player_str[j] in s):
                    if(player_str[j]==s[j]):#修正超過兩個以上重複字母所發生的判斷錯誤
                        print(bcolors.OK + player_str[j] + bcolors.RESET,end="")
                        flag+=1
                        time.sleep(0.5)
                        correct.add(player_str[j])
                        share.append("🟩")
                        continue
                    if(s.find(player_str[j])==j):#正確位置
                        print(bcolors.OK + player_str[j] + bcolors.RESET,end="")
                        flag+=1
                        time.sleep(0.5)
                        correct.add(player_str[j])
                        share.append("🟩")
                        continue
                    elif(s.rfind(player_str[j])==j):#正確位置
                        print(bcolors.OK + player_str[j] + bcolors.RESET,end="")
                        flag+=1
                        time.sleep(0.5)
                        correct.add(player_str[j])
                        share.append("🟩")
                        continue
                    else:#存在但位置不對
                        print(bcolors.WARNING + player_str[j] + bcolors.RESET,end="")
                        time.sleep(0.5)
                        wrong_position.add(player_str[j])
                        share.append("🟨")
                        continue
                else:#不存在
                    print(bcolors.FAIL + player_str[j] + bcolors.RESET,end="")
                    time.sleep(0.5)
                    fail.add(player_str[j])
                    share.append("⬛️")
                    continue
            if(flag==length):#全字皆正確
                time.sleep(0.25)
                print("")
                print("Correct!Congradulation")
                print("")
                print("the result:")
                res=0
                for k in range(times_tmp-times+1):#顯示本次遊戲之結果
                    for u in range(length):
                        print(share[res],end="")
                        res+=1
                    print("")
                print("")
                share.clear()
                flag=0
                res=0
                break
            flag=0
            times-=1
            print("")
    elif(tmp=="n"):#結束遊戲
        print("GAME OVER")
        break
    elif(tmp=="setting"):#設定最大挑戰次數以及單字長度
        print("請輸入最大挑戰次數:",end="")
        times=int(input())
        times_tmp=times
        while True:
            print("請輸入單字長度(4~10):",end="")
            length=int(input())
            if(length>10 or length<4):
                print("輸入錯誤")
            else:
                break
        print("want to start the game?(y or n):",end="")
        tmp=input()
        continue
    else:#在詢問是否進行遊戲時輸入了y/n/setting以外的選項
        print("wrong type")
    print("want to play again?(y or n or setting):",end="")
    tmp=input()