# class monkey():
#     def patch(self):
#         print("patch is being printed")
# def mon_pat(self):
#         print("mon_pat is being called")
# monkey.patch =  mon_pat
# obj = monkey()
# obj.patch()
#                                   **** Replace String with a given character ****
# def str_replace(text,ch):
#     result = ''
#     for i in text:
#         if i == ' ':
#             i = ch
#         result += i 
#     return result

# text = "leel s i"
# ch = "a"
# cha = str_replace(text,ch)
# print(cha)
# 
# def valid_square(num):
#     square = int(num**0.5)
#     check = square**2==num
#     print(check)
# valid_square(49)
# valid_square(109099)