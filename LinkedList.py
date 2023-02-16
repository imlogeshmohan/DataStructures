from Node import node

class LinkedList:

    def __init__(self):

        self.head = None
        self.n = 0

    def __len__(self):
        return self.no
    
    def insert_head(self,value):

        new_node = node(value)

        new_node.next = self.head

        self.head = new_node

        self.n = self.n + 1

    def __str__(self):

        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + "->"
            curr = curr.next

        return result[:-2]
    
    def append(self, value):
        new_node = node(value)

        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return 
        
        curr  = self.head

        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n = self.n +1

    def insert(self,after , value):
        new_node = node(value)

        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        
        if curr != None:
            new_node.next = curr.next

            curr.next = new_node
            self.n = self.n +1 
        else :
            print("Item not found")

    def clear(self):
        self.head = None
        self.n = 0

    def del_head(self):
        if self.head == None:
            return
        self.head = self.head.next 
        self.n = self.n -1

    def pop(self):
        if self.head == None:
            print("Empty list")
            return
        curr = self.head 

        if curr.next == None:
            self.del_head()
            return 
        
        while curr.next.next != None:
            curr = curr.next

        curr.next = None
        self.n = self.n -1

    def remove(self, value):

        if self.head == None:
            return print("Empty LL")

        curr = self.head

        if curr.data == value:
            return self.del_head()

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        
        if curr.next == None:
            print("Not Found")
            return

        curr = curr.next.next

    def search(self, Value):

        curr = self.head
        pos = 0

        while curr != None:
            if curr.data == Value:
                return pos
            curr = curr.next
            pos = pos+1
        
        return f"{Value} Not Found"
    
    def __getitem__(self, index):

        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos+1

        return "not Found"

    def replace_max(self, value):

        curr = self.head
        max = curr

        while curr != None:
            if max.data < curr.data:
                max = curr
            curr = curr.next
        
        max.data = value

    def Odd_pos(self):

        result = 0
        curr = self.head
        pos = 0

        while curr != None:
            if pos%2 !=0 :
                result = result + curr.data
            
            curr = curr.next
            pos= pos+1
        
        return result
    
    def reverse(self):

        per_node = None
        curr_node = self.head

        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = per_node

            per_node = curr_node
            curr_node = next_node

        self.head = per_node

    def simple_print(self):

        curr = self.head
        result = ""

        while curr !=None:
            result = result+curr.data

            curr = curr.next
        return result

    def sentance_changer(self):

        curr = self.head
        
        while curr != None:

            if curr.data == '*' or curr.data == "/":
                curr.data = " "

                if curr.next.data == "*" or curr.next.data == "/":
                    curr.next.next.data = curr.next.next.data.upper()
                    curr.next = curr.next.next

            curr = curr.next



        


a = LinkedList()

# a.insert_head(1)
# a.insert_head(2)
# a.insert_head(6)
# a.insert_head(4)
# a.append(5)
# a.insert(5,8)
# print(a)
# a.reverse()
# # a.replace_max(2)
# print(a)

a.append("T")
a.append("h")
a.append("e")
a.append("/")
a.append("*")
a.append("s")
a.append("k")
a.append("y")
a.append("*")
a.append("i")
a.append("s")
a.append("/")
a.append("/")
a.append("b")
a.append("l")
a.append("u")
a.append("e")

print(a.simple_print())
a.sentance_changer()
print(a.simple_print())