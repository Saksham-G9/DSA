class TreeNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.children: list["TreeNode"] = []

    def print_tree(self):
        # Print Data
        print(self.data, end=": ")
        
        # Print Children
        for child in self.children:
            print(child.data, end=" ")
        
        
        print()
        # Child Recursive Call
        for child in self.children:
            if child.children:
                child.print_tree()


if __name__ == "__main__":
    root = TreeNode(1)

    child2 = TreeNode(2)
    child3 = TreeNode(3)
    child4 = TreeNode(4)
    child5 = TreeNode(5)
    child6 = TreeNode(6)
    child7 = TreeNode(7)
    child8 = TreeNode(8)
    child9 = TreeNode(9)

    root.children.append(child2)
    root.children.append(child3)
    root.children.append(child4)
    root.children.append(child5)
    root.children.append(child6)

    child4.children.append(child7)
    child7.children.append(child8)
    child6.children.append(child9)

    root.print_tree()
