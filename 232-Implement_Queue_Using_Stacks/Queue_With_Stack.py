'''Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. 
You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 
Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.'''

#CODE
class MyQueue:

    def __init__(self):
        self.push_stk=[]    # Stack for pushing new elements
        self.pop_stk=[]     # Stack for popping and peeking elements

    def push(self, x: int) -> None:
        # Push the value into the input stack
        self.push_stk.append(x)

    def pop(self) -> int:
        if not self.pop_stk:
            self.transfer_elements()
        return self.pop_stk.pop() 

    def peek(self) -> int:
        if not self.pop_stk:
            self.transfer_elements()
        return self.pop_stk[-1] 
        

    def empty(self) -> bool:
        # Return whether both the input stack and the output stack are empty
        return not self.push_stk and not self.pop_stk

    def transfer_elements(self) -> None:
        # Transfer elements from push_stk to pop_stk
        while self.push_stk:
            self.pop_stk.append(self.push_stk.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()