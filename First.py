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
def getdomain(x):
    flag = 0
    for i in x:
        if i == chr(64):
            flag = 1
        if flag == 1:
            print(i)

getdomain(mail)

def findDog(x):
    s = x.split()
    for i in s:
        if s in ["dog","Dog","DOG"]:
            print("True")
            break
        else:
            print("Flase")

findDog('dog')