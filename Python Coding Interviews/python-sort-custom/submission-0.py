from typing import List

def sort_words(words: List[str]) -> List[str]:
    ## (key = len sorts by word length) (reverse = true)
    words.sort(key = len, reverse = True)     # sorting words (key = len)
    ## (reverse = True) makes it descending, longest to shortest
    return words
    # pass

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key = abs) ## sort list by absolute value
    return numbers
    # pass

## .sort() returns None
# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))