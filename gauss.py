Matrix=[]
x=[]
def Set():
    global Matrix
    global x
    try:
        n=input("Size of matrix: ")
    except NameError:
        print("Invalid data")
        return
    except EOFError:
        print("Empty data")
        return  
    if (not(type(n) is int)):
        print("Number must be Integer")
        return
    if (n<1):
        print("Count must be greater than zero")
        return
    i=0
    j=0
    x=[]
    while (i<n):
        lst=[]
        s=0
        index=i+1
        while (j<=n):
            if (j==n):
                lst.append(s)
            else:
                lst.append(float(1)/index)
                s=s+float(1)/index
            j=j+1
            index=index+1
        Matrix.append(lst)
        x.append(0)
        i=i+1
        j=0
def Print():
    global Matrix
    i=0
    n=len(Matrix)
    while (i<n):
        print Matrix.__getitem__(i)
        i=i+1
        
def Solve():
    global Matrix
    global x
    if (Matrix==[]):
        print "Empty matrix"
        return
    n=len(Matrix)
    k=0
    while(k<n-1):
        p=k
        m=k+1
        while (m<n):
            if (abs(Matrix[p][k])<abs(Matrix[m][k])):
                p=m
            m=m+1
        j=k
        while (j<n):
            r=Matrix[k][j]
            Matrix[k][j]=Matrix[p][j]
            Matrix[p][j]=r
            j=j+1
        r=Matrix[k][n]
        Matrix[k][n]=Matrix[p][n]
        Matrix[p][n]=r
        m=k+1
        while(m<n):
            c=float(Matrix[m][k])/Matrix[k][k]
            Matrix[m][n]=Matrix[m][n]-c*Matrix[k][n]
            i=k
            while(i<n):
                Matrix[m][i]=Matrix[m][i]-c*Matrix[k][i]
                i=i+1
            m=m+1
        k=k+1
    try:
        x[n-1]=round(float(Matrix[n-1][n])/Matrix[n-1][n-1],4)
    except ZeroDivisionError:
        print "Float division by zero "
        return
    k=n-2
    while (k>=0):
        s=0
        i=k+1
        while(i<n):
            s=s+Matrix[k][i]*x[i]
            i=i+1
        x[k]=round((Matrix[k][n]-s)/Matrix[k][k],4)
        k=k-1
    print "Resultat: ",x
            
print ("Programma GAUSS method: ")
Matrix=[]
b=[]
Set()
Print()
Solve()
