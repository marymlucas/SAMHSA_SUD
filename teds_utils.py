age_map = {1: '12-14 years old',
           2: '15-17 years old',
           3: '18-20 years old',
           4: '21-24 years old',
           5: '25-29 years old',
           6: '30-34 years old',
           7: '35-39 years old',
           8: '40-44 years old',
           9: '45-49 years old',
           10: '50-54 years old',
           11: '55-64 years old',
           12: '65 years and older'}

gender_map = {1: 'Male',
              2: 'Female',
              -9: 'Missing/unknown/not collected/invalid'}

race_map = {1: 'Alaska Native (Aleut, Eskimo, Indian))',
            2: 'American Indian (other than Alaska Native)',
            3: 'Asian or Pacific Islander',
            4: 'Black or African American',
            5: 'White',
            6: 'Asian',
            7: 'Other single race',
            8: 'Two or more races',
            9: 'Native Hawaiian or Other Pacific Islander',
            -9: 'Missing/unknown/not collected/invalid'}

ethnicity_map = {1: 'Puerto Rican',
                 2: 'Mexican',
                 3: 'Cuban or other specific Hispanic',
                 4: 'Not of Hispanic or Latino origin',
                 5: 'Hispanic or Latino, specific origin not specified',
                 -9: 'Missing/unknown/not collected/invalid'}

marstat_map = {1: 'Never married',
               2: 'Now married',
               3: 'Separated',
               4: 'Divorced, widowed',
               -9: 'Missing/unknown/not collected/invalid'}

educ_map = {1: 'Less than one school grade, no schooling, nursery school, or kindergarten to Grade 8',
            2: 'Grades 9 to 11',
            3: 'Grade 12 (or GED)',
            4: '1-3 years of college, university, or vocational school',
            5: '4 years of college, university, BA/BS, some postgraduate study, or more',
            -9: 'Missing/unknown/not collected/invalid'}

employ_map = {1: 'Full-time',
              2: 'Part-time',
              3: 'Unemployed',
              4: 'Not in labor force',
              -9: 'Missing/unknown/not collected/invalid'}
employ_cols = ['EMPLOY', 'EMPLOY_D']

yes_no_map = {1: 'Yes',
              2: 'No',
              -9: 'Missing/unknown/not collected/invalid'}
yes_no_cols = ['PREG', 'VET', 'METHUSE', 'PSYPROB']

livarag_map = {1: 'Homeless',
               2: 'Dependent living',
               3: 'Independent living',
               -9: 'Missing/unknown/not collected/invalid'}
livarag_cols = ['LIVARAG', 'LIVARAG_D']

priminc_map = {1: 'Wages/salary',
               2: 'Public assistance',
               3: 'Retirement/pension, disability',
               4: 'Other',
               5: 'None',
               -9: 'Missing/unknown/not collected/invalid'}

arrests_map = {0: 'None',
               1: 'Once',
               2: 'Two or more times',
               -9: 'Missing/unknown/not collected/invalid'}
arrests_cols = ['ARRESTS', 'ARRESTS_D']

region_map = {0: 'U.S. jurisdictions/territories',
              1: 'Northeast',
              2: 'Midwest',
              3: 'South',
              4: 'West'}

services_map = {1: 'Detox, 24-hour, hospital inpatient',
                2: 'Detox, 24-hour, free-standing residential',
                3: 'Rehab/residential, hospital (non-detox)',
                4: 'Rehab/residential, short term (30 days or fewer)',
                5: 'Rehab/residential, long term (more than 30 days)',
                6: 'Ambulatory, intensive outpatient',
                7: 'Ambulatory, non-intensive outpatient',
                8: 'Ambulatory, detoxification'}
services_cols = ['SERVICES', 'SERVICES_D']

daywait_map = {0: '0',
               1: '1-7',
               2: '8-14',
               3: '15-30',
               4: '31 or more',
               -9: 'Missing/unknown/not collected/invalid'}

reason_map = {1: 'Treatment completed',
              2: 'Dropped out of treatment',
              3: 'Terminated by facility',
              4: 'Transferred to another treatment program or facility',
              5: 'Incarcerated',
              6: 'Death',
              7: 'Other'}

los_map =  {1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: '11',
            12: '12',
            13: '13',
            14: '14',
            15: '15',
            16: '16',
            17: '17',
            18: '18',
            19: '19',
            20: '20',
            21: '21',
            22: '22',
            23: '23',
            24: '24',
            25: '25',
            26: '26',
            27: '27',
            28: '28',
            29: '29',
            30: '30',
            31: '31 to 45 days',
            32: '46 to 60 days',
            33: '61 to 90 days',
            34: '91 to 120 days',
            35: '121 to 180 days',
            36: '181 to 365 days',
            37: 'More than a year',
            -9: 'Missing/unknown/not collected/invalid'}

psource_map = {1: 'Individual (includes self-referral)',
               2: 'Alcohol/drug use care provider',
               3: 'Other health care provider',
               4: 'School (educational)',
               5: 'Employer/EAP',
               6: 'Other community referral',
               7: 'Court/criminal justice referral/DUI/DWI',
               -9: 'Missing/unknown/not collected/invalid'}

