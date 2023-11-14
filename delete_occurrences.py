# Task 1

# Given a list and a number, create a new list that contains 
# each number of list at most N times, without reordering.
# For example if the input number is 2, 
# and the input list is [1,2,3,1,2,1,2,3], 
# you take [1,2,3,1,2],
# drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, 
# and then take 3, which leads to [1,2,3,1,2,3].
# With list [20,37,20,21] and number 1, the result would be [20,37,21].


def delete_nth(order,max_e):
    result = []
    count_dict = {}

    for num in order:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

        if count_dict[num] <= max_e:
            result.append(num)
        
        print(result)

# Example usage:
input_list = [1, 2, 3, 1, 2, 1, 2, 3]
limit = 2
result = delete_nth(input_list, limit)
print(result)  # Output: [1, 2, 3, 1, 2]

input_list = [20, 37, 20, 21]
limit = 1
result = delete_nth(input_list, limit)
print(result)  # Output: [20, 37, 21]