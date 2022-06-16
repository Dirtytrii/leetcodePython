import ListNode


class Solution:
    def findLoop(self, head: ListNode) -> ListNode:
        fast, slow = head.next, head

        while fast is not None and slow is not None:
            if slow == fast:
                return slow

            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next

        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None

        nodeInList = self.findLoop(head)

        if nodeInList is None:
            return None

        countNode = 1
        temp = nodeInList

        # 统计环中节点数
        while temp != nodeInList:
            temp = temp.next
            countNode += 1

        fast, slow = head, head
        # 前指针先走n步
        for _ in range(0, countNode):
            fast = fast.next
        # 当两指针相遇时为环的入口节点
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow
