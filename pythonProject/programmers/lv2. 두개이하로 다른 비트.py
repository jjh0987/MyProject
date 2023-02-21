numbers = [1,2,7,100000]
bin(10**15)
def find(x):
    if x % 4 == 3:
        return x + 1
    else:
        return x + 1


number = [find(i) for i in range(10**15+1)]

[bin(i)[2:] for i in range(1,50,4)]