elements = [7,9,1,1,4]

ans = set()
ans.add(sum(elements))
elements = elements*2
for level in range(1,int(len(elements)/2)):
    tp = sum(elements[:level])
    ans.add(tp)
    try:
        for j in range(1,len(elements)):
            tp -= elements[j-1]
            tp += elements[level+j-1]
            ans.add(tp)
    except:pass

ans