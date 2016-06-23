'''
https://www.codewars.com/kata/5262119038c0985a5b00029f
Is Prime

Define a function isPrime that takes one integer argument and returns true or false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Example

isPrime(5)
=> true
Assumptions

You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers.
'''
def is_prime(num):
    if (num%2==0 and num!=2) or num==1 or num==-1:
        return False
    else:
        if num>0:
            for x in range(3,num,2):
                if num%x==0:
                    return False
        else:
            for x in range(-3,num,-2):
                if num%x==0:
                    return False
    return True