def aSiap(start_node, goal_node):
    open_set = set(start_node) # berisi node terbuka artinya node yang masih dipakai
    closed_set = set() # berisi node tertutup, artinya udah dilewati
    g = {} # menyimpan jarak tempuh dari node start
    parents = {} # menyimpan posisi parent yang sedang digunakan

    # jarak awal dari node start dimulai dari nol
    g[start_node] = 0
    # node start pasti menjadi root, karena tak punya parent
    # maka node start menjadi parent node sebagai awalan
    parents[start_node] = start_node

    # program berjalan selama open_set memiliki isi / mencapai node goal
    while len(open_set) > 0:
        n = None # set n ke None

        # mencari node dengan f(node) terkecil
        for v in open_set:
            # membandingan f(node) child yang ada (belum di-close)
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n=v #menyimpan node dengan f(node) terkecil ke n
                print('Choosen:', v, '; f({}):'.format(v), g[v], '+', heuristic(v), '=', g[v] + heuristic(v), '\n')

        # jika n merupakan node goal atau node tersebut buntu, maka pass
        if n == goal_node or Graph_nodes[n] == None:
            pass
        else:
            for(m, jarak) in get_child(n):
                # n merupakan parent sekarang
                # jika m berupa node yg belum ada di open_set / closed_set,
                # m dimasukkan ke open_set dan menyimpan jarak yang ditempuh
                if m not in open_set and m not in closed_set:
                    open_set.add(m) # memasukkan m ke node terbuka
                    parents[m] = n # maka parent dari m adalah n
                    print('parent:', parents[m])
                    g[m] = g[n] + jarak # menyimpan jarak
                    print('Visited:', m, '; Jarak sekarang:', g[m])

                # membandingkan jarak node m dari g(start) hingga g(n)
                else:
                    if g[m] > g[n] + jarak:
                        # update g[m]
                        g[m] = g[n] + jarak
                        # mengganti parent dari m dengan node n
                        parents[m] = n

                        # jika node m ada di closed_set,
                        # maka hapus dan tambahkan ke open_set
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        # jika n merupakan node kosong
        if n == None:
            print('Jalan tidak ada!')
            return None

        # jika node sekarang adalah goal_node
        # maka mulai menyusun jalan dari start ke goal
        if n == goal_node:
            solusi = []

            print("menyusun path:")
            # melakukan traceback untuk menyusun path
            while parents[n] != n:
                solusi.append(n)
                print(solusi)
                n = parents[n]
            solusi.append(start_node)
            solusi.reverse()

            print('Solusi ditemukan: {}'.format(solusi))
            return solusi


        # menghapus n dari open_set dan memasukkan ke closed_set
        # karena semua child dari n telah diperiksa
        open_set.remove(n)
        closed_set.add(n)
        print('calon path:',closed_set)


    print('Solusi tidak ada!')
    return None

# fungsi untuk me-return child dan jaraknya dari posisi parent yang sekarang
def get_child(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        'S': 11,
        'A': 10.4,
        'B': 6.7,
        'C': 4,
        'D': 8.9,
        'E': 6.9,
        'F': 3,
        'G': 0
    }
    return H_dist[n]

# Graph dari setiap node dan jarak
Graph_nodes = {
    'S': [('A', 3), ('D', 4)],
    'A': [('B', 4), ('D', 5)],
    'B': [('C', 4), ('E', 5)],
    'C': None,
    'D': [('A',5),('E', 2)],
    'E': [('B',5),('F', 4)],
    'F': [('G', 3)]
}

if __name__ == "__main__": aSiap('S', 'G')
