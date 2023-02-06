def findPairs(lst, K): 
    res = []
    while lst:
        num = lst.pop()
        diff = K - num
        if diff in lst:
            res.append((diff, num))
          
    res.reverse()
    return res
      
# Driver code
lst = [1, 5, 3, 7, 9]
K = 12
print(findPairs(lst, K))