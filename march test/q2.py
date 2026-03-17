def dectobin(number):
    if number==0:
        return ""
    else:
        return str(dectobin(number//2))+str(number%2)
print(dectobin(int(input("what decimal number do you want to convert to binary: "))))