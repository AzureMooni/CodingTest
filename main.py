# 거스름돈 문제

# 손님에게 N원을 동전(500, 100, 50, 10원)으로 거슬러 주어야 할때,
# 가장 적은 동전으로 거슬러 주려면 어떻게 해야 하는가?

N = int(input("거스름돈 금액 입력 :")) # 거스름돈 액수 입력
count = 0
coin_types = [500, 100, 50, 10]
print("\n")

for coin in coin_types: 
  count += N // coin
  print(str(coin), "원", N // coin, "개")
  N %= coin

print("\n동전 갯수 :", str(count), "개")

if N % 10 > 0:
  print("거슬러주지 못하는 금액 : ", N)