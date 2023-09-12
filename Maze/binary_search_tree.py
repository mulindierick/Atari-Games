class Node:
    def __init__(self, name, score) -> None:
        self.score = score
        self.name = name
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
    
    def insert_node(self, node, score):
        new_node = Node(node, score)
        if not self.root:
            self.root = new_node
        else:
            curr_root = self.root

            while(True):
                if (node == curr_root.name):
                    return None
                if node < curr_root.name:
                    if not curr_root.left:
                        curr_root.left = new_node
                        return self
                    else:
                        curr_root = curr_root.left
                elif node > curr_root.name:
                    if not curr_root.right:
                        curr_root.right = new_node
                        return self
                    else:
                        curr_root = curr_root.right
    
    def search(self, name):
        if not self.root:
            return None
        curr_root = self.root
        found = False
        while curr_root and not found:
            if name < curr_root.name:
                curr_root = curr_root.left
            elif name > curr_root.name:
                curr_root = curr_root.right
            else:
                found = True
        if not found: return None
        return curr_root
    
def add_names_to_bst():
    bst = BST()
    with open('/Users/erickmulindi/Desktop/CS209/Maze/scores.txt', 'r') as scores:
            for score in scores.readlines():
                score = score.strip().split(",")
                print(score)
                bst.insert_node(score[0], score[1])
    scores.close()
    return bst

    
if __name__ == '__main__':
    bst = add_names_to_bst()
    print(bst.root.score)
    print(bst.search("erick m").score)

 


