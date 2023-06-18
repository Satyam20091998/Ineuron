class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2:
        sum_val = carry
        
        if l1:
            sum_val += l1.val
            l1 = l1.next
        
        if l2:
            sum_val += l2.val
            l2 = l2.next
        
        carry = sum_val // 10
        current.next = ListNode(sum_val % 10)
        current = current.next
    
    if carry > 0:
        current.next = ListNode(carry)
    
    return dummy.next

# Example 1
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 7 0 8

print()

# Example 2
l1 = ListNode(0)
l2 = ListNode(0)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 0

print()

# Example 3
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 8 9 9 9 0 0 0 1
