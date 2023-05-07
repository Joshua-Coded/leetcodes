class Solution(object):
    def deleteNode(self, node):
        if node == None:
            pass
        else:
            next_node = node.next
            node.val = next_node.val
