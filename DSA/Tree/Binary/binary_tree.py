class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return
        
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTree(data)

    def search(self,val):
        if self.data==val:
            return True
        
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        else:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements+=self.right.in_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order_traversal()

        if self.right:
            elements+=self.right.post_order_traversal()

        elements.append(self.data)

        return elements
    
    def pre_order_traversal(self):
        elements=[self.data]

        if self.left:
            elements+=self.left.pre_order_traversal()

        if self.right:
            elements+=self.right.pre_order_traversal()

        return elements
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def cal_sum(self):
        sum=0
        for i in range(len(elements)):
                sum += elements[i]

        return sum

    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            # min_val=self.right.find_min()
            # self.data=min_val
            # self.right=self.right.delete(min_val)

            max_val=self.left.find_max()
            self.data=max_val
            self.left=self.left.delete(max_val)

        return self
    
def build_tree(elements):
    print("Building tree with these elemnts",elements)
    root=BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    # countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    # country_tree = build_tree(countries)

    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))

    elements=[17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(elements)
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("Pre order traversal gives this sorted list:",numbers_tree.pre_order_traversal())
    print("Post order traversal gives this sorted list:",numbers_tree.post_order_traversal())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.cal_sum())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]