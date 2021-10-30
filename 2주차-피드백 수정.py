import random
from datetime import datetime # 날짜 가져옴

res = []  #점수들
names=[] # 닉네임 
maxnum = 11 #최고기록 
f = open("C:/Users/hyoje/Desktop/SWING/2021/python study/updown_game.txt",'a+')#2주차 피드백 1
before=f.readlines() # 기존 파일 내용을 긁어옴

try:
    res.append(int(before[-1].split('')[0]))
except :
    ("지난 기록이 존재하지 않습니다.")
f.close()



while True:
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1.게임시작 2.기록확인 3.게임종료")
    menu = int(input()) # 메뉴에서 입력받음 어떤 걸 진행할지


    if(menu == 1): # 게임시작을 눌렀을 때
        ans = random.randint(1,101) ##랜덤으로 게임에서 지정해줌
        l = 1 #왼쪽값
        r=100 #오른쪽값
        i=0	#몇번째 도전인지

        while True:
            i+=1
            if(i > 10):
                print("게임오버") #최대 기회는 10번으로 지정한다.
                break
            try :
                print("%d번째 숫자 입력(%d~%d)" % (i,l,r)) #몇번째 입력한건지 , 범위와 함께 알려줌
                num = int(input("")) #입력값
                if num >100 or num <1:
                    print ("1~100 숫자만 입력하세요.")
                    continue
                
            except: #피드백 3 -- except문 오류 수정했습니다
                print (" error : 숫자만 입력해주세요.") #숫자말고 다른거 입력했을때의 예외처리
                continue # 숫자말고 다른거 입력한거는 카운트에 안들어가게 함

            
            f = open("C:/Users/hyoje/Desktop/SWING/2021/python study/updown_game.txt",'a')

            if(0<num<101):
                if num == ans:
                    print("정답\n%d번만에 맞춤" % i)
                    if maxnum == 11 : #처음 실행시
                        res.append(i)
                        name=input("닉네임을 입력해주세요 :")
                        file_data = "%d %s %s \n" % (i, name, datetime.today().strftime("%Y-%m-%d"))
                        f.write(file_data)
                        
                    elif(i < res[-1]): #여태 맞춘 기록보다 짧으면 최고 기록을 갱신해준다 
                        print("최고 기록 갱신~!")
                        name=input("닉네임을 입력해주세요 :")
                        maxnum=i
                        res.append(i) #몇번에 맞춘건지 기록해준다 
                        file_data = "%d %s %s \n" % (i, name, datetime.today().strftime("%Y-%m-%d")) #피드백 2 - 오류 수정했습니다
                        f.write(file_data) #닉네임도 저장해준다 / 날짜도 함께
                    break
                else :
                    if(0 < num <101) :
                        if(num < ans): #입력값이 정답보다 작을때에 출력
                            print("UP")
                            if(num > l):
                                l =num
                        elif(num > ans):# 입력값이 정답보다 클 때에 출력
                            print("DOWN")
                            if(num < r):
                                r =num
    
            else :
                print("1에서부터 100까지만 입력해주세요") 

                    
            #except:
             #   print (" error : 숫자만 입력해주세요.") #숫자말고 다른거 입력했을때의 예외처리
              #  i-=1 # 숫자말고 다른거 입력한거는 카운트에 안들어가게 함
            f.close()
        

    elif(menu == 2): # 기록보기를 선택했을때
        #res.sort() #점수 정렬
        f = open("C:/Users/hyoje/Desktop/SWING/2021/python study/updown_game.txt",'r')
        line =1
        lines = f.readlines()
        for lineee in reversed(lines):
            print("%d %s" %(line,lineee))
            line = line +1
        f.close
        #for i in range(len(res),0,-1):  #거꾸로 출력되게 함 기록된 배열은 뒤에 저장된거일수록 작을테니까!
         #   print("%d. %d" % i-1,res[i])
        #for i in range(len(res),0,-1): # 그 순서에 맞춰서 닉네임이랑 오늘 날짜를 저장해둠
         #   print("%s %s" % (names[i],today))
                  
    elif(menu == 3) : # 게임 종료를 눌렀을때

        break
    
    else: #1,2,3 말고 다른 숫자를 누르면 재입력받기
        print("메뉴 안의 숫자만 눌러주세요!") 
        
        
