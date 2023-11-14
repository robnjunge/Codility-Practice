# Implement the function unique_in_order 
# which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other
# and preserving the original order of elements.

def unique_in_order(sequence):
    return [item for i, item in enumerate(sequence) if i == 0 or item != sequence[i - 1]]

# Example usage:
# print(unique_in_order('AAAABBBCCDAABBB'))  
# print(unique_in_order('ABBCcAD'))          
# print(unique_in_order([1, 2, 2, 3, 3]))    
# print(unique_in_order((1, 2, 2, 3, 3))) 
