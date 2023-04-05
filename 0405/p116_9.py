'''
2023.04.05
기경목
본봉과 수당을 정수로 입력 받아서 이번달 월급 수령액 구하는 프로그램
(세금은 총액의 20%)

'''
sal=int(input("본봉:"))#본봉입력
allo=int(input("수당:"))#수당입력

tax=sal+allo*0.2
total_sal=sal+allo-tax
