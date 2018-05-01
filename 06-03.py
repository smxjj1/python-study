#推导过程
    #这个数一定是7的倍数，那么7*n
    #怎么知道n是哪个数，当(x%2 == 1)；(x%3 == 2)；(x%5 == 4)；(x%6==5)同时成立时，
    #(x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6==5)为True，即能找到n
flag = False;
x = 7;
n = 1;
while not flag:
    if((x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6==5)):
        flag = True;
    else:
        x = 7*(n+1);
    n += 1;
print(x)
#缺点：没有溢出检测，可能会超出py的运算范围，但是可能性比较小
