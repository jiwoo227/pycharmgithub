# 3.아래 코드를 이용하여 각 list1의 값을[2, 3, 4, 5, 6]으로 바꾸시오(Python코드로)

list1 = [10, 20, 30, 40, 50]
# a라는 변수(공간)을 새로 만들고 거기에, 10,20,20,40,50을 차례대로 넣는다.
# 따라서 a+1은 a에ㅔ 있는 값이 11,21,31,41,51로 변함
# list1에 있는 값이 변하는 것은 아니다.

for i in range(0, len(list1)):

   list1[i] += 1


print(list1)