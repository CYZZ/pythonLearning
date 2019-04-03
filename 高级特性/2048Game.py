import random
matix = [[0 for i in range(4)] for i in range(4)]
def notzero(s):
    return s if s!=0 else '' #如果非零的话就返回本身，否则返回空字符串
def display():
    print("\r\
    ┌────┬────┬────┬────┐\n\
    │%4s│%4s│%4s│%4s│\n\
    ├────┬────┬────┬────┤\n\
    │%4s│%4s│%4s│%4s│\n\
    ├────┬────┬────┬────┤\n\
    │%4s│%4s│%4s│%4s│\n\
    ├────┬────┬────┬────┤\n\
    │%4s│%4s│%4s│%4s│\n\
    └────┴────┴────┴────┘"\
    %(notzero(matix[0][0]),notzero(matix[0][1]),notzero(matix[0][2]),notzero(matix[0][3]),\
      notzero(matix[1][0]),notzero(matix[1][1]),notzero(matix[1][2]),notzero(matix[1][3]),\
      notzero(matix[2][0]),notzero(matix[2][1]),notzero(matix[2][2]),notzero(matix[2][3]), \
      notzero(matix[3][0]),notzero(matix[3][1]),notzero(matix[3][2]),notzero(matix[3][3]),)
          )
display()

def init():
    initNumlag = 0
    while 1:
        k = 2 if random.randrange(0,10) > 1 else 4
        s = divmod(random.randrange(0,16),4)
        if matix[s[0]][s[1]] == 0:
            matix[s[0]][s[1]] = k
            initNumlag += 1
            if initNumlag == 2:
                break