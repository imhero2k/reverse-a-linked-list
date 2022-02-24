def reverse(llist):
    l=[]
    while llist!=None:
        l.append(llist.data)
        llist=llist.next
    l.reverse()
    head=SinglyLinkedListNode(l[0])
    t=head
    for i in range(1,len(l)):
        t.next=SinglyLinkedListNode(l[i])
        t=t.next
    return head
