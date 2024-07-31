import sys
input = sys.stdin.readline
data = input()
data = data.split()
tp = []
cnt = 0
i = 0
while 1:
    try:
        tp.append(data[i])
        if len(' '.join(tp)) > 80:
            tp.pop()
            i -= 1
            print(' '.join(tp))
            tp = []
            cnt = 0
        elif data[i] == '<br>':
            tp.pop()
            if tp:
                print(' '.join(tp) + ' ')
            else:
                print('')
            tp = []
            cnt = 0
        elif data[i] == '<hr>':
            tp.pop()
            if tp:
                print(' '.join(tp) + ' ')
            tp = []
            cnt = 0
            print('-'*80)
        i += 1
    except:break
if tp:
    print(' '.join(tp))

import sys
full_sentence = data
for sentence in sys.stdin:  # ctrl+D 입력까지 모든 줄을 입력 받는다
    full_sentence += sentence

result_sentence = full_sentence.split()  # 다중 공백 제거 및 단어 별 리스트화
hr = ""
temp_list = []
temp_line_text = ""
for word in result_sentence:  # 단어별 탐색
    if word == '<br>':  # <br> 태그면 지금까지 출력해야할 문장 출력 후 '줄바꿈'
        temp_line_text = ' '.join(temp_list)
        temp_list = []
        print(temp_line_text)
    elif word == '<hr>':  # 구분선 출력
        hr = ""
        if len(temp_list) != 0:  # 첫지점에서 구분선 출력이 아니라면, 지금까지 출력해야할 문장 출력 후 구분선 출력
            temp_line_text = ' '.join(temp_list)
            temp_list = []
            print(temp_line_text)
        for _ in range(0, 80):
            hr += '-'
        print(hr)
    else:
        temp_list.append(word)  # 단어들이면 계속 합쳐준다
        temp_line_text = ' '.join(temp_list)
        if len(temp_line_text) > 80:  # 합치다가 80줄이 넘으면
            temp_list.pop(-1)  # 넘는 단어 빼고
            temp_line_text = ' '.join(temp_list)  # 다시 합쳐서 출력
            print(temp_line_text)
            temp_list = []
            temp_list.append(word)  # 다음 줄은 넘는 단어부터 시작
temp_line_text = ' '.join(temp_list)  # 마지막 줄 출력
print(temp_line_text)
