class Hashtable:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.MAX

    # def add(self,key,val):
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val

    # def get(self,key):
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr=None

t=Hashtable()
# print(t.add('march 6',130))
t['march 6']=130 # --> __setitem__()
t['march 10']=20
print(t.arr)
# print(t.get('march 6'))
t['march 6'] # --> __getitem__()
print(t.arr)
del t['march 6']
print(t.arr)