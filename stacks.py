# Easy
def is_valid_paranthesis(s: str) -> bool:
        openings = ["(", "{", "["]
        closings = [")", "}", "]"]
        stack = []
        char_map = dict(zip(closings, openings))

        for i in s:
            if i in openings:
                stack.append(i)
            elif i in closings:
                if not stack or stack.pop() != char_map[i]:
                    return False
        
        return len(stack) == 0

# Medium
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]