#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    - boxes: A list of lists where each list represents
    a box and contains keys to other boxes.

    Returns:
    - True if all boxes can be opened, False otherwise.
    """
    # Get the total number of boxes
    n = len(boxes)

    # Set to keep track of opened boxes (starting with box 0)
    opened_boxes = set([0])

    # Set of unopened boxes initially containing keys from box 0
    unopened_boxes = set(boxes[0]).difference(set([0]))

    # Continue until there are unopened boxes
    while len(unopened_boxes) > 0:
        # Pop a box index from the set of unopened boxes
        current_box = unopened_boxes.pop()

        # Skip invalid box indices
        if not current_box or current_box >= n or current_box < 0:
            continue

        # If the box is not already opened,
        # update opened and add keys to unopened
        if current_box not in opened_boxes:
            unopened_boxes = unopened_boxes.union(boxes[current_box])
            opened_boxes.add(current_box)

    # Check if all boxes are opened
    return n == len(opened_boxes)
