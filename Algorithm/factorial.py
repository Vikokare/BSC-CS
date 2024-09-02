from math import sqrt

num = int(input('Enter number:'))

prime_factors_list = []
while num % 2 == 0:
    prime_factors_list.append(2)
    num = num/2
for i in range(3, int(sqrt(num))+1, 2):
    if num % i == 0:
        prime_factors_list.append(i)
        num = num/i
if num > 2:
    prime_factors_list.append(int(num))
print("the fractorial is ",prime_factors_list)

