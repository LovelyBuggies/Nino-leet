
def valid(string):
    
    a, d, res = [], {}, 0
    for idx, s in enumerate(string):
        if str(s) not in d:
            a = a + [s]
            res = max(res, len(a))
            d[str(s)] = idx
        else:
            tmp = a[:d[str(s)]+1]
            a = a[d[str(s)]+1:] + [s]
            # **generate O(n) probably?**
            for i in tmp: d.pop(str(i))
            res = max(res, len(a))
            d[str(s)] = idx

        print("buffer array: " + str(a)\
                + "  \nbuffer dict: " + str(d) + "\n")

    return res


string = [4,5,6,1,2,3,1,1,4,5,6]
print("\nmax len: " + str(valid(string)))