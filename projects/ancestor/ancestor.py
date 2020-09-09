
def earliest_ancestor(ancestors, starting_node):
    # graph of each child's parents
    cgr = {}

    for p, c in ancestors:
        if c in cgr:
            cgr[c].append(p)
        else:
            cgr[c] = [p]

    longest = []
    length = 1
    lines = [[starting_node]]
    while lines:
        curr = lines.pop(0)
        if len(curr) == length:
            longest.append(curr)
        elif len(curr) > length:
            longest = [curr]
            length = len(curr)
        c = curr[-1]
        if c in cgr:
            for i in cgr[c]:
                nxt = curr.copy()
                nxt.append(i)
                lines.append(nxt)
    if len(longest) == 1:
        if longest[0][-1] == starting_node:
            return -1
        else:
            return longest[0][-1]
    derp = [i[-1] for i in longest]
    return min(derp)



            

