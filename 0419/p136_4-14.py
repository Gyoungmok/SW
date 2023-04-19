'''
2023.04.19
기경목
성별,키,몸무게를 입력받아서 BMI지수 구하고 비만도 측정하기
#문제분석
    변수-성별(sex),키(height),몸무게(weight),평균BMI(avg)
    수식-
    (남)avg=height*height*22
    (여)avg=height*height*21
#알고리즘
    1.변수선언
    sex,height(실수),weight(실수)를 입력 받는다.
    2.논리(내포된 선택문)
    if 성별이 여자:
    avg 계산
    if avg>=120: 
        *과체중*
    elif 110<=avg<=119:
        *과체중*

    else:
     *표준*
    elif 성별이 남자:
     
    else:
    *성별 잘못 입력*
'''
sex=input("성별입력('M or n' 또는 'F or f') :")
height=float(input("키 입력(cm) :"))/100
weight=float(input("몸무게 입력(kg) :"))

if(sex=='M' or sex=='n') :
    avg=height*height*22
    if 110<=avg<=119:
        print("과체중")
    elif avg>=120:
        print("비만체중")
    else:
        print("표준체중")
elif(sex=='F' or sex=='f') :
    avg=height*height*21
    if 110<=avg<=119:
        print("과체중")
    elif avg>=120:
        print("비만체중")
    else:
        print("표준체중")
else :
    print("성별 입력이 잘못 되었습니다.")
