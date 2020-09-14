print(" ")
print("########################################################")
print("#                                                      #")
print("#                 온라인 강의 3주차 과제               #")
print("#                                                      #")
print("#             학번 : 19273018      이름 : 이선빈       #")
print("#                                                      #")
print("#         리스트를 사용하여 평균 구하기 프로그램       #")
print("#                                                      #")
print("########################################################")

print(" ")
print(" ")

alist = []
sum = 0
for i in range(5):
    i = int(input("정수를 입력해주세요 : "))
    alist.append(i)
    sum += i

avg = sum/len(alist)
print("평균=",avg)



