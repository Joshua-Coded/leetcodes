'''
Reversed a singly linked list.
'''
#Definition for singly-linked list.
#class ListNode(object):
#      def__init__(self, x):
#      self.val = x
#      self.next = None



class Solution(object):
    def reversedList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            """
            If head is empty, return empty list """
            return None
        elif head != None and head.next == None:
            
            # if head is not empty and head of the address of next node is empty. return the head value """
            return head
        else:
            temp = None
            next_node = None

            while head != None:
                next_node = head.next
                head.next = temp
                temp = head
                head = next_node

            return temp
