from math import ceil,log
class SG_Tree:
  def build_tree(self,node,a,b,arr,tree):
    if(a>b):
        return
    if(a==b):
        tree[node]=arr[a];
        return
    self.build_tree(node*2,a,(a+b)/2,arr,tree)
    self.build_tree(node*2+1,1+(a+b)/2,b,arr,tree)
    tree[node]=max(tree[node*2],tree[node*2+1])
  def __init__(self,Arr):
      self.N=len(Arr)
      #print "N ",self.N
      self.tree=[0]*((1<<int((ceil(log(self.N,2))+1))))
      #print len(self.tree)
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
    tree[node]=max(tree[node*2],tree[node*2+1])
  def query_tree(self,node,a,b,i,j,tree):
    if(a>b or a>j or b<i):
        return float('-inf')
    if(a>=i and b<=j):
        return tree[node]
    q1=self.query_tree(node*2,a,(a+b)/2,i,j,tree)
    q2=self.query_tree(1+node*2,1+(a+b)/2,b,i,j,tree)
    return max(q1,q2)
  def update(self,a,b,val):
    return self.update_tree(1,0,self.N-1,a,b,val,self.tree)
  def query(self,a,b):
    return self.query_tree(1,0,self.N-1,a,b,self.tree)
"""arr=range(8)+[18]
print len(arr)
print arr
tree=SG_Tree(arr)
for i in range(7):
  print tree.query(0,i)
"""
    
