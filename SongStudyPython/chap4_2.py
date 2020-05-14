#딕셔너리 선언
dictionary = {
    "name":"7D 건조망고",
    "type":"당절임",
    "ingredient":["망고","설탕","매타주아황산나트륨","치자황색소"],
    "origin":"Philippines"
}

value = dictionary.get("price")

print("값",value)

if value ==None:
    print("에러났습니다.")