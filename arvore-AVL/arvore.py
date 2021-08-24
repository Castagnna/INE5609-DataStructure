

class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None # aponta para o pai do No
        self.height = 1 # a altura do no na arvore


class AVLTree:
    
    def __init__(self):
        self.root = None

    def insert(self, value:int):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value:int, cur_node:Node):

        if value < cur_node.value:

            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node # set parent
                self._inspect_insertion(cur_node.left_child)
            else:
                self._insert(value, cur_node.left_child)
                
        elif value > cur_node.value:

            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node # set parent
                self._inspect_insertion(cur_node.right_child)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in tree!")

    def _get_height(self, cur_node:Node):
        
        if cur_node == None:
            return 0
        
        return cur_node.height

    def _rebalance_node(self, z:Node, y:Node, x:Node):
        if y == z.left_child and x == y.left_child:
            self._right_rotate(z)
        elif y == z.left_child and x == y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right_child and x == y.right_child:
            self._left_rotate(z)
        elif y == z.right_child and x == y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('_rebalance_node: z,y,x node configuration not recognized!')
            
    def _inspect_insertion(self, cur_node:Node, node_path = []):
        
        if cur_node.parent == None:
            return
        
        node_path = [cur_node] + node_path

        left_height = self._get_height(cur_node.parent.left_child)
        right_height = self._get_height(cur_node.parent.right_child)

        if abs(left_height - right_height) > 1:
            # altura da arvore esquerda menos direita tem que estar entre [-1, 1]
            # caso contrário é preciso rebalancear
            node_path = [cur_node.parent] + node_path
            self._rebalance_node(node_path[0], node_path[1], node_path[2])
            return

        new_height = 1 + cur_node.height 
        
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._inspect_insertion(cur_node.parent, node_path)
            
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node:Node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(f'{cur_node.value}, h = {cur_node.height}')
            self._print_tree(cur_node.right_child)

    def __repr__(self):
        
        if self.root == None:
            return ''
        
        content = '\n' # to hold final string
        cur_nodes = [self.root] # all nodes at current level
        cur_height = self.root.height # height of nodes at current level
        sep = ' ' * (2 ** (cur_height - 1)) # variable sized separator between elements
        
        while True:
            cur_height += -1 # decrement current height
            if len(cur_nodes)==0: break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n == None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None,None])
                    continue

                if n.value != None:       
                    buf = ' ' * int((5 - len(str(n.value))) / 2)
                    cur_row += f'{buf}{n.value}{buf}' + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left_child != None:  
                    next_nodes.append(n.left_child)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right_child != None: 
                    next_nodes.append(n.right_child)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2) # cut separator size in half

        return content


if __name__ == '__main__':
    new_tree = AVLTree()

    new_tree.insert(30)
    new_tree.print_tree()
    print(new_tree.__repr__())

    new_tree.insert(20)
    new_tree.print_tree()
    print(new_tree.__repr__())

    new_tree.insert(50)
    new_tree.print_tree()
    print(new_tree.__repr__())

    new_tree.insert(40)
    new_tree.print_tree()
    print(new_tree.__repr__())

    new_tree.insert(70)
    new_tree.print_tree()
    print(new_tree.__repr__())

    new_tree.insert(35)
    new_tree.print_tree()
    print(new_tree.__repr__())