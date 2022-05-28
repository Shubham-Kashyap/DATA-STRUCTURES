# program to get the sum of digits 
def getSumOfDigits(number):
    # print(number)
    # assert number < 0 and int(number) == number, "The number should be a positive ineger";
    if(number == 0):
        return 0;
    else:
        # print("number remainder", number%10)
        return (number % 10) + getSumOfDigits(number/10)
print("The sum of digits of a number : ")
print(getSumOfDigits(155)); # print sum of digits



# program to get power of number
""" program to get power of number """
print('\n')
def getPowerOfNumber(base , exponent):
    assert exponent >= 1 and int(exponent ) == exponent , "The exponent must be positive integer only !";
    if(exponent == 0):
        print("Any number with power 0 will always return 1 ");
        return 1;
    elif(exponent == 1):
        #print('Any number with power 1 return number itself');
        return base;
    else:
        return base * getPowerOfNumber(base , exponent -1);
        # return result;
print("power of a number :")
print(getPowerOfNumber(2,4));



# program to get gcd of number
""" program to get gcd of number """
print('\n')
def greatestCommonDivisor(a,b):
    assert int(a) == a  and int(b) == b , "cant be negative";
    if(b == 0):
        return a;
    elif(a == 0):
        return 0;
    else:
        result = greatestCommonDivisor(b , a % b)
        return result;
print("GCD number :")
print(greatestCommonDivisor(48,18));



