def search(list,n):
  
    for i in range(len(list)):
        if list[i] == n:
            return True
    return False
  

list = [1, 2, 'sachin', 4,'sumit', 6]
  

n = 'sumit'
  
if search(list, n):
    print("Found")
else:
    print("Not Found")
