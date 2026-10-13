def get_first_element(arr):
    """
    Returns the first element of the given array.

    Parameters:
    arr (list): The input array.

    Returns:
    The first element of the array.
    """
    if not arr:
        return None  # Return None if the array is empty
    return arr[0]

gg=get_first_element([1, 2, 3, 4, 5])
print(gg)  # Output: 1