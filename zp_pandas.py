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
    0: 'district',
    4: 'group',
    6: 'category_of_worker',
    2: 'salary',
    5: 'attitude_salary',
    3: 'average_salary_for_individual_entrepreneus'
}


data = pd.read_excel('03-23-01.xlsx', skiprows=6, usecols='A:B,j')
data.insert(1, 'date', '07.01.2023' ,  False)
data.columns = range(data.columns.size)
data = data.rename(columns=column_name)
data = data.rename(columns={0:'district', 2:'salary'} )
#(100 * data[['salary']] / data.average_salary_for_individual_entrepreneus)
data['salary']=data['salary'].convert_dtypes(convert_integer=True)
data['average_salary_for_individual_entrepreneus']=data['average_salary_for_individual_entrepreneus'].convert_dtypes(convert_integer=True)
print(data['average_salary_for_individual_entrepreneus'])
data.assign(attitude_salary = data.salary * 100 / data.average_salary_for_individual_entrepreneus)