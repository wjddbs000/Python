lists = [52, 273, 32, 72, 100]


try:
    inputs = int(input("정수 입력 : ")) 
    print("{}번째 요소 : 값 {}".format(inputs,lists[inputs]))
    # radius = int(input("정수 입력 > "))
    # print("원의 반지름 : ",radius)
    # print("원의 둘레 : ",2*3.14159265*radius)
    # print("원의 넓이 : ",3.14159265*radius*radius)   
except ValueError as ex:
    print(ex)
    print("제발 좀 정수를 입력하세요")
except IndexError as ex:
    print(ex)
    print("인덱스 에러. 작은 수를 넣으세요")
except Exception as ex:
    print(ex)
    print("뭐여")
# else:
#     print("에러가 발생하지 않았습니다")
# finally:
#     print("프로그램 종료")

# lists = ['11','22','33','44','하이','55']
# outputs= []

# for item in lists:
#     try:
#         float(item)
#         outputs.append(item)
#     except:
#         pass
# print(outputs)


# f = open("./basic.txt","r")
# try:
#     f.write("TEST")
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# print("파일 클로즈?",f.closed)


# def test():
#     print("test() start")
#     try:
#         print("test() try")
        
#         print("test() after return")
#     except :
#         print("test() except")
#     else:
#         print("test() else")
#     finally:
#         print("test() finally")    
#     print("test() end")

# test()
   