# Calendar Debugging and Fixing

## Overview

This document provides the debugging process undertaken to fix the `calendar.py` code file. The original implementation tried to create a calendar system that prevents double bookings by ensuring that no two events overlap in time. However, existing code had logical issues that prevented it from giving expected output. This README details the step-by-step debugging process, identifies the underlying problems, and explains the solutions implemented to rectify them.

## Original Code Analysis

### 1. Understanding the Original Implementation

#### Classes Defined:

- **Node**: Represents an event with start and end times. It also has `left_child` and `right_child` pointers.
- **Calendar**: Manages the calendar by maintaining a root `Node` and providing a `book` method to schedule events.

#### Booking Logic (`Node.insert`):

- Attempts to insert a new event into the BST (Binary Search Tree).
- Checks if the new event's start time is less than or equal to the current node's end time.
- If so, it tries to insert into the `right_child`.
- Otherwise, it tries to insert into the `left_child`.

### 2. Identified Issues

#### Incorrect Overlap Detection:

The original `insert` method did not correctly check for overlapping events. The process of checking the start and end times was incorrect.

#### Type Hint Inconsistencies:

In the `Calendar` class, `self.root` was given a type of `Node`, but it was initialized as `None`. This will lead to error since `None` is not an instance of `Node`.

#### Logical Errors in BST Insertion:

The logic of inserting into the `left_child` or `right_child` was incorrect.

#### Missing Import:

The original code used `Optional` in types but did not import it from the `typing` module, which will give `NameError`.

## Debugging Process

### Step 1: Reviewing the Original Code

**Objective**: Understand the expected functionality and identify the incorrect logic.

**Action**: Understand `Node` and `Calendar` classes to understand how events are being inserted and checked for overlaps.

### Step 2: Identifying Logical Flaws

#### Issue with Overlap Detection:

The condition `if node.start <= self.end` is not correct for detecting overlaps. It will pass events where the new event starts before the current event ends but doesn't overlap.

#### Incorrect BST Property Maintenance:

The original insertion logic doesn't correctly place events in the BST based on their start and end times, leading to overlaps.

### Step 3: Analyzing Type Hints and Imports

#### Type Hint Mismatch:

`self.root` in `Calendar` is given a type hint as `Node` but is initialized as `None`. The correct type hint should allow for `None`, that is, `Optional[Node]`.

#### Missing Imports:

`Optional` is used in types but not imported, which would give a `NameError`.

### Step 4: Correcting Overlap Detection Logic

**Proper Overlap Condition**:

Two events `[start1, end1)` and `[start2, end2)` do not overlap if `end1 <= start2` or `end2 <= start1`. Therefore, the overlapping condition is not `(end1 <= start2 or end2 <= start1)`.

### Step 5: Revising the BST Insertion Logic

#### Left and Right Subtrees:

- **Left Subtree Insertion**: Events that end before the current event's start should go to the left subtree.
- **Right Subtree Insertion**: Events that start after the current event's end should go to the right subtree.
- **Overlap Detection**: Any other condition indicates an overlap.

### Step 6: Implementing Type Hint Corrections and Imports

#### Importing `Optional`:

```python
from typing import Optional
```
Added the necessary import for Optional.

### Adjusting Type Hints:
```python
self.root: Optional[Node] = None
```
Updated the type hint for self.root to allow None.

### Step 7: Testing with Example Inputs
**Test Cases:**
Verify the corrected code with the provided example inputs to ensure it behaves as expected.
Additional test cases are added to cover edge scenarios.
## Implemented Solutions
- **Corrected Overlap Detection**
    ```python
    
    if not (node.end <= self.start or node.start >= self.end):
        return False  # Overlapping event found
    ```
    This condition accurately detects overlapping events by ensuring that there is no overlap only if one event ends before the other starts.

- **Fixed BST Insertion Logic**
    Left Subtree Insertion: If the new event ends before the current event starts, attempt to insert into the left subtree.
    Right Subtree Insertion: If the new event starts after the current event ends, attempt to insert into the right subtree.
- **Type Hint Corrections and Imports**
    ```python
    
    from typing import Optional
    Added the necessary import for Optional.
    ```

    ```python
    
    self.root: Optional[Node] = None
    Updated the type hint for self.root to allow None.
    ```

- **Additional Enhancements**
    Documentation: Added docstrings to classes and methods for better clarity and maintainability.
    Test Cases: Expanded the test cases to include more scenarios, ensuring comprehensive testing of the calendar functionality.
## Conclusion
By meticulously analyzing the original implementation, identifying logical and structural issues, and applying targeted corrections, the calendar.py module now functions as intended. The corrected code accurately prevents double bookings by ensuring that no two events overlap and maintains a proper binary search tree structure for efficient event management.

The inclusion of detailed documentation and comprehensive test cases further enhances the reliability and maintainability of the calendar system.





