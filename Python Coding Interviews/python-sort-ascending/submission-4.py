from typing import List
## .sort() changes the original list directly. 
   # It does not return the sorted list.
   # That is why this is wrong: return words.sort()
     # because .sort() returns None.
## So the correct pattern is always:
   # list_name.sort()
   # return list_name

def sort_words(words: List[str]) -> List[str]:
    words.sort()
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort()
    return numbers

def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort()
    return numbers

# Testing above functions
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))
print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))
print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))

## Time Complexity: O(n log n)
## Space Complexity O(n)