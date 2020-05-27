import sys
import os
import datetime
# print(sys.argv)

# print(sys.getwindowsversion())
# print(sys.copyright)
# print(sys.version)

# print("OS : ",os.name)
# print("폴더 : ",os.getcwd())
# print("files : ",os.listdir())

# os.mkdir("Hello")
# os.rmdir("Hello")
# os.system("tree")

current = datetime.datetime.now()
print("{}년{}월{}일{}시{}분{}초".format(current.year,current.month,
        current.day,current.hour,current.minute,current.second))

from urllib import request

target = request.urlopen("https://google.com")
output = target.read()

print(output)

