#Question 1
data=[]
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

data.append(num1)
data.append(num2)
data.append(num3)
new_list=[]
while data:
    min=data[0]
    for x in data:
        if x < min:
            min=x
    new_list.append(min)
    data.remove(min)
print("From least to greatest, the order is :" ,new_list)

#Question 2
import cmath
a = float(input("Please enter a number :"))
b = float(input("Please enter a number :"))
c = float(input("Please enter a number :"))
#calculation of the discriminant
d = (b**2) - (4*a*c)
#finding the solution
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The only roots are {0} and {1}'.format(sol1,sol2))
#Question 3
#sum of digits from 1 to n
n = input("Please enter a positive interger : ")
n=int(n)

sum1 = [(((num)*(num+1)*(2*num +1)*(3*num**2 +3*num -1))/30) for num in range(1,n)]
print("The total computed using for loop" , sum(sum1))
sum2 = sum([(((n)*(n+1)*(2*n +1)*(3*n**2 +3*n -1))/30)])
print("The total computed using the formula" ,sum2)

#Question 4
# This program is intended to output a bill for a fruit stand
num_apples = int(input("Please enter the number of apples: "))
num_bananas = int(input("Please enter the number of bunches of bananas: "))
num_oranges = int(input("Please enter the number of oranges: "))
num_lemons = int(input("Please enter the number of lemons: "))
num_total = num_apples + num_bananas + num_oranges + num_lemons
price_apples = 0.50
price_bananas = 1.75
price_oranges = 0.75
price_lemons = 1.50
tot_apples = num_apples*price_apples
tot_bananas = num_bananas*price_bananas
tot_oranges = num_oranges*price_oranges
tot_lemons = num_lemons*price_lemons
bill_tot = tot_apples + tot_bananas + tot_oranges + tot_lemons
num = float(input("Input a number: "))
if num > 0:
   print("It is positive number")
elif num == 0:
   print("It is Zero")
else:
   print("It is a negative number")
class PluralItem(object):
    def __init__(self, num):
        self.n = num
        self._get_s()
    def _get_s(self):
        self.s = '' if self.n == 1 else 's'

class PluralES(PluralItem):
    def _get_s(self):
        self.s = 's' if self.n == 1 else 'es'

class PluralI(PluralItem):
    def _get_s(self):
        self.s = 'us' if self.n == 1 else 'i'
print("")
print("The total bill for {num_apples} apples is: ${tot_apples:.2f}")
print("The total bill for {num_bananas} bananas is: ${tot_bananas:.2f}")
print("The total bill for {num_oranges} oranges is: ${tot_oranges:.2f}")
print("The total bill for {num_lemons} lemons is: ${tot_lemons:.2f}")
print("")
print(f"The total number of items purchased is: {num_total}")
print(f"The overall total bill is: ${bill_tot:.2f}")
 #Question 5
def sum(N):
    global S1, S2, S3

    S1 = (((N // 3)) *
          (2 * 3 + (N // 3 - 1) * 3) // 2)
    S2 = (((N // 5)) *
          (2 * 5 + (N // 5 - 1) * 5) // 2)
    S3 = (((N // 10)) *
          (2 * 10 + (N // 10 - 1) * 10) // 2)

    return int(S1 + S2 - S3)


if __name__ == '__main__':
    N=int(input("Please enter a number :"))
    print("The sum of integers satisfying the condition:",sum(N))

#Question 6
n=int(input("Please enter a positive error tolerance :"))
sum3 = sum([((-1**i)*((i+1)/i**3*i+1)) for i in range(1,n)])
print(sum3)