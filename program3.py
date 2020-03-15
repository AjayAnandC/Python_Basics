def lst_add(a):
    ans=0
    n=len(a)
    for i in range(n):
        ans=ans+a[i]
    return ans    
import math
a={"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
list_values = [ v for v in a.values() ]
print("Sum of values:",lst_add(list_values))

