"""Description: This program is a custom set of methods for the set class, and includes a lot of overrides.


_author_ = 'Dakota Parks', 'Ian Cross', 'Suman Koirala'
_date_ = '4/22/2015'

"""

class CustomSet:
      def __init__(self, listOfNums):
            """Preconditions: Accepts list of nums, expected to be a list of ints.
               Description: This is a contructor that takes a list of numbers and then returns a list without any duplicates
               Postconditions: An object of type CustomSet is created, which is a list"""
            self._newList=[]
            self._listOfNums=listOfNums
            for el in self._listOfNums:
                  if el not in self._newList:
                        self._newList.append(el)
      def contains(self, member):
            """Preconditions: Accepts self and member, expected to be an int or string.
               Description: This method overrides "in" and looks for the specific member in the set.
               Postconditions: Prints either "Yes" or "Not there"."""
            if member in self._listOfNums:
                  print("Yes")
            elif member not in self._listOfNums:
                  print("Not there")

      def __str__(self):
            """Preconditions: Only recieves self.
               Description: Prints a string of the customset object.
               Postconditions: Nothing, only returns a string."""
            return(str(self._listOfNums))

      def brackets(self):
            """Preconditions: Only recieves self.
               Description: Prints a string of the customset object surrounded by brackets.
               Postconditions: Nothing, returns a string."""
            return("{ "+str(self)+" }")
      
      def __ge__(self,other):
            """
            Description: If one number is greater than other or not
            Preconditions: Two Values of datatype Customset.
            Postcondition:None
            """            
            if self._newList >= other._newList:
               return "Yes"
            else:
               return "No Subset"
        
      def __le__(self,other):
            """
            Description: If one number is less than other or not.
            Precondition: Two values of datatype CuustomerSet.
            PostCondition:None
            """            
            if self._newList <= other._newList:             
               return "Yes"
            else:
               return "No Subset"
      def __len__(self):
            """
            Description: Find the len of given list.
            Precondition:none
            postcondition:none
            """
            return len(self._newList)



