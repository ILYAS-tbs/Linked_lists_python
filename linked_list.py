
#! list Node : 

class Node: 
    
    def __init__(self , data):
        self.data = data 
        self.next = None 

    
    def __str__(self):
        return str(self.data)


#?-- first node (root)

root = Node(10)



#?-- second node : 
""" 
 node1 = Node(15)
 root.next = node1 
 """

print("ROOT : ", root) 
print(root.next) 


class Linked_list: 

    def __init__(self , node:Node): 
        self.root = node 
    
    def insert(self , data):
        
        x = self.root
        while (x.next != None ):
            x = x.next
        
        new_last_node = Node(data=data)
        x.next = new_last_node
    
    #! NOT A PURE FUNCTION ___ IT USES A VARIABLE FROM THE OUTSIDE 
    #! THATS WHY I DEFINED  FUNcTIONS  -- THE INNER IS PURE
    def length(self): 
        x = self.root

        def len_rec(x):
            if x is None:
                return 0 
            else : 
                return 1 + len_rec(x.next)
        
        return len_rec(x)
    
    #! PURE FUNCTION VERSION :
    def length_pure(self , x): 

        if x is None:
             return 0 
        else: 
            return 1 + self.length_pure(x.next)
        

    
    def find(self , data):
       
        x=self.root 

        while (x is not None):
            if (x.data == data ):
                return x 
            else:
                x=x.next
        
        return -1 
    
    def delete(self , data): 
        x:Node = self.root 
        
        #!todo : case of deleting the first elements (the root ):
        if (x.data == data):
            self.root=self.root.next 
            del x
        
        else:
            while  x is not None and x.next is not None:
                
                #! point on step / element before it 
                if (x.next.data == data ): 
                    temp = x.next
                    x.next = x.next.next 
                
                    #! dispose of it 
                    del temp
                
                x=x.next 

    #todo : read a list - read all 
    def __str__(self):
        result = []
        
        x=self.root
       
        while(x): 
            result.append(x.data)
            x=x.next 

        return str(result)


linked_list =Linked_list(root)

print(f"{linked_list} : len {linked_list.length()}")

linked_list.insert(7)
linked_list.insert(3)
linked_list.insert(20)
linked_list.insert(9)


print(f"{linked_list} : len {linked_list.length()} -- pure :{linked_list.length_pure(root)}")

linked_list.insert(77)
linked_list.insert(34)
linked_list.insert(240)
linked_list.insert(59)

print(f"{linked_list} : len {linked_list.length()} -- pure :{linked_list.length_pure(root)}")


print ( linked_list.find(59))

linked_list.delete(59)

print ( linked_list.find(59))

print(f"{linked_list} : len {linked_list.length()} -- pure :{linked_list.length_pure(linked_list.root)}")

linked_list.delete(7)
linked_list.delete(3)

linked_list.delete(240)

print(f"{linked_list} : len {linked_list.length()} pure :{linked_list.length_pure(linked_list.root)}")


#!  deleting the root : 
linked_list.delete(10)

print(f"{linked_list} : len {linked_list.length()} pure :{linked_list.length_pure(linked_list.root)}")

