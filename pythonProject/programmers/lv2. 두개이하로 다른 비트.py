numbers = [3,7,11,15]


def find(x):
    if x % 4 == 3:
        tar = bin(x)[2:]
        if '0' in tar:
            tar = list(tar)
            tar.reverse()
            idx0 = tar.index('0')
            tar[idx0], tar[idx0-1] = tar[idx0-1], tar[idx0]
            tar.reverse()
            tar = ''.join(tar)
            return int(tar, 2)
        else:
            tar = '10' + '1' * (len(tar) - 1)
            return int(tar, 2)
    else:
        return x + 1


numbers = [find(i) for i in numbers]
find(1)
bin(11)