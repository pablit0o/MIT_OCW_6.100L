# Problem Set 4A
# Name: Pablo Silva
# Collaborators:  my vest, pocket watch, tie, undershirt, belt, pants, and socks

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10)) 
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    if tree is None:
        return -1 # Account for +1
    
    maximum_height = 1 + max(find_tree_height(tree.get_left_child()), find_tree_height(tree.get_right_child()))
    return maximum_height


def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # leaf edge/base case
    if tree is None:
        return True
    
    T, l, r = tree.get_value(), tree.get_left_child(), tree.get_right_child()

    if l:
        # recur + must be heap
        if not is_heap(l, compare_func) or not compare_func(l.get_value(), T):
            return False
    if r: # process independently
        if not is_heap(r, compare_func) or not compare_func(r.get_value(), T):
            return False
    
    return True
    
    
    
    


if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    # print(find_tree_height(tree1))
    # tree1 = Node(5,Node(15,None,Node(16,Node(30),Node(17))),Node(6,Node(20,None,Node(45)),Node(11)))
    # print(is_heap(tree1, lambda x, y: x < y))
    # pad = [-1, 2, 3, 4, -12, 3]
    # new_pad = [-x for x in pad]
    # print(new_pad)
    pass
