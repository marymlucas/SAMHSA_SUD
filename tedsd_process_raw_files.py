import warnings
warnings.filterwarnings('ignore')

import pandas as pd
from utils.teds_utils import*

fp = './opendata/samhsa_sud/'

# import raw data files from 2015 - 2021
df_2015 = pd.read_csv(f'{fp}teds_d/raw/tedsd_2015_puf.csv')
df_2016 = pd.read_csv(f'{fp}teds_d/raw/tedsd_2016_puf.csv')
df_2017 = pd.read_csv(f'{fp}teds_d/raw/tedsd_puf_2017.csv')
df_2018 = pd.read_csv(f'{fp}teds_d/raw/tedsd_puf_2018.csv')
df_2019 = pd.read_csv(f'{fp}teds_d/raw/tedsd_puf_2019.csv')
df_2020 = pd.read_csv(f'{fp}teds_d/raw/tedsd_puf_2020.csv')
df_2021 = pd.read_csv(f'{fp}teds_d/raw/tedsd_puf_2021.csv', encoding='latin-1', keep_default_na=False)

# retain common variables across these years
cols_2015 = set(df_2015.columns)
cols_2016 = set(df_2016.columns)
cols_2017 = set(df_2017.columns)
cols_2018 = set(df_2018.columns)
cols_2019 = set(df_2019.columns)
cols_2020 = set(df_2020.columns)
cols_2021 = set(df_2021.columns)

common_cols = cols_2015 & cols_2016 & cols_2017 \
    & cols_2018 & cols_2019 & cols_2020 & cols_2021

cols_to_keep = list(common_cols)
df_15 = df_2015[cols_to_keep]
df_16 = df_2016[cols_to_keep]
df_17 = df_2017[cols_to_keep]
df_18 = df_2018[cols_to_keep]
df_19 = df_2019[cols_to_keep]
df_20 = df_2020[cols_to_keep]
df_21 = df_2021[cols_to_keep]

# standardize coding of columns based on codebooks 2015-2021
# (I use 2021 to set baselines recoding as it is the first year with descriptive column values)

dfs_to_recode = [df_15, df_16, df_17, df_18, df_19, df_20]

# recode using mappings

## individual mappings
for df in dfs_to_recode:
    df.loc[:, 'AGE'] = df['AGE'].map(age_map)
    df.loc[:, 'GENDER'] = df['GENDER'].map(gender_map)
    df.loc[:, 'RACE'] = df['RACE'].map(race_map)
    df.loc[:, 'ETHNIC'] = df['ETHNIC'].map(ethnicity_map)
    df.loc[:, 'MARSTAT'] = df['MARSTAT'].map(marstat_map)
    df.loc[:, 'EDUC'] = df['EDUC'].map(educ_map)
    df.loc[:, 'PRIMINC'] = df['PRIMINC'].map(priminc_map)
    df.loc[:, 'REGION'] = df['REGION'].map(region_map)
    df.loc[:, 'DAYWAIT'] = df['DAYWAIT'].map(daywait_map)
    df.loc[:, 'REASON'] = df['REASON'].map(reason_map)
    df.loc[:, 'LOS'] = df['LOS'].map(los_map)
    df.loc[:, 'PSOURCE'] = df['PSOURCE'].map(psource_map)
    df.loc[:, 'NOPRIOR'] = df['NOPRIOR'].map(noprior_map)
    df.loc[:, 'IDU'] = df['IDU'].map(idu_map)
    df.loc[:, 'ALCDRUG'] = df['ALCDRUG'].map(alcdrug_map)
    df.loc[:, 'DSMCRIT'] = df['DSMCRIT'].map(dmscrit_map)
    df.loc[:, 'HLTHINS'] = df['HLTHINS'].map(hlthins_map)
    df.loc[:, 'PRIMPAY'] = df['PRIMPAY'].map(primpay_map)

## grouped mappings
for df in dfs_to_recode:
    for col in employ_cols:
        df.loc[:, col] = df[col].map(employ_map)
    for col in yes_no_cols:
        df.loc[:, col] = df[col].map(yes_no_map)
    for col in livarag_cols:
        df.loc[:, col] = df[col].map(livarag_map)
    for col in arrests_cols:
        df.loc[:, col] = df[col].map(arrests_map)
    for col in services_cols:
        df.loc[:, col] = df[col].map(services_map)
    for col in subs_cols:
        df.loc[:, col] = df[col].map(subs_map)
    for col in route_cols:
        df.loc[:, col] = df[col].map(route_map)
    for col in freq_cols:
        df.loc[:, col] = df[col].map(freq_map)
    for col in age_frstuse_cols:
        df.loc[:, col] = df[col].map(age_frstuse_map)
    for col in sub_rep_at_adm_cols:
        df.loc[:, col] = df[col].map(sub_rep_at_adm_map)
    for col in self_help_atnd_cols:
        df.loc[:, col] = df[col].map(self_help_atnd_map)

# Drop unnecessary cols, see notes doc
all_dfs = [df_15, df_16, df_17, df_18, df_19, df_20, df_21]
cols_to_drop = ['DETNLF', 'DETNLF_D', 'STFIPS', 'DIVISION', 'DETCRIM']

for df in all_dfs:
    df.drop(columns=cols_to_drop, inplace=True, errors='ignore')

# merge datasets and save
df_fin = pd.concat(all_dfs, ignore_index=True)

# reorder cols
df_fin = df_fin[['CASEID', 'DISYR', 'AGE', 'GENDER', 'RACE', 'ETHNIC', 'MARSTAT', 'EDUC',\
         'EMPLOY', 'EMPLOY_D', 'PREG', 'VET', 'LIVARAG', 'LIVARAG_D', 'PRIMINC', 'ARRESTS',\
         'ARRESTS_D', 'REGION', 'SERVICES', 'SERVICES_D', 'METHUSE', 'DAYWAIT', 'REASON',\
         'LOS', 'PSOURCE', 'NOPRIOR', 'SUB1', 'SUB1_D', 'ROUTE1', 'FREQ1', 'FREQ1_D',\
         'FRSTUSE1', 'SUB2', 'SUB2_D', 'ROUTE2', 'FREQ2', 'FREQ2_D', 'FRSTUSE2', 'SUB3', 'SUB3_D',\
         'ROUTE3', 'FREQ3', 'FREQ3_D', 'FRSTUSE3', 'IDU', 'ALCFLG', 'COKEFLG', 'MARFLG', 'HERFLG',\
         'METHFLG', 'OPSYNFLG', 'PCPFLG', 'HALLFLG', 'MTHAMFLG', 'AMPHFLG', 'STIMFLG', 'BENZFLG',\
         'TRNQFLG', 'BARBFLG', 'SEDHPFLG', 'INHFLG', 'OTCFLG', 'OTHERFLG', 'ALCDRUG', 'DSMCRIT',\
         'PSYPROB', 'HLTHINS', 'PRIMPAY', 'FREQ_ATND_SELF_HELP_D', 'FREQ_ATND_SELF_HELP']]

df_fin.to_csv(f'{fp}teds_d/derived/teds-d_15-21-clean.csv', index=False)
