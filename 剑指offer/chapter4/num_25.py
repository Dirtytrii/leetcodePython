import ListNode


def reverseList(self, head: ListNode) -> ListNode:
    if not head.next: return head

    per, mid = None, head
    while mid != None:
        # 指向当前的下一个节点
        nextN = mid.next
        # 反转指针
        mid.next = per
        # 将指针依次后移
        per = mid
        mid = nextN

    return per


def addTwoReversed(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    sumNode = dummy
    # 进位
    carry = False

    while l1 is not None or l2 is not None:
        total = 0

        # 开始相加
        if l1 is not None:
            digit1 = l1.val
        else:
            digit1 = 0
        if l2 is not None:
            digit2 = l2.val
        else:
            digit2 = 0
        # 进位
        if carry is True:
            total = digit1 + digit2 + 1
            carry = False
        else:
            total = digit1 + digit2
        # 判断进位
        if total > 9:
            carry = True
            total -= 10

        newNode = ListNode(total)
        sumNode.next = newNode
        sumNode = newNode

        if l1 is not None: l1 = l1.next
        if l2 is not None: l2 = l2.next

    if carry:
        sumNode.next = ListNode(1)

    return dummy.next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    l1_h = self.reverseList(l1)
    l2_h = self.reverseList(l2)

    reversedHead = self.addTwoReversed(l1_h, l2_h)
    return reverseList(reversedHead)
