'''
2023.04.12
기경목
두개의 숫자를 입력 받아 두 개의 수가 모두 짝수이면 두 수를 더한 결과를 출력하고, 그렇지 않고 하나가 홀수이면 몇 번째 입력한 수를 짝수로 입력해야 하는지 출력하시오

'''
num1=int(input("첫번째 정수를 입력하세요 : "))
num2=int(input("두번째 정수를 입력하세요 : "))
if num1%2==0 and num2%2==0:
   print(num1,'+',num2,'=',num1+num2) 
elif num1%2==0 and num2%2==1:
    print("두번 째 정수를 짝수로 입력하세요.")
elif num1%2==1 and num2%2==0:
    print("첫번 째 정수를 짝수로 입력하세요.")
else:
    print('두 숫자 모두를 짝수로 입력하세요')