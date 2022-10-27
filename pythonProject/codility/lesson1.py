N = int(input())
tar = [len(i) for i in bin(N)[2:].split('1')]

if tar[-1] != 0:
    tar.pop()

if not tar:
    print(0)
else:
    print(max(tar))

bin(328)