from sys import getsizeof
test_variable=[1]
for i in range(2000000000):
    test_variable.append(1)
print( type(test_variable),getsizeof(test_variable))
#1/2 float 0.5
#1//2 int 0
#10.0//3 float 3.0
#10.0/3 float  3.33333333
#15//5.0 float 3.0
#5/0 ZeroDivisionError: division by zero