

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
        
        # se o valor a ser inserido for menor que o valor do no atual,
        if value < cur_node.value:
            # e se estiver vazia a posição esquerda do no atual, inseri na esquerda
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node
                # apos inserir o novo no eh preciso verificar o balanceamento da arvore
                self._inspect_insertion(cur_node.left_child)

            # se nao, repete o processo com o elemento esquerdo do no atual
            else:
                self._insert(value, cur_node.left_child)

        # se o valor a ser inserido for maior que o valor do no atual, guarda na direita   
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node # set parent
                self._inspect_insertion(cur_node.right_child)
            else:
                self._insert(value, cur_node.right_child)

        # se o valor nao for nem menor nem maior, então é o igual ao valor do no atual
        else:
            print("Value already in tree!")

    def _inspect_insertion(self, cur_node:Node, node_path = []):
        
        if cur_node.parent == None:
            return
        
        node_path = [cur_node] + node_path

        left_height = self._get_height(cur_node.parent.left_child)
        right_height = self._get_height(cur_node.parent.right_child)

        # se o absoluto da diferenca entre a arvore a esquera e a direita do no atual for maior que 1
        # é preciso rebalancear
        if abs(left_height - right_height) > 1:
            node_path = [cur_node.parent] + node_path
            self._rebalance_node(
                node_z = node_path[0],
                node_y = node_path[1],
                node_x = node_path[2],
            )
            return

        # se não for preciso rebalancear, então vamos atualizar a altura do no pai
        new_parent_height = 1 + cur_node.height 

        if new_parent_height > cur_node.parent.height:
            cur_node.parent.height = new_parent_height

        # vamos continuar esse processo recursivamente até a raiz
        self._inspect_insertion(cur_node.parent, node_path)

    def _get_height(self, cur_node:Node):
        
        if cur_node == None:
            return 0
        
        return cur_node.height

    def _rebalance_node(self, node_z:Node, node_y:Node, node_x:Node):

        # LEFT LEFT CASE: se o filho esquerdo de Z e for Y e o filho esquerdo de Y for X,
        # então faz uma rotacao direita em z
        if node_z.left_child == node_y and node_y.left_child == node_x:
            self._right_rotate(node_z)

        # LEFT RIGHT CASE: se o filho esquerdo de Z e for Y e o filho direito de Y for X,
        # então faz uma rotacao esquerda em y e rotação direita em z
        elif node_z.left_child == node_y and node_y.right_child == node_x:
            self._left_rotate(node_y)
            self._right_rotate(node_z)

        # RIGHT RIGHT CASE: se o filho direito de Z e for Y e o filho direito de Y for X,
        # então faz uma rotacao esquera em z
        elif node_z.right_child == node_y and node_y.right_child == node_x:
            self._left_rotate(node_z)

        # RIGHT LEFT CASE: se o filho direito de Z e for Y e o filho esquerdo de Y for X,
        # então faz uma rotacao direita em y e rotação esquerda em z
        elif node_z.right_child == node_y and node_y.left_child == node_x:
            self._right_rotate(node_y)
            self._left_rotate(node_z)

        else:
            raise Exception('_rebalance_node: z, y, x node configuration not recognized!')

    def _right_rotate(self, node_z:Node):

        sub_root = node_z.parent 
        node_y = node_z.left_child
        node_t3 = node_y.right_child
        node_y.right_child = node_z
        node_z.parent = node_y
        node_z.left_child = node_t3

        if node_t3 != None:
            node_t3.parent = node_z

        node_y.parent = sub_root

        if node_y.parent == None:
                self.root = node_y
        else:
            if node_y.parent.left_child == node_z:
                node_y.parent.left_child = node_y
            else:
                node_y.parent.right_child = node_y	

        # a nova altura do nó será: 1 + a maior altura dentre os seus filhos
        node_z.height = 1 + max(self._get_height(node_z.left_child), self._get_height(node_z.right_child))
        node_y.height = 1 + max(self._get_height(node_y.left_child), self._get_height(node_y.right_child))

    def _left_rotate(self, node_z:Node):

        sub_root = node_z.parent 
        node_y = node_z.right_child
        node_t2 = node_y.left_child
        node_y.left_child = node_z
        node_z.parent = node_y
        node_z.right_child = node_t2

        if node_t2 != None:
            node_t2.parent = node_z

        node_y.parent=sub_root

        if node_y.parent == None: 
            self.root = node_y
        else:
            if node_y.parent.left_child == node_z:
                node_y.parent.left_child = node_y
            else:
                node_y.parent.right_child = node_y

        # a nova altura do nó será: 1 + a maior altura dentre os seus filhos
        node_z.height = 1 + max(self._get_height(node_z.left_child), self._get_height(node_z.right_child))
        node_y.height = 1 + max(self._get_height(node_y.left_child), self._get_height(node_y.right_child))
            
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
            if len(cur_nodes) == 0:
                break
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
            sep = ' ' * int(len(sep) / 2)

        return content


if __name__ == '__main__':
    new_tree = AVLTree()

    new_tree.insert(5)
    new_tree.print_tree()
    print(new_tree)

    new_tree.insert(2)
    new_tree.print_tree()
    print(new_tree)

    new_tree.insert(3)
    new_tree.print_tree()
    print(new_tree)
