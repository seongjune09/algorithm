# 주민등록번호가 입력되면 주민등록에 포함된 정보를 출력하는 프로그램을 작성해 봅시다.
# 주민등록번호 입력시 중간에 하이픈(-)을 포함해 입력합니다.

n = input("주민등록번호 입력 : ")

if n[7] == '1':
    print(f"19{n[:2]}년에 태어난 남자입니다.")
elif n[7] == '2':
    print(f"19{n[:2]}년에 태어난 여자입니다.")
elif n[7] == '3':
    print(f"20{n[:2]}년에 태어난 남자입니다.")
elif n[7] == '4':
    print(f"20{n[:2]}년에 태어난 남자입니다.")
else :
    print("잘못입력하였습니다.")