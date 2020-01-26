#str
owog="Delger"
#  len()- urt
#  lower()- jijigruuleh
#  upper()- tomruulah
#  capitalize()- ehnii useg tomruulah
#  replace()- temdegt solih
print(owog.find("e"))
print(owog.count("e"))
print(owog[2:10])

a=21
b=21
if a>b:
    print("a too ih")
elif a==b:
    print("tentsuu")
else:
    print("b too ih")

a, b = input().split()
for i in range(a, b+1):
    print(i)