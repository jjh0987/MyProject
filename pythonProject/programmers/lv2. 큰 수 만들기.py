number = '1924'
k = 2

number = "1231234"
k = 3

number = "4177252841"
k = 4

number = [int(i) for i in number]
target = number[:number.index(max(number))]
while 1:
    if len(target) > k:
        target = target[:target.index(max(target))]
    else:
        break

number = number[len(target):]
k -= len(target)

target = number[:number.index(min(number))]
while 1:
    if len(target) > k:
        target = target[:target.index(min(target))]
    else:
        break


target

ans = ''
for i in number:
    if i != 0:
        ans += str(i)