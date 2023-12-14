import pandas as pd 

download_catalog = [
    {'postfix': '-01.xlsx',
     'category_of_workers': 'Педагогические работники дошкольных образовательных учреждений',
     'group': 'Педагоги',
      'date': '04.12.23'},
    {'postfix': '-02.xlsx',
     'category_of_workers': 'Педагогические работники образовательных учреждений общего образования',
     'group': 'Педагоги',
      'date' : '05.12.22'} ]

column_name = {
    1: 'date',
    2: 'district',
    3: 'group',
    4: 'category_of_worker',
    5: 'salary',
    6: 'attitude_salary',
    7: 'average_salary_for_individual_entrepreneus'
}

data = pd.read_excel('03-23-01.xlsx', skiprows=6, usecols='A:B,j')
data.insert(1, 'date', '07.01.2023' ,  False)
data.columns = range(data.columns.size)
data = data.rename(columns=column_name)
df_columns = pd.Series(column_name.items(), name='column_name')
data = data.join(df_columns)

data