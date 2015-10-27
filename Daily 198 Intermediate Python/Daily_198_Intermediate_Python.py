r, number = input("Enter the base and a number in that base (seperated by a space): ").split(" ")
r = int(r)
c = 0
sum = 0
x = 1
if(number[0]=="-"):
    x = -1
    number = number.replace('-', '')
for i in number[::-1]:
    sum += int(i)*r**c
    c += 1

number = sum*x
result=""
r = -r

if(r!=10):
    if(r>0):
        while(abs(number)>=abs(r)):
            result += str(abs(number%abs(r)))
            number /= r
        result += str(number)
        result = result[::-1]
    else:
        while number!=0:
            rest= number%r
            number/=r
            if(rest<0):
                number+=1
                rest+=abs(r)
            result+=str(rest)
        result = result[::-1]

else:
    result = str(number)
print (result)