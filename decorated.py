def f2(f1):
    add=f1()
    sum=add+500
    print(sum)
@f2
def f1():
    return 500
print(f2(f1))