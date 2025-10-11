'''
# Python: Multiset Implementation

## Question

A multiset is the same as a set except that an element might occur more than once in a multiset. Implement a multiset data structure in Python. Given a template for the Multiset class, implement 4 methods:

- `add(self, val)`: adds val to the multiset
- `remove(self, val)`: if val is in the multiset, removes val from the multiset; otherwise, do nothing
- `__contains__(self, val)`: returns True if val is in the multiset; otherwise, it returns False
- `__len__(self)`: returns the number of elements in the multiset

The implementations will be tested by operations:
- add val: calls add(val) on the Multiset instance
- remove val: calls remove(val) on the Multiset instance
- query val: appends the result of expression val in m, where m is an instance of Multiset
- size: calls len(m), where m is an instance of Multiset, and appends the returned value to the result list

Complete the class Multiset with the 4 methods given above (add, remove, __contains__, and __len__).

## Constraints
- 1 ≤ number of operations in one test file ≤ 10⁵
- if val is a parameter of operation, then val is an integer and 1 ≤ val ≤ 10⁹
'''

class Multiset:
    def __init__(self):
        """Initialize an empty multiset using a dictionary to store element counts."""
        self.data = {}
    
    def add(self, val):
        """
        Adds val to the multiset.
        
        Args:
            val: The value to add to the multiset
        """
        if val in self.data:
            self.data[val] += 1
        else:
            self.data[val] = 1
    
    def remove(self, val):
        """
        If val is in the multiset, removes one occurrence of val from the multiset.
        Otherwise, does nothing.
        
        Args:
            val: The value to remove from the multiset
        """
        if val in self.data:
            self.data[val] -= 1
            if self.data[val] == 0:
                del self.data[val]
    
    def __contains__(self, val):
        """
        Returns True if val is in the multiset; otherwise, returns False.
        
        Args:
            val: The value to check for in the multiset
            
        Returns:
            bool: True if val is in the multiset, False otherwise
        """
        return val in self.data
    
    def __len__(self):
        """
        Returns the number of elements in the multiset (counting duplicates).
        
        Returns:
            int: Total number of elements in the multiset
        """
        return sum(self.data.values())


# Example usage and testing
if __name__ == "__main__":
    m = Multiset()
    
    # Test adding elements
    m.add(5)
    m.add(5)
    m.add(3)
    m.add(7)
    
    print(f"Length: {len(m)}")  # Should print 4
    print(f"Contains 5: {5 in m}")  # Should print True
    print(f"Contains 2: {2 in m}")  # Should print False
    
    # Test removing elements
    m.remove(5)
    print(f"Length after removing one 5: {len(m)}")  # Should print 3
    print(f"Contains 5: {5 in m}")  # Should still print True (one 5 remains)
    
    m.remove(5)
    print(f"Contains 5 after removing second: {5 in m}")  # Should print False
    
    m.remove(10)  # Remove non-existent element (should do nothing)
    print(f"Length after trying to remove non-existent: {len(m)}")  # Should print 2