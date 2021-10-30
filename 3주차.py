import urllib.request
from bs4 import BeautifulSoup

web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup = BeautifulSoup(web, 'html.parser')
li = soup.findAll('a') # a 부분만 추출해준다.
base = "http://www.swu.ac.kr"

print(" *** 서울여자대학교 학과 및 홈페이지 정보 *** \n")
print("학과\t\t\t\t홈페이지")

for k in li:

    if "대학원" in k.text or "교육원" in k.text: #먼저 대학원, 바롬인성교육원을 제외해준다
            continue
    elif "전공" in k.text or "학과" in k.text or "학부" in k.text: #전공과 학과 학부를 확인해준다
        if k.text =="공동기기실"or k.text=="자율전공학부" : #그 중에서도 공동기기실과 자율전공학부는 넘어간다
            continue
        web2 = urllib.request.urlopen(base + k['href']) 
        soup2 = BeautifulSoup(web2, 'html.parser')
        li2 = soup2.find('a', {"class","btn btn_xl btn_blue_gray"})# 홈페이지에 들어가 홈페이지 바로가기 버튼 부분의 코드 확인하면 이럼
        print(k.text, end="\t\t\t") #학과 이름을 출력해준다
        
        if li2 is None :
            print("홈페이지 없음") # 안해줬더니 자꾸 오류가 나서 에러로 걸러줌 (*)되어있는 학과!
        else:
                
            if "홈페이지" in li2.text:
                print(li2['href'])
            else:
                print("홈페이지 존재하지않음")


        
        
