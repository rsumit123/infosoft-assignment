# FIXED CODE
from typing import Optional

class Node:
    """
    Represents an event in the calendar with a start and end time.
    """
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.left_child: Optional['Node'] = None
        self.right_child: Optional['Node'] = None

    def insert(self, node: 'Node') -> bool:
        """
        Attempts to insert a new event into the binary search tree without causing a double booking.

        Args:
            node (Node): The new event to be inserted.

        Returns:
            bool: True if the event was successfully inserted, False if it causes a double booking.
        """
        # If the new event starts before the current event ends and ends after the current event starts, it's a conflict
        if not (node.end <= self.start or node.start >= self.end):
            return False  # Overlapping event found

        # Insert into the left subtree
        if node.end <= self.start:
            if self.left_child is None:
                self.left_child = node
                return True
            else:
                return self.left_child.insert(node)
        else:
            # Insert into the right subtree
            if self.right_child is None:
                self.right_child = node
                return True
            else:
                return self.right_child.insert(node)

class Calendar:
    """
    Calendar system to schedule events without double bookings.
    """
    def __init__(self):
        self.root: Optional[Node] = None

    def book(self, start: int, end: int) -> bool:
        """
        Attempts to book a new event.

        Args:
            start (int): Start time of the event.
            end (int): End time of the event.

        Returns:
            bool: True if the event was successfully booked, False otherwise.
        """
        new_node = Node(start, end)
        if self.root is None:
            self.root = new_node
            return True
        else:
            return self.root.insert(new_node)

# Test Cases
if __name__ == "__main__":
    calendar = Calendar()
    
    # Test Cases
    test_cases = [
        (5, 10, True),
        (8, 13, False),
        (10, 15, True),
        (15, 20, True),
        (0, 5, True),
        (3, 4, False),
        (20, 25, True),
        (25, 30, True),
        (24, 26, False)
    ]
    
    for start, end, expected in test_cases:
        result = calendar.book(start, end)
        print(f"calendar.book({start}, {end}) -> {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")
