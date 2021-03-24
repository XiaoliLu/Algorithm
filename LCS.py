def LCS(s1 ,s2):
  m = len(s1)
  n = len(s2)
  c = [[0 for i in range(n)] for i in range(m)]
  flag = [[0 for i in range(n)] for i in range(m)]
  for i in range(m):
    for j in range(n):
      if s1[i] == s2[j]:
        c[i][j] = c[i-1][j-1] + 1
        flag[i][j] = 'ij'
      elif c[i-1][j] >= c[i][j-1]:
        c[i][j] = c[i-1][j]
        flag[i][j] = 'i'
      else:
        c[i][j] = c[i][j-1]
        flag[i][j] = 'j'
  return c,flag,c[m-1][n-1]
  
def print_LCS(s,flag,m,n):
  if m ==0 or n == 0:
    return
  if flag[m-1][n-1] == 'ij':
    print_LCS(s,flag,m-1,n-1)
    print(s[m-1])
  elif flag[m-1][n-1] == 'i':
    print_LCS(s,flag,m-1,n)
  else:
    print_LCS(s,flag,m,n-1)
    
    
if __name__ == '__main__':
  s1 = 'abcdba'
  s2 = 'bdcaba'
  c,flag,len_LCS = LCS(s1,s2)
  print_LCS(s1,flag,len(s1),len(s2))
  
