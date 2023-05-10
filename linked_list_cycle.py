# Definition for singly linked list
# class ListNode(object)
#    def __init__(self, x):
#          self.val = x
#          self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        else:
            fast = head
            slow = head


            has_cycle = False

            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next

                if fast == slow:
                    has_cycle =  True
                    break


                if has_cycle == False:
                    return None


                slow = head

                while fast != slow:
                    fast = fast.next
                    slow = slow.next

                return slow
