class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remover_duplicata(head):
    current = head
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return head

def print_list(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    print(" → ".join(map(str, values)) + " → None")

def criar_lista(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


values = [0, 1, 1, 5, 7, 10, 10]
head = criar_lista(values)

print("Lista:")
print_list(head)


head = remover_duplicata(head)

print("Lista sem duplicata:")
print_list(head)


