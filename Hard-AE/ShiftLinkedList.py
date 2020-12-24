def shiftLinkedList(head, k):
    """
    TC: O(n) | SC: O(1)
    """
    listLength = 1
    listTail = head

    while listTail.next is not None:
        listLength += 1
        listTail = listTail.next

    offsetShift = abs(k) % listLength

    if offsetShift == 0:
        return head

    newTailPosition = listLength - offsetShift if k > 0 else offsetShift
    newTail = head

    for _ in range(1, newTailPosition):
        newTail = newTail.next
    
    listTail.next = head
    newHead = newTail.next
    newTail.next = None

    return newHead
