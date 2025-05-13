import math

num = int(input("Enter the number :"))

#to calculate square root
sqrt_result = math.sqrt(num)
print("square root  :",sqrt_result)
 
#to calculate log base e
if num > 0:
    log_result = math.log(num)
    print(" logarithm : ",log_result)
else:
    print("Natural logarithm is undefined for zero or negative numbers.")

#to calculate sune (of number in ) radian

sine_reslut = math.sin(num)
print("sine :",sine_reslut)