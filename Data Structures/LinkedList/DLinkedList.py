class Node(object):
    def __init__(self, val):
        self.val = val;
        self.next = None;

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.size or index < 0: #corner case
            return -1
        if self.head == None: #no node
            return -1
        
        cur = self.head
        for i in range(index):
            cur = cur.next;
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        cur = Node(val)
        #if self.head == None: 
        cur.next = self.head
        self.head = cur #new head
        self.size +=1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        cur = Node(val)
        if self.head == None: #1 node in list
            self.head = cur
            self.tail = cur
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = cur
            cur.next = None
            self.tail = cur
        self.size +=1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        cur = Node(val)
        if index > self.size or index < 0: 
            return
        if index == 0: #add front:
            self.addAtHead(val)
        #elif index == index-1: #add back
        #    self.addAtTail(val):
        else:
            prev = self.head
            for i in range(index-1):
                prev = prev.next
            #prev points to pre indxth
            cur.next = prev.next
            prev.next = cur
        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index >= self.size or index < 0: 
            return
        cur = self.head
        if index == 0:
            self.head = cur.next #delete head
        else: #delete tail same as other cases
            temp = self.head
            for i in range(index-1):  
                cur = cur.next
            #cur stops at pre indexth
            cur.next = cur.next.next
        self.size -= 1
                
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)