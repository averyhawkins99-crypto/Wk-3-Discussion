def insert_at(lst, index, value):
    """
    Inserts a value into the list at the specified index.
    """
    # Requirement: Use a list operation to insert the value.
    lst.insert(index, value)

    # Requirement Comments:
    # 1. What happens to existing elements:
    #    When an item is inserted, Python must shift all existing elements at and to
    #    the right of the specified index one position to the right in memory.
    #
    # 2. How insertion performance varies by position:
    #    - Beginning (index 0): Worst-case scenario (O(n) time) because every item shifts.
    #    - Middle: Average-case scenario (O(n) time) because roughly half the elements shift.
    #    - End (index len(lst)): Best-case scenario (O(1) amortized time) because zero items shift.
    pass

def delete_at(lst, index):
    """
    Removes and returns the value at the specified index.
    """
    # Requirement: Validate that the index exists.
    if 0 <= index < len(lst):
        # Requirement: Return the removed value.
        removed_value = lst.pop(index)

        # Requirement Comments:
        # Index validation prevents application crashes caused by IndexError.
        # Safe deletion ensures the program gracefully handles bad inputs. Like insertion,
        # deleting from the beginning or middle triggers memory shifts to close the gap (O(n)),
        # while deleting from the end requires no shifting (O(1)).
        return removed_value

    # Requirement: Return None if the index is invalid.
    return None

def search_value(lst, value):
    """
    Searches for a value within the list.
    """
    # Requirement: Iterate through the list to look for the value.
    for i in range(len(lst)):
        if lst[i] == value:
            # Requirement: Return the index if the value is found.
            return i

    # Requirement Comments:
    # This is a linear search because it scans sequentially, one element at a time, from index 0
    # to the end. It must check elements in order because a standard Python list is unsorted;
    # the target value could be anywhere. Worst-case complexity is O(n).

    # Requirement: Return -1 if the value is not found.
    return -1

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    print("\n=== INSERTION TESTS ===")

    # 1. Create a list containing several values.
    my_list = [10, 20, 30, 40]

    # 2. Display the original list.
    print(f"Original list: {my_list}")

    # 3. Test insertion at the beginning.
    print("\nInserting 5 at the beginning (index 0)...")
    insert_at(my_list, 0, 5) # All original elements shift right.
    print(f"Updated list: {my_list}")

    # 3. Test insertion in the middle.
    print("\nInserting 25 in the middle (index 3)...")
    insert_at(my_list, 3, 25) # Elements at index 3+ shift right.
    print(f"Updated list: {my_list}")

    # 3. Test insertion at the end.
    print("\nInserting 50 at the end (index len(lst))...")
    insert_at(my_list, len(my_list), 50) # Efficient O(1) operation; no elements shift.
    print(f"Updated list: {my_list}")


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    print("\n=== DELETION TESTS ===")
    print(f"Current list before deletions: {my_list}")

    # 1. Delete an item from the beginning.
    del_val = delete_at(my_list, 0)
    print(f"Removed value from beginning: {del_val}")
    print(f"Updated list: {my_list}") # Elements shift left to fill the gap.

    # 1. Delete an item from the middle.
    del_val = delete_at(my_list, 2)
    print(f"\nRemoved value from middle (index 2): {del_val}")
    print(f"Updated list: {my_list}") # Later elements shift left.

    # 1. Delete an item from the end.
    del_val = delete_at(my_list, len(my_list) - 1)
    print(f"\nRemoved value from end: {del_val}")
    print(f"Updated list: {my_list}") # O(1) operation; no elements shift.


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")

    # 1. Search for a value that exists.
    target_exist = 30
    idx_found = search_value(my_list, target_exist)
    print(f"Searching for existing value '{target_exist}'...")
    print(f"Result index: {idx_found} (Found sequentially)")

    # 2. Search for a value that does not exist.
    target_missing = 99
    idx_missing = search_value(my_list, target_missing)
    print(f"\nSearching for missing value '{target_missing}'...")
    print(f"Result index: {idx_missing} (Scanned entire list, item not present)")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge Case 1: Delete using an invalid index
    print("Edge Case 1: Attempting to delete from an out-of-bounds index (index 100)...")
    invalid_del = delete_at(my_list, 100)
    print(f"Returned value: {invalid_del} (Safe handling successful)")

    # Edge Case 2: Insert into an empty list
    empty_list = []
    print("\nEdge Case 2: Inserting into an entirely empty list at index 0...")
    insert_at(empty_list, 0, 999)
    print(f"Empty list after insertion: {empty_list}")


    # ====================================
    # TODO (Student): REAL-WORLD SCENARIO
    # ====================================
    print("\n=== REAL-WORLD SCENARIO: UNDO HISTORY BLOCK ===")
    # Simulating a basic text editor's action log history.
    # Appending actions is fast (at the end), but clearing old history from the front forces shifts.
    action_log = ["Type 'Hello'", "Bold Text", "Underline Text"]
    print(f"Initial text editor action log: {action_log}")

    # User performs a new action (Fast O(1) Append at the end)
    print("\nUser types another word (Adding to end of history)...")
    insert_at(action_log, len(action_log), "Type 'World'")
    print(f"Action log: {action_log}")

    # System limits log size by purging the oldest entry (O(n) Shift from the front)
    print("\nSystem clean-up: Purging oldest history event from the front...")
    purged = delete_at(action_log, 0)
    print(f"Purged old action: {purged}")
    print(f"Final Action log: {action_log}")

if __name__ == "__main__":
    main()
