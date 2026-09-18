# 파이썬 버전 3.11.16 / 아나콘다 가상환경 설정 후 실행 할 것 / gemini 확인

import numpy as np
import pandas as pd 
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler


label_data = pd.read_csv('../dataset/labeled_data.csv')
label_data['EQUIP_NAME'].value_counts()
label_data['PART_NAME'].value_counts()

def make_input(data, machine_name, product_name):
    machine_ = data['EQUIP_NAME'] == machine_name
    product_ = data['PART_NAME'] == product_name
    data = data[machine_ & product_]

    data.drop(['_id', 'TimeStamp', 'PART_FACT_PLAN_DATE', 'Reason',
               'PART_FACT_SERIAL', 'PART_NAME','EQUIP_CD','EQUIP_NAME',
               'Mold_Temperature_1', 'Mold_Temperature_2', 'Mold_Temperature_5',
               'Mold_Temperature_6', 'Mold_Temperature_7', 'Mold_Temperature_8',
               'Mold_Temperature_9', 'Mold_Temperature_10', 'Mold_Temperature_11',
               'Mold_Temperature_12'], axis=1, inplace=True)


    return data 

machine_name = '650톤-우진2호기'

product_name = ["CN7 W/S SIDE MLD'G LH", "CN7 W/S SIDE MLD'G RH", "RG3 MOLD'G W/SHLD, LH", "RG3 MOLD'G W/SHLD, RH"]

cn7lh = make_input(label_data, machine_name, product_name[0])

cn7rh = make_input(label_data, machine_name, product_name[1])

rg3lh = make_input(label_data, machine_name, product_name[2])

rg3rh = make_input(label_data, machine_name, product_name[3])

cn7 = pd.concat([cn7lh, cn7rh], ignore_index=True)
rg3 = pd.concat([rg3lh, rg3rh], ignore_index=True)

rg3.drop(['Plasticizing_Position'], axis=1, inplace=True)

cn7['PassOrFail']=cn7['PassOrFail'].replace('Y', 0).replace('N', 1)

cn7.describe()

plt.subplots(figsize=(25,25))
sns.heatmap(data = cn7.corr(), annot=True, fmt='.2f', linewidths=.1, cmap='Blues')
