import ListNode


def reverseList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    # 三个指针 一个指向当前的前一个 一个指向当前 一个指向当前之后一个
    pre = None
    mid = head

    while mid is not None:
        # 指向后一个
        nextNode = mid.next
        # 反转指针
        mid.next = pre

        # 将指针依次后移
        pre = mid
        mid = nextNode
    return pre
