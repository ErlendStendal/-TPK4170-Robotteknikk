import math

def grubler(m, N, J, dof_i):
    
    dof = m*(N-1-J)
    for i in dof_i:
        dof += i    
    
    return dof

print(grubler(3, 4, 4, [1, 1, 1, 1])) #out: 