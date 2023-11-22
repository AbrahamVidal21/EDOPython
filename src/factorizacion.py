import numpy as np
# Matriz de coeficientes

A = np.array([[1,0,1,0], [2,1,0,1], [2,2,1,0], [0,2,0,1]])

# Vector resultante
B = np.array([0,0,0,1])

print("Array A", A)
print("Array B", B)

## Matriz U y L
U = np.zeros((len(A),len(A)))
L = U.copy()
C = np.zeros(len(A))
x = np.zeros(len(A))

# Número de elementos
N = len(A)
U[0,:]=A[0,:]
L[1:,0]=A[1:,0]/U[0,0]

for i in range(1,N-1):
    for j in range(i,N):        
        suma = 0;        
        for k in range(0,i):            
            suma = suma + L[i,k]*U[k,j]         
        #End for       
        U[i,j]=A[i,j]-suma    
        #End for        
        for k in range(i+1,N):        
            suma = 0;        
            for j in range(0,i):            
                suma = suma + L[k,j]*U[j,i]         
                #End for        
            L[k,i]=(A[k,i]-suma)/U[i,i]    
            #End for

suma = 0
for i in range(0,N-1):    
    suma = suma + L[N-1,i]*U[i,N-1]
    #End for
U[N-1,N-1]= A[N-1,N-1]-suma
C[0] = B[0]
for i in range(1,N):    
    suma = 0    
    for j in range(0,i):        
        suma = suma + (L[i,j]*C[j])    
        #End for    
    C[i]=B[i]-suma
    #End for
x[N-1]=C[N-1]/U[N-1,N-1]
for i in range(N-2,-1,-1):    
    st = 0    
    for j in range(i+1,N):        
        st = st + (U[i,j]*x[j])    
    #End for    
    x[i]=(C[i]-st)/U[i,i]
#End for
print("La solución de x:")
print(x)
print("Fin de la factorización LU :3")