noprior_map = {0: 'No prior treatment episode',
               1: 'One or more prior treatment episodes',
               -9: 'Missing/unknown/not collected/invalid'}

subs_map = {1: 'None',
           2: 'Alcohol',
           3: 'Cocaine/crack',
           4: 'Marijuana/hashish',
           5: 'Heroin',
           6: 'Non-prescription methadone',
           7: 'Other opiates and synthetics',
           8: 'PCP',
           9: 'Hallucinogens',
           10: 'Methamphetamine/speed',
           11: 'Other amphetamines',
           12: 'Other stimulants',
           13: 'Benzodiazepines',
           14: 'Other tranquilizers',
           15: 'Barbiturates',
           16: 'Other sedatives or hypnotics',
           17: 'Inhalants',
           18: 'Over-the-counter medications',
           19: 'Other drugs',
           -9: 'Missing/unknown/not collected/invalid'}
subs_cols = ['SUB1', 'SUB1_D', 'SUB2', 'SUB2_D', 'SUB3', 'SUB3_D']

route_map = {1: 'Oral',
             2: 'Smoking',
             3: 'Inhalation',
             4: 'Injection (intravenous, intramuscular, intradermal, or subcutaneous)',
             5: 'Other',
             -9: 'Missing/unknown/not collected/invalid'}
route_cols = ['ROUTE1', 'ROUTE2', 'ROUTE3']

freq_map = {1: 'No use in the past month',
            2: 'Some use',
            3: 'Daily use',
            -9: 'Missing/unknown/not collected/invalid'}
freq_cols = ['FREQ1', 'FREQ1_D', 'FREQ2', 'FREQ2_D', 'FREQ3', 'FREQ3_D']

age_frstuse_map = {1: '11 years and under',
               2: '12-14 years',
               3: '15-17 years',
               4: '18-20 years',
               5: '21-24 years',
               6: '25-29 years',
               7: '30 years and older',
               -9: 'Missing/unknown/not collected/invalid'}
age_frstuse_cols = ['FRSTUSE1', 'FRSTUSE2', 'FRSTUSE3']

idu_map = {0: 'IDU not reported',
           1: 'IDU reported',
           -9: 'No substances reported'}

sub_rep_at_adm_map = {0: 'Substance not reported',
                      1: 'Substance reported'}
sub_rep_at_adm_cols = ['ALCFLG', 'COKEFLG', 'MARFLG', 'HERFLG', 'METHFLG',
                       'OPSYNFLG', 'PCPFLG', 'HALLFLG', 'MTHAMFLG', 'AMPHFLG',
                       'STIMFLG', 'BENZFLG', 'TRNQFLG', 'BARBFLG', 'SEDHPFLG',
                       'INHFLG', 'OTCFLG', 'OTHERFLG']

alcdrug_map = {0: 'None',
               1: 'Alcohol only',
               2: 'Other drugs only',
               3: 'Alcohol and other drugs'}

dmscrit_map = {1: 'Alcohol-induced disorder',
               2: 'Substance-induced disorder',
               3: 'Alcohol intoxication',
               4: 'Alcohol dependence',
               5: 'Opioid dependence',
               6: 'Cocaine dependence',
               7: 'Cannabis dependence',
               8: 'Other substance dependence',
               9: 'Alcohol abuse',
               10: 'Cannabis abuse',
               11: 'Other substance abuse',
               12: 'Opioid abuse',
               13: 'Cocaine abuse',
               14: 'Anxiety disorders',
               15: 'Depressive disorders',
               16: 'Schizophrenia/other psychotic disorders',
               17: 'Bipolar disorders',
               18: 'Attention deficit/disruptive behavior disorders',
               19: 'Other mental health condition',
              -9: 'Missing/unknown/not collected/invalid'}

hlthins_map = {1: 'Private insurance, Blue Cross/Blue Shield, HMO',
               2: 'Medicaid',
               3: 'Medicare, other (e.g. TRICARE, CHAMPUS)',
               4: 'None',
               -9: 'Missing/unknown/not collected/invalid'}

primpay_map = {1: 'Self-pay',
               2: 'Private insurance (Blue Cross/Blue Shield, other health insurance, workers compensation)',
               3: 'Medicare',
               4: 'Medicaid',
               5: 'Other government payments',
               6: 'No charge (free, charity, special research, teaching)',
               7: 'Other',
               -9: 'Missing/unknown/not collected/invalid'}

self_help_atnd_map = {1: 'No attendance',
                      2: '1-3 times in the past month',
                      3: '4-7 times in the past month',
                      4: '8-30 times in the past month',
                      5: 'Some attendance, frequency is unknown',
                      -9: 'Missing/unknown/not collected/invalid'}
self_help_atnd_cols = ['FREQ_ATND_SELF_HELP', 'FREQ_ATND_SELF_HELP_D']