class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListCycleII:
    def detect_cycle(self, head: ListNode) -> ListNode:
        '''
        使用特别的判断方法：Floyd 判圈法，将两个指针分别命名为快指针 fast 和慢指针 slow，将两个指针分别放在列表的开头， 规则为快指针每次
        移动两个单位的时候，慢指针移动一个单位。当 fast 和 slow 第一次相遇的时候，说明当前链表存在一个环。
        此时，再次将 fast 指针移动到链表的开头，同时将 fast 和 slow 都每次前进一步，当两个指针再次相遇的时候，此时为链表中环的起点
        '''
        # 下面使用Floyd方法
        # 将快慢指针分别放置于表头
        '''
        在这里需要留意一个问题，就是刚开始设置的时候，slow和fast就是放在一起的，所以在下面fast和slow 是否相等的判断中，会引起误判，在这里可
        以用到两个不同的解法，一个是先移动指针，再进行判断；一个是设置modified变量来辅助判断。但是后者更花时间，因此用前者更好。
        '''
        slow, fast = head, head
        # 开始循环移动两个快慢指针，按照上面的规则来进行，fast + 2, slow + 1 each
        while True:
            if fast.next is None:  # 如果 fast 移动到了尽头，那么说明整个链表不存在环
                return None
            elif fast.val == slow.val:  # 如果 两个指针第一次相遇，那么证明存在环，进行查找环头的操作
                break
            else:
                # 否则照常移动指针
                slow = slow.next
                fast = fast.next
                fast = fast.next

        # 能到这里来，说明一定存在环，因此进行查找环头的操作
        fast = head
        while True:
            if fast.val == slow.val:
                return fast
            slow = slow.next
            fast = fast.next
