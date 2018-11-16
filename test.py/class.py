
class book:
      def __init__(self,pages):
          self.pages=pages


      def __add__(self,others):
          return self.pages+others.pages


      def __sub__(self,others):
          return self.pages-others.pages
      def __mul__(self,others):
          return self.pages*others.pages




b1=book(200)
b2=book(300)
print(b1+b2)        
print(b1*b2) 
print(b1*b2)