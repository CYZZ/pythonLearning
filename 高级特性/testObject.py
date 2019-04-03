# print(dir('ABC'))
# import re
# m = re.search('(?<=abc)def','abcdef')
# print(m.group(0))

# try:
#     f = open('work.txt','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

with open('work.txt','r') as f:
    print(f.read())
