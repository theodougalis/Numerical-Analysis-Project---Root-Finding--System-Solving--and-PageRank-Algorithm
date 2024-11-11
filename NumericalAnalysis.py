import math
#Exercise 1
             #(a)
def f(x):
             y=(math.exp(math.sin(x)**3)+x**6-2*x**4-x**3-1)
             return y
def minRepeatsNeeded(a,b):
             N= (math.log(b-a)-math.log((0.5)*10**(-5))/math.log(2))
             return N

def dixotomisif(a,b,r):

             for i in range(r):
                          if (f(a)*f(b))<0:
                                       m=(a+b)/2
                                       if (f(m)==0):
                                                    print("Exact root found:")
                                                    return m
                                       if (f(a)*f(m)<0):
                                                    b=m
                                                    
                                       elif (f(b)*f(m)<0):
                                                    a=m
                          else:
                                       return("Can't approach root.")
                          
             return m

             #(b)
def df(x):
             y=(math.exp(math.sin(x)**3)*3*(math.sin(x)**2)*(math.cos(x))+6*x**5-8*x**3-3*x**2)
             return y
def ddf(x):
             y=(3*(3*(math.exp(math.sin(x)**3)*(math.sin(x)**4)*(math.cos(x)**2))+(math.exp(math.sin(x)**3))*((math.sin(2*x))*(math.cos(x)))-(math.sin(x)**3))+30*(x**4)-24*(x**2)-6*x)
             return y
             
def NRf(x):
             counter=0
             if ((f(x)*ddf(x))>0):
                          while (counter<100):
                                       counter+=1
                                       y=(x-(f(x)/df(x)))
                                       if (abs(y-x)<(0.5)*10**(-5)):
                                                    print(counter," repeats happened.")
                                                    return y
                                       x=y
             else:
                          return ("Choose another starting point")

             #(c)
def Secantf(a,b):
             counter=0
             while (counter<100): 
                          counter+=1
                          x=(b-((f(b)*(b-a))/(f(b)-f(a))))
                          if (abs(x-b)<(0.5)*10**(-5)):
                                       print(counter," repeats happened.")
                                       return x
                          a=b
                          b=x

#Exercise 2
             
             #(a)
def modNR(aF,aDf,aDdf,x,dig):
             counter=0
             if ((aF(x)*aDdf(x))>0):
                          while True:
                                       counter+=1
                                       y=x-(1/((aDf(x)/aF(x))-(aDdf(x)/(2*aDf(x)))))
                                       if (abs(y-x)<(0.5)*10**(-dig)):
                                                    print(counter," repeats happened.")
                                                    return y
                                       x=y
             else:
                          return ("Choose another starting point")
             #(b)

import random

def modDix(aF,a,b,dig):
             if (aF(a)*aF(b))<0:
                          counter=0
                          while (b-a)>=10**(-dig):
                                       counter+=1
                                       y=b-(random.uniform(0,b-a))
                                       if (aF(y)==0):
                                                    print("Exact root found after ",counter," repeats")
                                                    return y
                                       if (aF(a)*aF(y)<0):
                                                    b=y                                   
                                       elif (aF(b)*aF(y)<0):
                                                    a=y
             else:
                          return("Can't approach root.")
             print (counter," repeats happened.")
             return y

             #(c)

def modSecant(aF,x0,x1,x2,dig):
             counter=0
             while True:
                          counter+=1
                          q=(aF(x0)/aF(x1))
                          r=(aF(x2)/aF(x1))
                          s=(aF(x2)/aF(x0))
                          y=x2-(((r*(r-q)*(x2-x1))+((1-r)*s*(x2-x0)))/((q-1)*(r-1)*(s-1)))
                          if (abs(y-x2)<(0.5)*10**(-dig)):
                                       print(counter," repeats happened.")
                                       return y
                          x0=x1
                          x1=x2
                          x2=y 
