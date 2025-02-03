

```python
def two_sum(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return True  # Found a pair that sums to the target
        elif current_sum < target:
            left += 1  # Increase the left pointer to get a larger sum
        else:
            right -= 1  # Decrease the right pointer to get a smaller sum
            
    return False  # No such pair found

# Example Usage
arr = [1, 3, 4, 6, 10, 15]
target = 10
print(two_sum(arr, target))  # Output: True (because 6 + 4 = 10)
```

#### reverse array
```python
def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap the elements at left and right
        arr[left], arr[right] = arr[right], arr[left]
        
        # Move the pointers towards each other
        left += 1
        right -= 1
    
    return arr

# Example Usage
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))  # Output: [5, 4, 3, 2, 1]
```

#### remove duplicates (sorted arr)l.

```python
def remove_duplicates(arr):
    if not arr:
        return 0  # Return 0 if the array is empty
    
    # Pointer `i` to store the index of the next unique element
    i = 0
    
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]  # Move the unique element to the next position
    
    # The length of the array without duplicates is i + 1
    return i + 1

# Example Usage
arr = [1, 1, 2, 3, 3, 4, 5, 5]
new_length = remove_duplicates(arr)
print(new_length)  # Output: 5 (because unique elements are [1, 2, 3, 4, 5])
print(arr[:new_length])  # Output: [1, 2, 3, 4, 5]

```

Input: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 10
Output: [[1, 9], [2, 8], [3, 7], [4, 6]]
```python
    def pair_sum(arr):
        if not arr:
            return 0
            # checks for empty array
        left = 0
        right = len(arr) - 1
        while (left < right):
            

