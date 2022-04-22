# Implementing Red-Black Tree in Python

class Node():
    def _init_(self,value):
        self.value = value                               
        self.parnt = None                               
        self.l = None                                 
        self.r = None                                
        self.color = 1                                  


class RedBlackTree():
    def _init_(self):
        self.null = Node ( 0 )
        self.null.color = 0
        self.null.l = None
        self.null.r = None
        self.root = self.null

    def insertNode(self, key):
        node = Node(key)
        node.parnt = None
        node.value = key
        node.l = self.null
        node.r = self.null
        node.color = 1                                   

        y = None
        x = self.root

        while x != self.null :                           
            y = x
            if node.val < x.value :
                x = x.l
            else :
                x = x.r

        node.parnt = y                                  
        if y == None :                                  
            self.root = node
        elif node.value < y.value :                          
            y.l = node
        else :
            y.r = node

        if node.parnt == None :                         
            node.color = 0
            return

        if node.parnt.parnt == None :                  
            return

        self.fixInsert ( node )                          


    def minimum(self, node):
        while node.l != self.null:
            node = node.l
        return node


   
    def LR ( self , x ) :
        y = x.r                                     
        x.r = y.l                               
        if y.l != self.null :
            y.l.parnt = x

        y.parnt= x.parnt                             
        if x.parnt == None :                            
            self.root = y                               
        elif x == x.parnt.l :
            x.parnt.l = y
        else :
            x.parnt.r = y
        y.l = x
        x.parnt = y


    
    def RR ( self , x ) :
        y = x.l                                      
        x.l = y.r                                
        if y.r != self.null :
            y.r.parnt = x

        y.parnt = x.parnt                           
        if x.parnt == None :                          
            self.root = y                                
        elif x == x.parnt.r :
            x.parnt.r = y
        else :
            x.parnt.l = y
        y.r = x
        x.parent = y


   
    def fixInsert(self, k):
        while k.parnt.color == 1:                        
            if k.parnt == k.parnt.parnt.r:       
                u = k.parnt.parnt.l                
                if u.color == 1:                         
                    u.color = 0                          
                    k.parnt.color = 0
                    k.parnt.parnt.color = 1            
                    k = k.parnt.parnt                  
                else:
                    if k == k.parnt.l:                
                        k = k.parnt
                        self.RR(k)                       
                    k.parnt.color = 0
                    k.parnt.parnt.color = 1
                    self.LR(k.parnt.parnt)
            else:                                         
                u = k.parnt.parnt.right               
                if u.color == 1:                        
                    u.color = 0                          
                    k.parnt.color = 0
                    k.parnt.parnt.color = 1             
                    k = k.parnt.parnt                  
                else:
                    if k == k.parnt.r:             
                        k = k.parnt
                        self.LR(k)                        
                    k.parnt.color = 0
                    k.parnt.parnt.color = 1
                    self.RR(k.parnt.parnt)              
            if k == self.root:                            
                break
        self.root.color = 0                               
    def fixDelete ( self , x ) :
        while x != self.root and x.color == 0 :           
            if x == x.parnt.l :                       
                s = x.parnt.r                      
                if s.color == 1 :                         
                    s.color = 0                          
                    x.parnt.color = 1                    
                    self.LR ( x.parnt )                  
                    s = x.parnt.r
               
                if s.l.color == 0 and s.r.color == 0 :
                    s.color = 1                           
                    x = x.parnt
                else :
                    if s.r.color == 0 :              
                        s.l.color = 0                  
                        s.color = 1                       
                        self.RR ( s )                     
                        s = x.parnt.r

                    s.color = x.parnt.color
                    x.parnt.color = 0                    
                    s.r.color = 0
                    self.LR ( x.parnt )                  
                    x = self.root
            else :                                        
                s = x.parnt.l                        
                if s.color == 1 :                         
                    s.color = 0                          
                    x.parnt.color = 1                    
                    self.RR ( x.parnt )                 
                    s = x.parnt.l

                if s.r.color == 0 and s.r.color == 0 :
                    s.color = 1
                    x = x.parnt
                else :
                    if s.l.color == 0 :                
                        s.r.color = 0                 
                        s.color = 1
                        self.LR ( s )                    
                        s = x.parnt.l

                    s.color = x.parnt.color
                    x.parnt.color = 0
                    s.l.color = 0
                    self.RR ( x.parnt )
                    x = self.root
        x.color = 0


   
    def __rb_transplant ( self , a , b ) :
        if a.parnt == None :
            self.root = b
        elif a == a.parnt.l :
            a.parnt.l = b
        else :
            a.parnt.r = b
        b.parnt = a.parnt


    
    def delete_node_helper ( self , node , key ) :
        z = self.null
        while node != self.null :                         
            if node.value == key :
                z = node

            if node.value <= key :
                node = node.r
            else :
                node = node.l

        if z == self.null :                               
            print ( "Value not present in Tree " )
            return

        y = z
        y_original_color = y.color                         
        if z.l == self.null :                           
            x = z.r                                   
            self.__rb_transplant ( z , z.r)           
        elif (z.r == self.null) :                       
            x = z.l                                      
            self.__rb_transplant ( z , z.l )             
        else :                                              
            y = self.minimum ( z.r )                    
            y_original_color = y.color                     
            x = y.r
            if y.parnt == z :                             
                x.parnt = y                                
            else :
                self.__rb_transplant ( y , y.r )
                y.r = z.r
                y.r.parnt = y

            self.__rb_transplant ( z , y )
            y.l = z.l
            y.l.parnt = y
            y.color = z.color
        if y_original_color == 0 :                         
            self.fixDelete ( x )


   
    def delete_node ( self , val ) :
        self.delete_node_helper ( self.root , val )        

   
    def __printCall ( self , node , indent , last ) :
        if node != self.null :
            print(indent, end=' ')
            if last :
                print ("R--",end= ' ')
                indent += "     "
            else :
                print("L--",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.val ) + "(" + s_color + ")" )
            self.__printCall ( node.l , indent , False )
            self.__printCall ( node.r , indent , True )

   
    def print_tree ( self ) :
        self.__printCall ( self.root , "" , True )


if __name__ == "_main_":
    bst = RBTree()

    bst.insertNode(8)
    bst.insertNode(18)
    bst.insertNode(28)
    bst.insertNode(5)
    bst.insertNode(4)
    bst.insertNode(2)

    bst.print_tree()

    print("\nAfter deleting element")
    bst.delete_node(2)
    bst.print_tree()
