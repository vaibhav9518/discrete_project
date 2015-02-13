#all vertices can have values except -1
#        A
#   B    C   D
#  E F   H    I
# G     J K L
from math import ceil,log
tree={'a':['b','c'],'b':['a','d','e','f'],'c':['g','h','a'],'d':['b'],'e':['b'],'f':['b'],'g':['c'],'h':['c']}
tree={"A":["B","C","D"],"B":["A","E","F"],"C":["H"],"D":["I"],"E":["B","G"],"F":["B"],"H":["C","J","K","L"],"I":["D"],"G":["E"],"J":["H"],"K":["H"],"L":["H"]}
root="A"
weight={}
edge_tree={}
path_list={}
expr=" "
int_ptr=0
pos={}
reverse_pos={}
PathParentHead={root:root}
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

def HLD(tree,vertex,pathindex):
    global edge_tree,weight,int_ptr,Base_array,pos,last_vertex,reverse_pos
    if(pathindex!=-1):
        path_list[pathindex]+=[vertex]
        edge_tree[vertex]=pathindex
        pos[vertex]=int_ptr
        reverse_pos[int_ptr]=vertex
        int_ptr+=1
    else:
        pathindex=vertex
        path_list[pathindex]=[vertex]
        edge_tree[vertex]=pathindex
        pos[vertex]=int_ptr
        reverse_pos[int_ptr]=vertex
        int_ptr+=1
    preferred=-1
    val=-2
    for i in tree[vertex]:
        if(i not in edge_tree):
            if(weight[i]>val):
                preferred=i
                val=weight[i]
    if(preferred!=-1):
        HLD(tree,preferred,pathindex)
    for i in tree[vertex]:
        if(i not in edge_tree):
            HLD(tree,i,-1)            
def assign_weight(tree,vertex,visited):
        ma=-1
        global expr
        if(expr[-1]!=vertex):
           expr+=vertex
        visited.add(vertex)
        for j in tree[vertex]:
           if(j not in visited):
             PathParentHead[j]=vertex  
             ma=max(assign_weight(tree,j,visited),ma)
           if(expr[-1]!=vertex):
              expr+=vertex
        weight[vertex]=ma+1
        return ma+1
def level_ancestor(u,level,chain,pos,parent):
    global reverse_pos
    if(level==0):
        return u
    dist_above=pos[u]-pos[chain[u]]
    if(dist_above>=level):
        index=pos[u]-level
        return reverse_pos[index]
    else:
        while(dist_above<level):
            level-=dist_above
            level-=1
            u=parent[chain[u]]
            dist_above=abs(pos[u]-pos[chain[u]])
        index=pos[u]-level
        return reverse_pos[index]
def query_up(u,v,chain,tree,pos,parent):
    #v is ancestor of u
    vchain=chain[v]
    ans=0
    if(u==v):
        return tree.query(pos[v],pos[u])
    while(True):
        uchain=chain[u]
        if(uchain==vchain):
            if(u==v):
                break
            #print "length",abs(pos[v]-pos[u]),chain[v]  
            ans=max(ans,tree.query(pos[v],pos[u]))
            break
        ans=max(ans,tree.query(pos[chain[u]],pos[u]))
        u=parent[uchain]
    return ans
class LCA:
    def __init__(self,expr,weights):
        self.expr=expr
        self.weight=weights
        self.weighted_list=map(lambda w:weights[w],expr)
        self.tree=SG_Tree2(self.weighted_list)
    def find_lca(self,a,b):
        lis=sorted([self.expr.index(a),self.expr.index(b)])
        return expr[self.tree.query(lis[0],lis[1])]
class query_handler:
    def __init__(self,pos,weight,expr,chain,parent):
        self.chain_index=chain
        self.chain_parent=parent
        self.pos=pos
        self.weight=weight
        self.lis=[0]*len(pos)
        self.expr=expr
        self.LCA=LCA(self.expr,self.weight)
        for i in pos:
            self.lis[pos[i]]=weight[i]
        self.tree=SG_Tree(self.lis)
    def change_weight(self,a,weight):
        self.weight[a]=self.weight[a]+weight
        self.tree.update(self.pos[a],self.pos[a],weight) 
    def level(self,u,level):
        return level_ancestor(u,level,self.chain_index,self.pos,self.chain_parent)
    def query(self,u,v):
        lca=self.LCA.find_lca(u,v)
        print "max between  "+u+" and "+v+" is "
        return max(query_up(u,lca,self.chain_index,self.tree,self.pos,self.chain_parent),query_up(v,lca,self.chain_index,self.tree,self.pos,self.chain_parent))
def main():
  global expr,weight ,root 
  visited=set()    
  assign_weight(tree,root,visited)
  HLD(tree,root,-1)
  expr=expr[1:]
  lis=[]
  print weight["A"]
  print path_list
  QR=query_handler(pos,weight,expr,edge_tree,PathParentHead)
  print QR.query('G','I')
  print QR.level('J',2)
  QR.change_weight("E",5)
  print QR.query('G','I')
  """   
  for i in tree.keys()[1:2]:
    for j in tree.keys():
      print "\n"
      print QR.query(i,j)
  """    
main()
