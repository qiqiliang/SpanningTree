#Sample Topology
# 1 --- 2 --- 3

topo = { 1: [2],
         2: [1, 3],
         3: [2] }
ttl_limit = 2
drops = []
