#Get all reachable nodes
def get_reachable_nodes(input, node, d, inputUsed, foundNodes, preInputEpsilons):
    #Check if we already used up our input letter/number only epsilon transitions matter after that point
    if inputUsed and (node, 'e') in d:
        for subNode in d[(node, 'e')]:
            if not subNode in foundNodes:
                foundNodes.append(subNode)
                get_reachable_nodes(input, subNode, d, True, foundNodes, preInputEpsilons)
    #If we haven't used up our input letter examine both epsilon transitions and input paths
    elif not inputUsed:
        if (node, input) in d:
            for subNode in d[(node, input)]:
                foundNodes.append(subNode)
                get_reachable_nodes(input, subNode, d, True, foundNodes, preInputEpsilons)
        if (node, 'e') in d:
            for subNode in d[(node,'e')]:
                #Use pre input epsilons to break out of infinite epsilon recursion
                if subNode not in preInputEpsilons:
                    preInputEpsilons.append(subNode)
                    get_reachable_nodes(input, subNode, d, False, foundNodes, preInputEpsilons)

#Define the delta function
d={}
d[('0','e')] = ['1','4']

d[('1','0')] = ['1']
d[('1','1')] = ['2']

d[('2','0')] = ['3']
d[('2','1')] = ['1']
d[('2','e')] = ['0']

d[('3','0')] = ['2']
d[('3','1')] = ['3']

d[('4','0')] = ['4']
d[('4','1')] = ['5']

d[('5','0')] = ['6']
d[('5','1')] = ['7']

d[('6','0')] = ['8']
d[('6','1')] = ['4']
d[('6','e')] = ['0']

d[('7','0')] = ['5']
d[('7','1')] = ['6']

d[('8','0')] = ['7']
d[('8','1')] = ['8']

#
nodes = ['0','1','2','3','4','5','6','7','8']
inputs = ['0','1']
for node in nodes:
    reachableNodes = []
    print("Node number: " + node)
    for input in inputs:
        print("Input: " + input)
        #Find all reachable nodes
        get_reachable_nodes(input, node, d, False, reachableNodes, [])
        reachableNodes = map(lambda x: int(x), reachableNodes)
        reachableNodes = set(reachableNodes)

        #Build the binary represenation of the output
        binary_rep = ""
        i = len(nodes)-1
        while i>=0:
            if i in reachableNodes:
                binary_rep += '1'
            else:
                binary_rep += '0'
            i -= 1

        print(binary_rep)
        reachableNodes = []








