'''
2023.04.19
기경목
두개 숫자를 입력을 받아서 두번째수가 첫번째 수의 약수인지 아닌지 구분하기
#문제분석
 변수-정수1은 (num1) 정수2는 (num2)
 수식-num1%num2==0(num2는 num1의 약수)
 #알고리즘
  1.변수선언
   num1,num2 정수로 입력 받기
  2.논리(선택if,else)
  if num1%num2==0
     num2는 num1의 약수이다
else: 
    num2는 num1의 약수가 아니다
   
'''
num1=int(input("첫 번째 정수를 입력하세요 :"))
num2=int(input("두 번째 정수를 입력하세요 :"))

if num1%num2==0 :
    print("{}는{}의 약수 입니다.".format(num2,num1))
else:
    print("{}는{}의 약수 아닙니다.".format(num2,num1))

