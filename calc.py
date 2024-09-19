def find_diff(first:int=1, second:int=0)->int:
    return first - second
print(find_diff(20,10))
print(find_diff(second=10,first=20))
print(find_diff(second=10))
print(find_diff())
def change_name(names,index,name):
    names[index] = name

names = ['modi','rahul']
print(names)
change_name(names,1,"modiji")
print(names)

print(sum([10,20,20]))

def find_sum(first, second,*other):
    s = first+second
    if(len(other)>0):
        for num in other:
          s += num
    return s
print(find_sum(10,20))
print(find_sum(10,20,30))
print(find_sum(10,20,30,40,50))


def find_sum(first, second,**other):
    s = first+second
    if(len(other)>0):
        for num in other.values():
          s += num
    return s

print(find_sum(first=10,second=20))
print(find_sum(first=10,second=20,third=50))
#print(find_sum(first=10,second=20,third=30)) #60
print(find_sum(first=10,second=20,third=30,fourth=40,fifth=50))

#def fact(N)