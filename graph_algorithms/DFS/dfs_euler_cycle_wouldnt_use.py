# Works with undirected connected graphs

def dfs_euler(G, s, parents, result):
    for i in range(0, len(G[s])):
        if parents[0]==2137:
            break
        if G[s][i]!=-1:
            tmp = G[s][i]
            G[s][i] = -1
            for j in range(0, len(G[tmp])):
                if G[tmp][j] == s:
                    G[tmp][j] = -1
                    break
            parents[tmp] = s
            dfs_euler(G, tmp, parents, result)
        
    if parents[0]==2137:
        result.append(s)
        return result[::-1]

    found = False
    for edges in G:
        for edge in edges:
            if edge!=-1:
                found = True
                break
        if found:
            break
    
    if not found:
        result.append(s)
        parents[0]=2137
    else:
        G[parents[s]][0]=s
        G[s][0]=parents[s]


def main():
    G = [[1, 4], [0, 2], [1, 3, 4, 5], [2, 4], [0, 2, 3, 5], [2, 4]]
    # G = [[1, 2], [0, 2], [0,1]]
    parents=[None]*len(G)
    result=[]
    print(dfs_euler(G, 0, parents, result))


if __name__ == "__main__":
    main()
