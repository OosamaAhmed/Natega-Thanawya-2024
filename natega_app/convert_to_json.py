import pandas as pd
df = pd.read_excel('data.xlsx', engine='openpyxl')
df_sorted = df.sort_values(by='الدرجة', ascending=False).reset_index(drop=True)

df_sorted['الترتيب'] = df_sorted.index + 1
total_score = 410
df_sorted['النسبة_المئوية'] = (df_sorted['الدرجة'] / total_score * 100).round(2)
df_sorted.rename(columns={
    'رقم الجلوس': 'رقم_الجلوس',
    'الاسم': 'الاسم',
    'الدرجة': 'الدرجة',
    'student_case': 'student_case',
    'student_case_desc': 'student_case_desc',
    'c_flage': 'c_flage'
}, inplace=True)
df_sorted = df_sorted[['الترتيب', 'رقم_الجلوس', 'الاسم', 'الدرجة', 'النسبة_المئوية', 'student_case', 'student_case_desc', 'c_flage']]
df_sorted.to_json('data.json', orient='records', force_ascii=False)