def f2(x):
             y=(54*x**6)+(45*x**5)-(102*x**4)-(69*x**3)+(35*x**2)+(16*x)-4
             return y
def df2(x):
             y=(324*x**5)+(225*x**4)-(408*x**3)-(207*x**2)+(70*x)+16
             return y
def ddf2(x):
             y=(1620*x**4)+(900*x**3)-(1224*x**2)-(414*x)+70
             return y


#Exercise 3


             #(1)
def createID(dim):
             A=[[0]*dim for i in range(dim)]
             for i in range(dim):
                          A[i][i]=1
             return A
def swapRows(A,r1,r2):
             if r1==r2:
                          return A
             elif ((r1-1)<0 or (r1-1)>len(A)) or ((r2-1)<0 or (r2-1)>len(A)):
                          return ("Choose valid rows.")
             else:
                          t=A[r1-1]
                          A[r1-1]=A[r2-1]
                          A[r2-1]=t
             return A
def multiply(A,B):
             if len(A[0])!=len(B):
                          return ("Dimensions not suitable")
             C=[[0]*(len(B[0]))for d in range(len(A))]
             for i in range(len(A)):
                          for j in range(len(B[0])):
                                       for k in range(len(A[0])):
                                                    C[i][j]+=A[i][k]*B[k][j]
             return C
def createCopy(A):
             C=createID(len(A))
             for i in range(len(A)):
                          for j in range(len(A)):
                                       C[i][j]=A[i][j]
             return C
def pivot(A,P):
             while True:
                          for j in range(len(A)):
                                       for i in range(j,len(A)-1):
                                                    if (abs(A[i][j])<abs(A[i+1][j])):
                                                                 maxi=i+1
                                                                 swapRows(A,i+1,maxi+1)
                                                                 swapRows(P,i+1,maxi+1)
                                                    else:
                                                                 maxi=i
                                                                 swapRows(A,i+1,maxi+1)
                                                                 swapRows(P,i+1,maxi+1)
                          return A
def getLU(PA,L):
             for j in range(len(PA)):
                          for i in range(j+1,len(PA)):
                                       L[i][j]=(PA[i][j]/PA[j][j])
                                       PA[i][j]=0
                                       for k in range(j+1,len(PA)):
                                                    PA[i][k]-=(L[i][j]*PA[j][k])
             return PA
                                       
             
def palu(A):             
             PA=createCopy(A)
             P=createID(len(A))
             L=createID(len(A))
             pivot(PA,P)
             U=getLU(PA,L)
             
             return(P,L,U)
def axb(A,b):


             """
             Ax=b
             PAx=Pb
             LUx=Pb
             Assume Ux=z
             Solve Lz=Pb
             Then solve Ux=z

             """
             
             P,L,U=palu(A)
             Pb=multiply(P,b)
             z=[]
             for i in range(len(A)):
                          v=Pb[i][0]
                          for j in range(i):
                                       v-=(L[i][j]*z[j][0])
                          z.append([v])
             u=[[0]for i in range(len(z)-1)]
             u.append([z[len(z)-1][0]/U[len(z)-1][len(z)-1]])
             for i in range(len(A)-2,-1,-1):
                          v=(z[i][0]/U[i][i])
                          for j in range(len(A)-1,i,-1):
                                       v-=(((U[i][j])*(u[j][0]))/(U[i][i]))
                          u[i][0]=v
             return(u)


#Exercise 4

def powerM(A,b,dig):
             while True:
                          b=multiply(A,b)
                          l=b[0][0]
                          for i in range(len(b)):
                                       b[i][0]/=l                                      
                                       if abs(multiply(A,b)[0][0]-l)<10**(-dig):
                                                    b=multiply(A,b)
                                                    l=b[0][0]
                                                    for i in range(len(b)):
                                                                 b[i][0]/=l
                                                    return (l,b)
