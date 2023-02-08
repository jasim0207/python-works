def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k - 1)
        #print(result)
        print(tri_recursion(k - 1))
    else:
       result = 0
    return result
#print("\n\nRecursion example results")
tri_recursion(6)