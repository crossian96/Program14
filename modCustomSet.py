"""Description: This program is a custom set of methods for the set class, and includes a lot of overrides.


_author_ = 'Dakota Parks', 'Ian Cross', 'Suman Koirala'
_date_ = '4/22/2015'

"""

class CustomSet:
      def __init__(self, listOfNums):
            """Preconditions: Accepts list of nums, expected to be a list of ints.
               Description: This is a contructor that takes a list of nubmers and then returns a list without any duplicates
               Postconditions: An object of type CustomSet is created, which is a list"""
            self._newList=[]
            self._listOfNums=listOfNums
            for el in self._listOfNums:
                  if el not in self._newList:
                        self._newList.append(el)



