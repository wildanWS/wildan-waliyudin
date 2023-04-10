# import datetime

# x = datetime.datetime.now()
# print(x)

# import datetime

# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))


# import datetime

# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%B"))


# import datetime

# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%d/%m/%Y"))


# arr_1 = [5,78,2,0]

# assert(min(arr_1)) == 0
# assert(max(arr_1)) == 78

# # funtion 5 pangkat 5

# assert(pow(5, 5)) == 3125

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")


# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")


# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])

# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)


# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())


# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the overwriting:
# f = open("demofile3.txt", "r")
# print(f.read())


