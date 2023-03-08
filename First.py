s = "Hi there Dad!"
print(s.split())

planet = "Earth"
diameter = 12742

print("The diameter of {plan} is {num} kilometers." .format(plan = planet, num = diameter))

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

print(lst[3][1][2])

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d['k1'][3]['tricky'][3]['target'][3])

mail ="user@domain.com"
def getdomain(mail):
    print(mail.split('@')[-1])

getdomain(mail)

def findDog(x):
    return 'dog' in x.lower().split()

print(findDog('dog'))

count = 0

for i in 'This dog runs faster than the other dog dude!'.split():
    if i == 'dog':
        count += 1

print(count)

seq = ['soup','dog','salad','cat','great']
print(list(filter(lambda word: word[0]=='s',seq)))

def caughtspeeding(speed, is_birthday):
    if is_birthday == True:
        speed -= 5
    if speed <= 60:
        print("No ticket")
    elif speed > 61 and speed <= 80:
        print("Small Ticket")
    else:
        print("Big ticket")

caughtspeeding(81,True)
caughtspeeding(81,False)