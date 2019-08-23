import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, HTML

def splitter(simbol='-', amount=100):
	print(amount*simbol)

def view(d, only_numeric=True, full_stats=False, histograms=True):

    print("\033[1mРазмер данных:\033[0m {}".format(d.shape))
    
    print("\n\033[1mОбзор первых строк данных\033[0m")
    splitter()
    display(HTML(d.head().to_html()))
    
    print("\n\033[1mТипы данных и кол-во непустых строк\033[0m")
    splitter()
    display(HTML(pd.DataFrame(d.info()).to_html()))
    
    print("\n\033[1mНаличие дат (месяц, год, день) или id в названиях столбцов\033[0m")
    splitter()
    
    data_types = pd.DataFrame()
    filter_columns = []
    for col in d.columns:
        if 'date' in col.lower() or 'time' in col.lower():
            filter_columns.append(col)
            temp = {'Имя':col, 
                        'Текущий тип':d[col].dtypes,
                        'Рекомендуемый тип':'datetime или int'}
            data_types = data_types.append(pd.DataFrame.from_dict(temp, orient='index').T)
        if 'year' in col.lower() or 'month' in col.lower() or 'day' in col.lower() or 'id' in col.lower() or 'uuid' in col.lower():
            filter_columns.append(col)
            temp = {'Имя':col, 
                        'Текущий тип':d[col].dtypes,
                        'Рекомендуемый тип':'int'}
            data_types = data_types.append(pd.DataFrame.from_dict(temp, orient='index').T)
    if data_types.shape[0] != 0:
        #print(filter_columns)
        display(HTML(data_types.set_index('Имя').to_html()))
    else:
        print("Столбцов с упоминанием даты или id нет!")
    
    print("\n\033[1mКол-во пропусков в данных\033[0m")
    splitter()
    numbers_of_nulls = pd.DataFrame(columns=['Имя'], data=d.columns)
    numbers_of_nulls['Пропуски'] = d.isnull().sum().values
    numbers_of_nulls['Пропуски, %'] = 100*d.isnull().sum().values/d.shape[0]
    display(HTML(numbers_of_nulls.set_index('Имя').to_html()))
    
    print("\n\033[1mКол-во дубликатов в данных\033[0m")
    splitter()
    print(d.duplicated().sum())
    
    # делим данные на числовые и категориальные
    # для числовых посчитаем среднее/медиану/квартили и IQR и кол-во выбросов методом интерквартильного размаха
    print("\n\033[1mОписательные статистики числовых признаков\033[0m")
    splitter()
    d_without_date_id = d.drop(filter_columns, axis=1)
    if d_without_date_id.select_dtypes(np.number).shape[1] != 0:
        dsc = d_without_date_id.describe(include=np.number).T
        dsc['IQR'] = dsc['75%'] - dsc['25%']
        dsc['min_out'] = dsc['25%'] - 1.5 * dsc['IQR']
        dsc['max_out'] = dsc['75%'] + 1.5 * dsc['IQR']
        outliers = []
        for col in dsc.index:
            outliers.append(d_without_date_id[(d_without_date_id[col] < dsc.loc[col, 'min_out']) | (d_without_date_id[col] > dsc.loc[col, 'max_out'])].shape[0])
        dsc['number_of_outliers'] = outliers
        dsc['count'] = dsc['count'].astype('int')
        if full_stats:
            display(HTML(dsc.to_html()))
        else:
            display(HTML(dsc.drop(['min_out', 'max_out', 'IQR'], axis=1).to_html()))
    else:
        print("В данных нет числовых признаков!")
    
    if histograms:
        print('\n\033[1mГистограммы числовых показателей\033[0m')
        splitter()
        d_without_date_id.select_dtypes(include=np.number).hist(figsize = (12, 12), bins = 20, color='#00ffea', alpha=0.75)
        plt.show()
    
    print("\n\033[1mОписательные статистики категориальных признаков\033[0m")
    splitter()
    if d.select_dtypes('object').shape[1] != 0:
        if not only_numeric:
            temp = pd.DataFrame()
            for col in d.select_dtypes('object').columns:
                # подсчет числа каждого уникального элемента и сортировка по убыванию
                # выбираем только топ-5
                t = d[col].value_counts()[:5]
                if t.shape[0] < 5:
                    # заполням -1 если элементов не хватает до 5
                    for _ in range(5 - t.shape[0]):
                        t = t.append(pd.Series([-1]))
                # формирум таблицу
                temp[col + '_name'] = t.index
                temp[col + '_count'] = t.values

            # вывод метода describe для категориальнх элементов
            dsc = d.describe(exclude=np.number).T
            display(HTML(dsc.to_html()))
            # вывод таблицы с топ-5 каждого категориального элемента
            print("\n\n\033[1mТоп-5 уникального категориального признака\033[0m")
            splitter()
            display(HTML(temp.to_html()))
    else:
        print("В данных нет категориальных признаков!")