import ctypes

class LoguList:

    def __init__(self):
        self.size = 1
        self.n = 0

        self.A = self.__make__array(self.size)

    def __make__array(self, capacity):
        return (capacity*ctypes.py_object)() 
    
    def append(self,item):

        if self.size == self.n:
            self.__resize()
        
        self.A[self.n] = item  
        self.n = self.n + 1

    def __resize(self):
        tempA = self.__make__array(self.size+8)
        self.size = self.size+8

        for x in range(self.n):
            tempA[x] = self.A[x]

        self.A = tempA

    def find(self, search):

        for x in range(self.n):
            if self.A[x] == search:
                return x
                
        return (f"Value Error {search} not in List")

    def __len__(self):
        
        return self.n
    
    def clear(self):
        self.n = 0
        self.size = 1

    def inset(self, ind, item):

        if self.size == self.n:
            self.__resize()
        
        for x in range(self.n, ind, -1):
            self.A[x] = self.A[x-1]

        self.A[ind] = item
        self.n = self.n +1

    def __delitem__(self,pos):

        if 0<= pos < self.n:
            for x in range(pos, self.n-1):
                self.A[x] = self.A[x+1]

            self.n = self.n - 1

    def remove(self, item):
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

    def __str__(self):
        result = ''

        for x in range(self.n):
            result = result + str(self.A[x]) + ","
        
        return (f"[{result[:-1]}]")
    

L = LoguList()
L.append(2)
L.append("hello")
L.append("Logu")
L.append(2.8)
print(L)
# print(L.find("logu"))
L.inset(1,"hey")
print(L)
L.remove("Logu")
print(L)