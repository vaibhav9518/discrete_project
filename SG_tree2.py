from math import ceil,log
class SG_Tree2:
  def build_tree(self,node,a,b,arr,tree):
    if(a>b):
        return
    if(a==b):
        tree[node]=arr[a]
        self.map[node]=a
        return
    self.build_tree(node*2,a,(a+b)/2,arr,tree)
    self.build_tree(node*2+1,1+(a+b)/2,b,arr,tree)
    if(tree[node*2]>=tree[node*2+1]):
        tree[node]=tree[node*2]
        self.map[node]=self.map[node*2]
    if(tree[node*2+1]>tree[node*2]):
        tree[node]=tree[node*2+1]
        self.map[node]=self.map[node*2+1]    
  def __init__(self,Arr):
      self.map={}
      self.N=len(Arr)
      self.tree=[0]*((1<<int((ceil(log(self.N,2))+1)))-1)
      self.arr=Arr
      self.build_tree(1,0,self.N-1,self.arr,self.tree)
  def update_tree(self,node,a,b,i,j,value,tree):
    if(a>b or a>j or b<i):
        return
    if(a==b):
        tree[node]+=value
        return
    self.update_tree(node*2,a,(a+b)/2,i,j,value,tree)
    self.update_tree(1+node*2,1+(a+b)/2,b,i,j,value,tree)
    if(tree[node*2]>=tree[node*2+1]):
        tree[node]=tree[node*2]
        self.map[node]=self.map[node*2]
    if(tree[node*2+1]>tree[node*2]):
        tree[node]=tree[node*2+1]
        self.map[node]=self.map[node*2+1] 
  def query_tree(self,node,a,b,i,j,tree):
    if(a>b or a>j or b<i):
        return float('-inf')
    if(a>=i and b<=j):
        return self.map[node]
    q1=self.query_tree(node*2,a,(a+b)/2,i,j,tree)
    q2=self.query_tree(1+node*2,1+(a+b)/2,b,i,j,tree)
    if(q1==float("-inf")):
        return q2
    if(q2==float("-inf")):
        return q1
    if(self.arr[q1]>self.arr[q2]):
        return q1
    else:
        return q2
  def update(self,a,b,val):
    return self.update_tree(1,0,self.N-1,a,b,val,self.tree)
  def query(self,a,b):
    return self.query_tree(1,0,self.N-1,a,b,self.tree)
"""arr=range(8)+[18]+range(1,100)
arr=arr[::-1]
print len(arr)
print arr
tree=SG_Tree2(arr)
#print tree.query(0,5)
#input()
print tree.map
for i in range(9):
  print i,tree.query(0,i)#,arr[tree.query(0,i)]
""" 
