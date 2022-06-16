import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)

        self.mergeList(l1, l2)

    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        mid = head

        while mid:
            nextNode = mid.next
            mid.next = pre
            pre = mid
            mid = nextNode

        return pre

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l2 and l1:
            # 记录后两个节点
            l1_temp = l1.next
            l2_temp = l2.next

            # 重组并后移指针
            l1.next = l2
            l1 = l1_temp

            l2.next = l1_temp
            l2 = l2_temp
