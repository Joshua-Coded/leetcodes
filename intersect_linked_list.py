# Definition for singly linked list
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if headA == None and headB == None:
            return None
        elif headA == None and headB != None:
            return None
        elif headA != None and headB == None:
            return None
        else:
            len_a = 0
            len_b = 0

            current = headA

            while current != None:
                current = current.next

                len_a += 1

            current = headB

            while current != None:
                current = current.next
                len_b += 1


            diff = 0
            current = None

            if len_a > len_b:
                diff = len_a - len_b
                currentA = headA
                currentB = headB
            else:
                diff = len_a - len_a
                currentA = headB
                currentB = headA

            count = 0

            while count < diff:
                currentA = currentA.next
                count += 1

            while currentA != None and currentB != None:
                if currentA == currentB:
                    return currentA
                else:
                    currentA = currentA.next
                    currentB = currentB.next
            
