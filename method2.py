def maxwat(ht): # this is a more direct method and the time complexity of this problem is O(n2)
  maxarea=0
  for i in range(len(ht)):
    for j in range(i+1,len(ht)):
      area=min(ht[i],ht[j])*(j-i)
      if area>maxarea:
        maxarea=area
  print(maxarea)
  return maxarea
#testcase1
height1=[1,8,6,2,5,4,8,3,7]
maxwat(height1)
#testcase2
height2=[1,2,1]
maxwat(height2)
  
