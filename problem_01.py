#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of  or  below .

def multiples(num):
    total = 0;
    for x in range(num):
        if(x % 3==0 or x % 5==0):
            total += x;

    return total;

print(multiples(1000));
#Answer: 233168
