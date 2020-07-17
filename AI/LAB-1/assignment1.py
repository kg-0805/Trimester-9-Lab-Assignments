#Name : Kartik Gupta
#PRN : 1032170673
#Subject : Artificial Intelligance
#Assignment 1
#Roll No. : PB-40

class Node:
    def __init__(self, matrix, level, f_value, parent=None, move='Start'):
        self.matrix = matrix
        self.level = level
        self.f_value = f_value
        self.parent = parent
        self.move = move

    def print_node_info(self):
        '''prints the node info'''
        print('\nNode Level = {}, Node H Value = {}, Node F Value = {}\nNode matrix : \n'.format(self.level,self.f_value-self.level, self.f_value))
        for i in self.matrix:
            for j in i:
                print(j, '\t', end="")
            print('\n')
        print('\n')

    def generate_child_nodes(self):
        '''we are going to move blank i.e. _ to possible directios out of left, right, up and down'''
        '''first we need to find location of blank'''
        x_blank, y_blank = self.find_blank()
        '''now we have to find possible values values that our blank can move'''
        possible_positions = []
        if x_blank-1 != -1:
            possible_positions.append(([x_blank-1, y_blank], 'up'))
        if x_blank+1 != len(self.matrix):
            possible_positions.append(([x_blank+1, y_blank], 'down'))
        if y_blank-1 != -1:
            possible_positions.append(([x_blank, y_blank-1], 'left'))
        if y_blank+1 != len(self.matrix):
            possible_positions.append(([x_blank, y_blank+1], 'right'))
        '''now we are going to generate the child nodes that by swapping blank with
        all possible values and append them to list and then return that list'''
        children_nodes = []
        for new_position, move in possible_positions:
            '''
            temp_matrix = self.matrix
            above line doesn't work because changes in temp_matrix changes the self.matrix
            '''
            temp_matrix = self.create_duplicate_matrix(self.matrix)
            temp_matrix[x_blank][y_blank], temp_matrix[new_position[0]][new_position[1]] = temp_matrix[new_position[0]][new_position[1]], temp_matrix[x_blank][y_blank]
            children_nodes.append(Node(temp_matrix, self.level+1, 0, self, move))
        return children_nodes

    def find_blank(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == '_':
                    return i, j
    def create_duplicate_matrix(self, matrix):
        temp = []
        for i in matrix:
            temp_row = []
            for j in i:
                temp_row.append(j)
            temp.append(temp_row)
        return temp
    
class Puzzle:
    def __init__(self, size):
        self.size = size
        self.open = []
        self.closed = []
        self.solution = []

    def function(self):
        print('Enter the start matrix \n(whitespace seperated n numbers on n lines) \n( _ for blank)')
        start_matrix = self.accept_matrix()
        print('Enter goal matrix in above format')
        goal_matrix = self.accept_matrix()
        '''Now we have to convert start matrix into node that can generate children'''
        start_node = Node(start_matrix, 0, 0)
        '''finding the f value of start node and then appending it to open list'''
        start_node.f_value = self.find_f_value(start_node, goal_matrix)
        self.open.append(start_node)
        while len(self.open) != 0:
            current_node = self.open[0]
            '''stop condition (when current matrix becomes equal to goal matrix)'''
            if self.find_h_value(current_node.matrix, goal_matrix) == 0:
                while current_node.parent != None:
                    self.solution.append(current_node)
                    current_node = current_node.parent
                self.solution.append(current_node)
                break
            '''creating childs by moving the blank i.e. _ in all possible directions,
            finding their heuristic (f) values and appending them to open list'''
            for i in current_node.generate_child_nodes():
                '''many nodes can be duplicated when heuristic function is difference between matrices
                to avoid that, we are checking if the matrix is already in open or closed nodes, its childre aren't generated again'''
                if self.is_not_duplicate(i.matrix):
                    i.f_value = self.find_f_value(i, goal_matrix)
                    self.open.append(i)
            '''add current node to closed list and delete it from open list'''
            self.closed.append(current_node)
            del self.open[0]
            '''we have to sort open list according to f values of nodes so that
            we in next loop, we will check node with list '''
            self.open.sort(key = lambda node:node.f_value)
        for i in reversed(self.solution):
            i.print_node_info()
        print('\nGoal was reached after checking {} state spaces'.format(1+len(self.closed)))
        print('Solution moves are : ')
        for i in reversed(self.solution):
            print('\t', i.move)

    def accept_matrix(self):
        '''accepts square of given size'''
        temp = []
        for i in range(self.size):
            temp.append(input().split(" "))
        return temp

    def find_f_value(self, start_node, goal_matrix):
        '''finds heuristic value of a node'''
        return start_node.level + self.find_h_value(start_node.matrix, goal_matrix)

    def find_h_value(self, start_matrix, goal_matrix):
        '''finds the difference between given puzzles'''
        diff = 0
        for i in range(self.size):
            for j in range(self.size):
                if start_matrix[i][j] != goal_matrix[i][j] and start_matrix[i][j] != '_':
                    diff = diff+1
        return diff

    def is_not_duplicate(self, matrix):
        '''check if matrix exists in open or closed list'''
        for i in self.open:
            if i.matrix == matrix:
                return False
        for i in self.closed:
            if i.matrix == matrix:
                return False
        return True
    
def main():
    n = int(input('Enter the size of matrix (square root of puzzle size + 1) : '))
    puzzle = Puzzle(n)
    puzzle.function()

main()

#Sample Input / Output

#Enter the size of matrix (square root of puzzle size + 1) : 3
#Enter the start matrix 
#(whitespace seperated n numbers on n lines) 
#( _ for blank)
#1 2 3
#_ 4 6
#7 5 8
#Enter goal matrix in above format
#1 2 3
#4 5 6
#7 8 _
#
#Node Level = 0, Node H Value = 3, Node F Value = 3
#Node matrix : 
#
#1 	2 	3 	
#
#_ 	4 	6 	
#
#7 	5 	8 	
#
#
#
#
#Node Level = 1, Node H Value = 2, Node F Value = 3
#Node matrix : 
#
#1 	2 	3 	
#
#4 	_ 	6 	
#
#7 	5 	8 	
#
#
#
#
#Node Level = 2, Node H Value = 1, Node F Value = 3
#Node matrix : 
#
#1 	2 	3 	
#
#4 	5 	6 	
#
#7 	_ 	8 	
#
#
#
#
#Node Level = 3, Node H Value = 0, Node F Value = 3
#Node matrix : 
#
#1 	2 	3 	
#
#4 	5 	6 	
#
#7 	8 	_ 	
#
#
#
#
#Goal was reached after checking 4 state spaces
#Solution moves are : 
#	 Start
#	 right
#	 down
#	 right
