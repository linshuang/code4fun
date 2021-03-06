def lequal(l1, l2):
    """
    python内建list的相等
    :param l1:
    :param l2:
    :return:
    """
    if len(l1) != len(l2):
        return False

    for i in range(len(l1)):
        i = l1[i]
        idx = l2.index(i)
        if idx == -1:
            return False
        l2.remove(i)
    return True


class ListNode(object):
    """
    链表的节点
    """

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = 'val: ' + str(self.val) + ', linked-list: '
        sett = set()  # 防止环
        p = self
        while p is not None:
            if p in sett:
                break
            else:
                sett.add(p)
            s += (str(p.val) + '->')
            p = p.next
        return s[0:-2] if len(s) > 0 else s


def print_link_list(head):
    """
    打印链表，链表节点为ListNode
    :param head: 链表的头
    :return:
    """
    node = head
    s = ''
    while node is not None:
        s += str(node.val)
        s += '->'
        node = node.next
    print(s)


def create_link_list(l):
    """
    由python内建的list创建链表，链表节点为ListNode
    :param l: list
    :return:
    """
    head = ListNode(l[0])
    cur_node = head
    for i in range(1, len(l)):
        next_node = ListNode(l[i])
        cur_node.next = next_node
        cur_node = next_node

    return head
