from Node import node

class stack:

    def __init__(self):
        self.top = None
        self.n = 0

    def isempty(self):
        return self.top == None

    def push(self,value):

        new_stack = node(value)

        new_stack.next = self.top

        self.top = new_stack
        self.n = self.n +1

    def __str__(self):

        curr  = self.top
        result = ""

        while curr != None:
            result = result + str(curr.data) + " "
            curr = curr.next

        return result

    def peek(self):
        if self.isempty():
            return "Stack Empty"
        return self.top.data

    def pop(self):
        if self.isempty():
            return "stack Empty"
        
        curr = self.top

        self.top = self.top.next
        self.n = self.n -1

        return curr.data

    def size(self):
        return self.n


def reverse_str(text):
    a= stack()

    result = ""
    for i in text:
        a.push(i)

    while not a.isempty():
        result = result +  str(a.pop())

    return result
        
def text_editor(text , patten):
    u = stack()
    r = stack()
    res = ""

    for i in text:
        u.push(i)

    for i in patten:

        if i == "u":
            data = u.pop()
            r.push(data)
        if i == "r":
            data = r.pop()
            u.push(data)

    while not u.isempty():
        res = res + u.pop()

    return res

def celebrity(L):
    a = stack()

    for i in range(len(L)):
        a.push(i)

    while a.size() >= 2:
        i = a.pop()
        j = a.pop()

        if L[i][j] == 0:
            a.push(i)

        else:
            a.push(j)

    celeb = a.pop()

    for i in range(len(L)):

        if i != celeb:
            if L[i][celeb] == 0 or L[celeb][i] == 1:
                return "No one is celeb"

    return f"{celeb} is a celebrity"


def balanced_bracket(prob):
    a = stack()

    for x in prob:
        if x == "[" or x == "{" or x == "(":
            a.push(x)

        brakat = a.peek()

        if x == ")" and brakat != "(":
            return False
        elif x == "}" and brakat != "{":
            return False
        elif x == "]" and brakat != "[":
            return False
        
        elif x== "}" or x == "]" or x == ")":
            a.pop()

    if a.isempty():
        return True
    else :
        return False

print(balanced_bracket("[]"))

# s = stack()

L = [
    [0,0,1,0],
    [0,1,1,1],
    [0,0,0,0],
    [1,0,1,0]
]
# print(s.isempty())
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# print(s.isempty())
# print(s)
# print(s.peek())
# # print(reverse_str("logesh"))
# # print(text_editor("logesh" , "uuru"))

# print(celebrity(L))