survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

survey_form = {'RT':{'R':0,'T':0},
               'TR':{'R':0,'T':0},
               'FC':{'C':0,'F':0},
               'CF':{'C':0,'F':0},
               'MJ':{'J':0,'M':0},
               'JM':{'J':0,'M':0},
               'AN':{'A':0,'N':0},
               'NA':{'A':0,'N':0}}

for i in range(len(choices)):
    if choices[i] < 4:
        survey_form[survey[i]][survey[i][0]] += abs(choices[i]-4)
    elif choices[i] > 4:
        survey_form[survey[i]][survey[i][1]] += choices[i]-4

ans_dict = {'R':0,'T':0,
            'C':0,'F':0,
            'J':0,'M':0,
            'A':0,'N':0}
for sur in survey_form.values():
    for s in sur:
        ans_dict[s] += sur[s]

ans_dict
ans = ''
if ans_dict['R'] < ans_dict['T']:
    ans += 'T'
else:
    ans += 'R'
if ans_dict['C'] < ans_dict['F']:
    ans += 'F'
else:
    ans += 'C'
if ans_dict['J'] < ans_dict['M']:
    ans += 'M'
else:
    ans += 'J'
if ans_dict['A'] < ans_dict['N']:
    ans += 'N'
else:
    ans += 'A'