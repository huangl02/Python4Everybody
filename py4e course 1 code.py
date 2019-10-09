#Python for everyone (first course) week1-week7
# week 5 exercise 1
# calculate pay
hrs = input("Enter Hours:")
rate=input('Enter rate:')
h = float(hrs)
r=float(rate)
if h>40:
    pay=(h-40)*r*1.5+40*r
else:
    pay=h*r

print(pay)


# week 5 exercise 2
# calculate grade
score = input("Enter Score: ")
score=float(score)
if score<0 or score>1:
    print('error')
elif score>=0.9:
    print('A')
elif score>=0.8:
    print('B')
elif score>=0.7:
    print('C')
elif score>=0.6:
    print('D')
else:
    print('F')


# week 6 exercise
# calculate pay
def computepay(h,r):
    if h>40:
        pay=(h-40)*r*1.5+40*r
    else:
        p=h*r
    return pay

hrs = input("Enter Hours:")
rate=input("Enter Rate:")
h=float(hrs)
r=float(rate)
p = computepay(h,r)
print(p)

# week 7 exercise 1(video)
#calculate total and average of input numbers
num=0
tot=0.0
while True:
    sval=input('Enter a number:')
    if sval=='done':
        break
    try:
        fval=float(sval)
    except:
        print('invalid input')
        continue
    print(fval)
    num=num+1
    tot=tot+fval
print(tot, num, tot/num)

# week 7 exercise 2
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n=int(num)
    except:
        print('Invalid input')
        continue
    if largest<=n:
        largest=n
    elif largest<n:
        largest=n
    if smallest is None:
        smallest=n
    elif smallest>n:
        smallest=n
print("Maximum is", largest)
print("Minimum is", smallest)
