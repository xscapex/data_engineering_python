# For given lists, if the value is none replace it with the last non none value, consider the edge case of consecutive Nones.

# examples
lst1 = [1,2,3,None, None,4,5]
lst2 = [None,8, None]

def listClean(lst):
  result = []
  for i in range( len(lst) ):
    if i == 0:
      result.append(lst[i])
    elif lst[i]==None:
      result.append(result[-1])
    else:
      result.append(lst[i])
  return result