def AtoG(A,q):
             n=len(A)
             s=[]
             for i in range(n):
                          su=0
                          for j in range(n):
                                       su+=A[i][j]
                          s.append(su)
             G=createID(n)
             for i in range(n):
                          for j in range(n):
                                       G[i][j]=((q/n)+(((A[j][i])*(1-q))/(s[j])))
             return G
def task1():
             B=[[0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
                [0,0,1,0,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,1,0,1],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]]
             G=AtoG(B,0.15)
             counter=0
             for m in range(len(B)):
                          se=0
                          for k in range(len(B)):
                                       se+=G[k][m]
                          if se==1:
                                       counter+=1
             if counter==len(B):
                          return True
def task2():
             B=[[0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
                [0,0,1,0,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,1,0,1],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]]
             G=AtoG(B,0.15)
             b=[[0]for i in range(len(G))]
             b[0][0]=1
             l,p=powerM(G,b,20)
             su=0
             for j in range(len(p)):
                          su+=p[j][0]
             for j in range(len(p)):
                          p[j][0]/=su  
             return p
def task3():
             """
             connect the one I choose(first page) with the powerful ones, take out one irrelevant.
             """
             B=[[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                [0,0,1,0,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
                [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,1,1,0,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0]]
             G=AtoG(B,0.15)
             b=[[0]for i in range(len(G))]
             b[0][0]=1
             l,p=powerM(G,b,20)
             su=0
             for j in range(len(p)):
                          su+=p[j][0]
             for j in range(len(p)):
                          p[j][0]/=su
             if p[0][0]>0.026824566615597813:
                          return("Page 1 successfully went viral!")
def task4a():
             B=[[0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
                [0,0,1,0,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,1,0,1],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]]
             G=AtoG(B,0.02)
             b=[[0]for i in range(len(G))]
             b[0][0]=1
             l,p=powerM(G,b,20)
             su=0
             for j in range(len(p)):
                          su+=p[j][0]
             for j in range(len(p)):
                          p[j][0]/=su
             """
             Those with low importance went lower, while those with high went higher.
             Lowering q value means the chance the users enter a random website is
             lowered while the chances they enter one through the links of the current
             website (1-q) rise.
             """
             return(p)
def task4b():
             B=[[0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
                [0,0,1,0,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,1,0,1],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]]
             G=AtoG(B,0.6)
             b=[[0]for i in range(len(G))]
             b[0][0]=1
             l,p=powerM(G,b,20)
             su=0
             for j in range(len(p)):
                          su+=p[j][0]
             for j in range(len(p)):
                          p[j][0]/=su
             """
             Exactly the opposite. Rising q makes being linked less important due to
             rising the chances the users enter websites randomly.
             """
             return p
def task5():
             B=[[0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
                [0,0,1,0,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,3,0,0,0,0],
                [0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,1,1,0,0,3,0,0,0,0],
                [0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,1,0,1],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]]
             G=AtoG(B,0.15)
             b=[[0]for i in range(len(G))]
             b[0][0]=1
             l,p=powerM(G,b,20)
             su=0
             for j in range(len(p)):
                          su+=p[j][0]
             for j in range(len(p)):
                          p[j][0]/=su
             if p[10][0]>p[9][0]:
                          return ("It worked")
             else:
                          return ("It didn't work")
def task6():
             B=[[0,1,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,1,0,1,0,1,0,0,0,0,0,0,0],
                [0,1,0,0,0,1,0,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,1,0,0,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,1,1,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,1,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,1,0,1,0,1],
                [0,0,0,0,0,0,0,0,0,0,1,0,1,0]]
             G=AtoG(B,0.15)
             b=[[0]for i in range(len(G))]
             b[0][0]=1
             l,p=powerM(G,b,20)
             su=0
             for j in range(len(p)):
                          su+=p[j][0]
             for j in range(len(p)):
                          p[j][0]/=su  
             return p
             
             
             
             
             
             
