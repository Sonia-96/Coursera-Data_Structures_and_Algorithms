# Use Python3

c = input()
n, capacity = map(int, c.split())
value_per_weight = []
dic = {}
# dic = {v/w: weight}
for i in range(n):
    c = input()
    v, w = map(int, c.split())
    value_per_weight.append(v / w)
    dic[v / w] = w
value_per_weight.sort(reverse=True)

def get_optimal_value(capacity, dic, value_per_weight):
    V = 0
    for i in range(n):
        if capacity == 0:
            return(V)
        a = min(capacity, dic[value_per_weight[i]])
        V = V + value_per_weight[i] * a
        capacity = capacity - a
    return V

opt_value = get_optimal_value(capacity, dic, value_per_weight)
print("{:.4f}".format(opt_value))
