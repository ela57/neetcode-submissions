class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0;
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        curr = self.head
        newnode = ListNode(val)
        newnode.next = curr.next
        self.head.next = newnode
        if not newnode.next:
            self.tail = newnode

    def insertTail(self, val: int) -> None:
        newnode = ListNode(val)
        self.tail.next = newnode
        self.tail = newnode

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while i < index and curr.next:
            i += 1
            curr = curr.next
        if curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        rtn = []
        curr = self.head.next
        while curr:
            rtn.append(curr.val)
            curr = curr.next
        return rtn
