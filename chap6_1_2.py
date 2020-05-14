try:
    number = int(input("점수 입력 : "))
    if number > 0 :
        raise NotImplementedError("0이 넘어")
    else :
        raise NotImplementedError("0이 안되")
except NotImplementedError as ex:
    print("구현좀..")
    print(ex)
except ValueError as ex:
    print("정수좀;;")
except Exception as ex:
    print("??")