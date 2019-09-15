"""Queue class using 2 stacks."""


class Queue2Stacks:
    """Create a Queue using 2 stacks."""

    def __init__(self):
        """Initialize 2 stacks."""
        self.in_stack = list()
        self.out_stack = list()

    def enqueue(self, elem):
        """Add element to in_stack."""
        self.in_stack.append(elem)

    def dequeue(self):
        """Get FIFO reversing order from in_stack."""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
