# program to get the sum of digits 

def getSumOfDigits(number):
    # print(number)
    # assert number < 0 and int(number) == number, "The number should be a positive ineger";
    if(number == 0):
        return 0;
    else:
        # print("number remainder", number%10)
        return (number % 10) + getSumOfDigits(number/10)

print(getSumOfDigits(155)); # print sum of digits