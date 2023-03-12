class Node:

    # Constructor of the Node, which assigns data and create undefined children
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Method to allow insert to the tree by existing root (self)
    def insert(self, data):
        # If value < than the value of the parent node
        if data < self.data:
            # If left child exists, we have to move towards the left
            if self.left:
                self.left.insert(data)
            # Else we have the position to insert
            else:
                self.left = Node(data)
                return
        # if value > than the value of the parent node
        else:
            # If right child exists, we have to move towards the right
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
                return


class InorderIterator:
    def __init__(self, root):
        self.traversal = []
        self.__move_left(root)

    def __move_left(self, current):
        while current != None:
            self.traversal.append(current)
            current = current.left

    def has_next(self):
        return len(self.traversal) > 0

    def next(self):
        if not self.has_next():
            raise Exception('No such element Exists')

        current = self.traversal.pop()

        if current.right != None:
            self.__move_left(current.right)

        return current


if __name__ == '__main__':
    root = Node(8)
    root.insert(9)
    root.insert(3)
    root.insert(2)
    root.insert(4)
    root.insert(5)

    itr = InorderIterator(root)
    try:
        print(itr.next().data)
        print(itr.next().data)
        print(itr.next().data)
        print(itr.next().data)
        print(itr.next().data)
        print(itr.next().data)
        print(itr.next().data)
        print(itr.has_next())
    except Exception as e:
        print("No such element Exists")
