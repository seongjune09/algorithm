# 만약 돈이 5000원 이상이 있으면 택시를 타고, 5000원은 없지만 2000원 이상 있으면 버스를 타고 2000원
# 도 없으면 걸어 가라 는 메시지를 출력하는 프로그램을 작성해 봅시다.

m = int(input("돈 입력 : "))
if m >= 5000:
    print("택시타고갑시다.")
elif m >= 2000:
    print("버스타고갑시다.")
else:
    print("걸어갑시다..")