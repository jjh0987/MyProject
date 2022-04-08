import streamlit as st
from collections import Counter

import preprocessing
import execute


pre = preprocessing
tokens = pre.tokens
lines_token = pre.lines_token
promise140 = pre.promise140

candidates = ['기호 1번', '기호 2번', '기호 3번', '기호 4번', '기호 5번', '기호 6번', '기호 7번',
                  '기호 8번', '기호 9번', '기호 10번', '기호 11번', '기호 12번', '기호 13번', '기호 14번', '전체']


sp = execute.SearchPromise()
vk = execute.VisualizeKeywords()


st.sidebar.header('메뉴')
chapter = st.sidebar.selectbox('선택', ['시작', '후보자 공약 분석', '주제 분류', '클러스터링', '후보자/공약 추천'])


if chapter == '시작':
    st.title('제20대 대선 정책 공약 시각화')
    st.write('제20대 대선 후보자 14명의 정책 공약을 시각화하였습니다.')

    # 시작 >> 정보 등록 후 서비스 사용 가능
    user_age = st.selectbox('나이', range(1, 101))
    user_gender = st.radio(label='성별', options=['남성', '여성'])
    # user_from 

    if st.button('확인'):
        st.success('정상적으로 등록되었습니다. 감사합니다.')

# 시각화 - 후보자별 그래프, 클러스터링맵, 지역공약
elif chapter == '후보자 공약 분석':
    st.title('후보자 공약 분석')
    st.subheader('단어 분석')
    candidate = st.selectbox('후보자 선택', candidates)
    i = candidates.index(candidate)
    if candidate != '전체':
        counts = Counter(tokens[i])
        vk.show_graphs(counts, lines_token[i], i + 1)
    else:
        counts_for_all = Counter(sum(tokens, []))
        vk.show_graphs(counts_for_all)
    # 그래프 표시
    st.subheader('주제 단어 분석')
    vk.stacked_category()

    st.subheader('상관관계 분석')
    # 그래프 표시
    # 설명
    st.subheader('지역 공약 살펴보기')
    st.map()

# 주제 분류 - LSA, pyLDAvis
elif chapter == '주제 분류':
    st.title('주제 분류: 토픽 모델링')
    st.subheader('LSA')
    st.write('> LSA 설명')
    # 데이터프레임, 전체, 후보자별, 누적 그래프
    st.subheader('LDA')
    st.write('> LDA 설명')
    #pyLDAvis

# 클러스터링 
elif chapter == '클러스터링':
    st.title('클러스터링')

# 추천
elif chapter == '후보자/공약 추천':
    sub_chapter = st.sidebar.selectbox('방법', ['선택','머신러닝', '클러스터링', '유사도'])
    if sub_chapter == '선택':
        st.title('후보자/공약 추천')
        st.write('머신러닝,클러스터링,유사도를 이용해서 적합한 공약집을 추천해 드립니다!')
    elif sub_chapter == '머신러닝':
        st.title('머신러닝을 이용한 후보추천')
        target = st.text_input('')
        if target:
            for i in execute.ML().pred(target):
                st.write('추천된 공약집은', i, '입니다.')