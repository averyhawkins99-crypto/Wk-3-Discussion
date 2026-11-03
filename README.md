# Unit 3 Discussion: List Operations

## Overview
This assignment examined insertion, deletion, and searching operations in Python lists, specifically focusing on element memory shifting and performance impacts across different positions.

## Learning Objectives
- Inserted values into a list
- Deleted values from a list
- Searched for values in a list
- Analyzed list behavior and performance benchmarks

## Completed Requirements

1. **Tested Insertion at Multiple Positions**
   - Inserted an element at the beginning (index 0), which required shifting all pre-existing elements to the right in memory ($O(n)$ complexity).
   - Inserted an element in the middle, demonstrating an average-case memory shift of half the list size ($O(n)$ complexity).
   - Inserted an element at the end of the list using the length of the list, which executed efficiently without shifting any elements ($O(1)$ complexity).

2. **Tested Deletion at Multiple Positions**
   - Implemented an index-validated deletion sequence that securely removed elements using standard Python list operations.
   - Deleted from the beginning and middle positions, causing subsequent items to slide left to fill memory gaps.
   - Deleted from the end of the list, which completed with zero element-shifting overhead.

3. **Searched for Existing and Missing Values**
   - Executed a linear search function that scanned the list sequentially from index 0 onward.
   - Successfully located a valid target item and returned its accurate index.
   - Verified that missing items safely returned a `-1` indicator after checking every element.

4. **Demonstrated Edge Cases**
   - Tested handling an invalid, out-of-bounds deletion index, confirming that the defensive bounds-checking logic prevented runtime errors.
   - Tested an insertion sequence starting from a completely empty list layout.

5. **Created a Real-World Scenario**
   - Modeled an undo action history log inside a simulated text editor environment. 
   - Demonstrated how logging new actions at the end operates with optimal speed, while forcing size limits by purging old history from the front introduces structural performance delays.
