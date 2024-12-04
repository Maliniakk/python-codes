class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def dodaj_na_koniec(head, data):
   node=Node(data)
   if head is None:
       head = node
       return head

   else:
       current = head
       while current.next is not None:
           current=current.next
       current.next = node

   return head

def wyswietlanie(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next
    print(None)

head = None
head = dodaj_na_koniec(head,1)
head = dodaj_na_koniec(head,2)
head = dodaj_na_koniec(head,3)
head = dodaj_na_koniec(head,4)
head = dodaj_na_koniec(head,5)

wyswietlanie(head)
