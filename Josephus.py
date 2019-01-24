#  File: Josephus.py

#  Description: 
# This program uses a Circular List Object to simulate the Josephus problem and it is stated as follows. 
# There is a group of soldiers surrounded by an overwhelming enemy force. There is no hope for victory without reinforcements, 
# so they make a pact to commit suicide.

#  Student Name: David Bradham

#  Course Name: CS 313E

class Link(object):
  def __init__(self, data, next = None):
    self.data = data
    self.next = next
  def __str__(self):
    return str(self.data)

class CircularList(object):
  # Constructor
  def __init__ ( self ): 
    self.first = None
    self.last = None
  # Insert an element (value) in the list
  def insert ( self, item ):
    new_link = Link(item)
    current = self.first
# assign new_link as self.first if CircularList is empty
    if current == None:
      self.first = new_link
      return
# assign new_link as self.last and self.first.next as new_link if there is only one Link in the CircularList
    if current.next == None:
      new_link.next = current
      current.next = new_link
      self.last = new_link
      return
# find the link which points to the first link and make it point to new_link, then make new_link point to self.first
    while current.next != self.first:
      current = current.next
    current.next = new_link
    new_link.next = self.first
    self.last = new_link
    return
  # Find the link with the given key (value)
  def find ( self, key ):
    current = self.first
    if current == None:
      return None
    while current.data != key and current.next != None:
      current = current.next
    if current.data == key:
      return current
    return
  # Delete a link with a given key (value)
  def delete ( self, key ):
    previous = self.first
    current = self.first
    if current == None:
      return None
# find the Link with a given key
    while current.data != key and self.find(key) != None:
      previous = current
      current = current.next
    if current == self.last:
      previous.next = current.next
      self.last = previous
# if only two Links in CircularList, delete the link with a given key and make the pointer of the other link equal to None      
    if current.next == previous and previous.next == current:
      previous.next = None
      return current
    if current == self.first and current.data == key:
      if current.next.next == current:
        self.first = current.next
        self.first.next = None
        return current
      self.first = self.first.next
      self.last.next = self.first
    if current.data == key:
      previous.next = current.next
      return current
  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
    current = self.find(start)
    if current != None:
      for i in range(n - 1):
        current = current.next
      next_link = current.next
      dead_link = current
      self.delete(current.data)
      return next_link
    
  # Return a string representation of a Circular List
  def __str__ ( self ):
    s = ''
    if self.first == None:
      return s
    if self.first.next == None:
      return str(self.first.data)
    current = self.first
    values = []
    while current.data != '':
      s = s + str(current) + ' '
      current = current.next
      if current == self.first:
        break
    return s
def main():
  josephus = CircularList()
  in_file = open('josephus.txt', 'r')
  num_soldiers = int(in_file.readline().strip())
  start = int(in_file.readline().strip())
  step_size = int(in_file.readline().strip())
  in_file.close()
# populate CircularList
  for i in range(1, num_soldiers + 1):
    josephus.insert(i)
# begin the circle of death
  current = josephus.find(start)
  for i in range(num_soldiers):
    if i == 0:
      for j in range(step_size - 2):
        current = current.next
    else:
      for j in range(step_size - 1):
        if current != None:
          current = current.next
    if current != None:
      print(josephus.delete(current.next.data))
  print(josephus)
main()
