'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''
# Definition for singly-linked list.
# class ListNode(object):
#      def__init__(self, x):
#      self.val = x
#      self.next = None


class Solution(object):
    def mergeTwoLits(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 == None and l2 == None:
            return None

        elif l1 != None and l2 == None:
            return l1
        elif l2 != None and l1 == None:
            return l2
        else:
            dummy = ListNode(0)
            p = dummy


            while l1 != None and  l2 != None:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next

            if l1 != None:
                p.next = l1

            if l2 != None:
                p.next = L2

            return dummy.next
        
