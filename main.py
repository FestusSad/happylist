t='0'
x=[]
v=0
while t!='':
    t=input()
    if t!='':
        try:
            r=int(t)
            x.append(r)
        except:
            x.remove(x[v])

def f(x):
    a=max(x)
    x.remove(a)
    b=max(x)
    x.remove(b)
    c=max(x)
    x.remove(c)
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        s=(p*(p-a)*(p-b)*(p-c))**0.5
        return s
print(f(x))