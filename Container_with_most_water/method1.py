def sym(n): #this is to find the value distribution of each element in an n element array
  ar=[]
  if n%2==1:
    for i in range(n):
      ar.append(abs(((n+1)/2)-i-1))
  else:
    for i in range(int(n/2)):
      ar.append(abs((n/2)-i-1))
    for i in range(int(n/2),n):
      ar.append(abs(n/2-i))
  return ar #this return an array of n size. for example n=5 gives [2,1,0,1,2]
  
def maxwat(height): # this function is to find the most water in the container
  n=len(height)
  value=sym(n)
  arr=[value[i]+height[i] for i in range(n)] # this adds the value of distances of each element and to get the priority of each element in array
  v1,v2=arr[:int(n/2)].index(max(arr[:int(n/2)])),arr[int(n/2):].index(max(arr[int(n/2):]))+(n//2) # this splits the array into two matrixes and find the max value indexes
  print(v1,v2)
  print(min(height[v1],height[v2])*abs(v1-v2)) # this is to find the area of the rectangular water content

#testcase 1
height1=[1,8,6,2,5,4,8,3,7]
maxwat(height1)

#testcase 2
height2=[1,2,1]
maxwat(height2)
