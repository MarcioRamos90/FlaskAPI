class Node:
  def __init__(self, data=None, next_node=None):
      self.data = data
      self.next_node = next_node


class LinkedList:
  def __init__(self):
    self.head = None
    self.last_node = None

  def get_by_id(self, id: int):
    node = self.head
    while node:
      if node.data["id"] == int(id):
        return node.data
      node = node.next_node
    return None

  def to_list(self):
    list = []
    if self.head is None:
      return list
    
    node = self.head
    while node:
      list.append(node.data)
      node = node.next_node
    return list


  def print_ll(self):
    ll_string = ""
    node = self.head
    if node == None:
      print(None)
    while node:
      ll_string += f" {str(node.data)} ->"
      if node.next_node is None:
        ll_string += " None"
      node = node.next_node
    print(ll_string)

  def insert_begining(self, data):
    if self.head is None:
      self.head = Node(data, None)
      self.last_node = self.head
    else:
      new_node = Node(data, self.head)
      self.head = new_node

  def insert_at_end(self, data):
    if self.head is None:
      self.insert_begining(data)
      return
    self.last_node.next_node = Node(data, None)
    self.last_node = self.last_node.next_node

