import sys
input = sys.stdin.readline

import re
html = input().rstrip('\n')
div_blocks = re.findall(r'<div[^>]*>(.*?)</div>', html)
p = [0,0]
for i, block in enumerate(div_blocks, 1):
    p_count = len(re.findall(r'<p\b[^>]*>', block))
    p.append(p_count)
p = [p[i]+p[i-1] for i in range(1,len(p))]

titles = re.findall(r'<div[^>]*\btitle="([^"]*)"', html)
titles = [i.replace('  ',' ').strip() for i in titles]

p_contents_raw = re.findall(r'<p[^>]*>(.*?)</p>', html)
p_texts = [re.sub(r'<[^>]+>', '', text).strip() for text in p_contents_raw]
p_texts = [' '.join(i.strip().split()) for i in p_texts]

for i in range(len(titles)):
    print(f'title : {titles[i]}')
    for j in range(p[i],p[i+1]):
        print(p_texts[j])

# html = '<main><div title="title_name_1"><p><po></po>paragraph 1</p><p>paragraph 2 <diving>Italic Tag</diving> <br > </p><p>paragraph 3 <b>Bold Tag</b> end.</p></div><div title="title_name_2"><p>paragraph 4</p><p>paragraph 5 <i>Italic Tag 2</i> <br > end.</p></div></main>'

import sys
input = sys.stdin.readline
html = input().rstrip('\n')

i = 0
dash = False
while i < len(html):
    if html[i] == '<':
        tp = ''
        while html[i] != '>':
            if html[i] == '/':
                dash = True
            tp += html[i]
            i += 1
        tp += html[i]
        i += 1

        if dash:
            dash = False
            continue

        if tp == '<main>':
            continue
        elif '="' in tp:
            print('title : '+tp.split('"')[1].replace('  ',' ').strip())
        elif tp == '<p>':
            tp = ''
            sub = ''
            while 1:
                try:
                    if html[i] == '<':
                        while html[i] != '>':
                            sub += html[i]
                            i += 1
                        sub += html[i]
                        i += 1
                    else:
                        tp += html[i]
                        i += 1

                    if sub == '</p>':
                        break
                    else:
                        sub = ''

                except:
                    tp += html[i]
                    i += 1
            print(' '.join(tp.strip().split()))

        else:
            i += 1
    else:
        i += 1


import sys
input = sys.stdin.readline
html = input().rstrip('\n')

i = 0
while i < len(html):
    if html[i] == '<':
        tp = ''
        while html[i] != '>':
            tp += html[i]
            i += 1
        tp += html[i]
        i += 1

        if tp.startswith('</'):
            continue

        if tp == '<main>':
            continue

        elif tp.startswith('<div') and 'title="' in tp:
            print('title : ' + tp.split('title="')[1].split('"')[0])

        elif tp.startswith('<p'):
            paragraph = ''
            tag = ''
            in_tag = False

            while True:
                if html[i] == '<':
                    in_tag = True
                    tag = ''
                if in_tag:
                    tag += html[i]
                    if html[i] == '>':
                        in_tag = False
                        if tag == '</p>':
                            i += 1
                            break
                    i += 1
                else:
                    paragraph += html[i]
                    i += 1

            print(' '.join(paragraph.strip().split()))

    else:
        i += 1
