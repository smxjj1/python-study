tem = input("请输入1到100之间的数字");
inputNum = int(tem);
while inputNum>100 or inputNum<1:
    tem = input("请再次输入正确的数字,你个弱智")
    inputNum = int(tem);
if inputNum<100 or inputNum>1:
    print("ok")
else:
    print("ojbk")
print("game over!!!")

