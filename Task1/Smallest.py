def find_first_repeating_element(arr):
    seen_elements = set()
    first_repeating = None
    for i in range(len(arr) - 1, -1, -1):
        element = arr[i]
        if element in seen_elements:
             first_repeating = element
        else:
            # If we haven't seen this element, add it to the set.
            seen_elements.add(element)
            
    return first_repeating

if __name__ == "__main__":
    # Test Case 1: A standard example
    arr1 = [10, 5, 3, 4, 3, 5, 6]
    result1 = find_first_repeating_element(arr1)
    print(f"Array: {arr1}")
    if result1 is not None:
        print(f"The first repeating element is: {result1}")
    else:
        print("No repeating element found.")
    
    print("-" * 30)

    # Test Case 2: No repeating elements
    arr2 = [6, 10, 5, 4, 9, 120]
    result2 = find_first_repeating_element(arr2)
    print(f"Array: {arr2}")
    if result2 is not None:
        print(f"The first repeating element is: {result2}")
    else:
        print("No repeating element found.")

    print("-" * 30)
    
    # Test Case 3: An empty list
    arr3 = []
    result3 = find_first_repeating_element(arr3)
    print(f"Array: {arr3}")
    if result3 is not None:
        print(f"The first repeating element is: {result3}")
    else:
        print("No repeating element found.")