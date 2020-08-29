#Name : Kartik Gupta
#PRN : 1032170673
#Subject : Artificial Intelligance
#Assignment 2
#Roll No. : PB-40

class Variable:
    def __init__(self,value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
class Constant:
    def __init__(self,value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
class Rel:
    def __init__(self,name,args):
        #This is a list
        self.name = name
        self.value = str(self.name)+str([i.value for i in args])
        self.args = args



def Unify(L1,L2,testset):
    '''
    L1 and L2 are Rel types, variables or constants
    '''
    #If both are variable or constants
    if(isinstance(L1,Variable) or isinstance(L2,Variable) or isinstance(L1,Constant) or isinstance(L2,Constant)):
        if L1 == L2:
            return None
        elif isinstance(L1,Variable):
            if isinstance(L2,Variable):
                print("Both missmatching variables")
                return False
            else:
                if L1.value not in testset.values():
                    return [L2,L1]
                else:
                    print("Ambigious Variable")
                    return False
        elif isinstance(L2,Variable):
            if isinstance(L1,Variable):
                print("Both missmatching variables")
                return False
            else:
                if L2.value not in testset.values():
                    return [L1,L2]
                else:
                    print("Ambigious Variable")
                    return False
        else:
            print("Missmatch")
            return False

    #Ensuring the functions are the same 
    elif L1.name != L2.name:
        print("Relation Missmatch")
        return False
    #Ensuring the functions have the same number of arguments
    elif len(L1.args) != len(L2.args):
        print("Arguements length missmatch")
        return False
    
    SUBSET = {}

    for i in range(len(L1.args)):
        S = Unify(L1.args[i],L2.args[i],SUBSET)
        if S==False:
            return False
        if S != None:
            SUBSET[S[0].value] = S[1].value

    return SUBSET


if __name__ == "__main__":

    print(Unify(Rel("Knows",[Constant("John"),Variable("X")]),Rel("Knows",[Variable("Y"),Rel("Mother",[Variable("Y")])]),{}))
    print()
    print(Unify(Rel("Knows",[Constant("John"),Variable("X")]),Rel("Knows",[Variable("Y"),Constant("Elizabeth")]),{}))
    print()
    print(Unify(Rel("Knows",[Constant("John"),Variable("X")]),Rel("Knows",[Variable("X"),Constant("Elizabeth")]),{}))    


#Output:
#{'John': 'Y', "Mother['Y']": 'X'}
#{'John': 'Y', 'Elizabeth': 'X'}
#Ambigious Variable
#False
