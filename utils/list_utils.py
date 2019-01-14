
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

def print_link_list(head):
    """
    打印链表，链表节点为ListNode
    :param head: 链表的头
    :return:
    """
    node = head
    s = ''
    while node is not None:
        s+=str(node.val)
        s+='->'
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
