import pandas as pd
pd.set_option('max_rows', 500)
pd.set_option('max_columns', 500)
pd.set_option('max_colwidth', -1)
df = pd.read_csv('Emp_Churn.csv', sep = ';')
df.head()
Employee_ID	Age	Critical_Job_Role	Risk_of_Loss	Impact_of_Loss	Future_Leader	Gender	Generation	Managerial_Employee	Minority	Organization_Tenure_Months	Salary	Employment_Type	Employment_Type_2	High_Potential	Previous Functional Area	Previous Job Level	Previous Career Path	Previous Performance Rating	Previous Country	PrevCountryLat	PrevCountryLon	Previous Region	TimeInPrevPositionMonth	Current Functional Area	Current Job Level	Current Career Path	Current Performance Rating	Current Region	Current Country	CurCountryLat	CurCountryLon	Promotion within last 3 years	Changed Position within last 2 years	Change in Performance Rating	FunctionalAreaChangeType	JobLevelChangeType	Flight_Risk
0	10032	26	Yes	High	High	Yes	Female	Generation Y	Non-Managerial	Non-Minority	24	40000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Service	4 - Expert / Manager	Project / Management	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	No change	No change	No
1	10033	46	Yes	Low	High	Yes	Female	Generation X	Non-Managerial	Non-Minority	48	85000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Support	2 - Specialist	Functional	0 - No performance Measurement	EMEA	Germany	51.08342	10.423447	No	No	0 - Not available	No change	No change	No
2	10034	26	Yes	Medium	High	Yes	Female	Generation Y	Non-Managerial	Non-Minority	11	50000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Sales	3 - Senior	Functional	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	External Hire	External Hire	No
3	10035	26	Yes	High	High	Yes	Male	Generation Y	Non-Managerial	Non-Minority	22	40000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Service	1 - Associate	Functional	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	No change	No change	No
4	10038	26	Yes	Unallocated	Unallocated	Yes	Female	Generation Y	Non-Managerial	Non-Minority	34	30000	Part-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Service	4 - Expert / Manager	Functional	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	No change	No change	No
list(df)
['Employee_ID',
 'Age',
 'Critical_Job_Role',
 'Risk_of_Loss',
 'Impact_of_Loss',
 'Future_Leader',
 'Gender',
 'Generation',
 'Managerial_Employee',
 'Minority',
 'Organization_Tenure_Months',
 'Salary',
 'Employment_Type',
 'Employment_Type_2',
 'High_Potential',
 'Previous Functional Area',
 'Previous Job Level',
 'Previous Career Path',
 'Previous Performance Rating',
 'Previous Country',
 'PrevCountryLat',
 'PrevCountryLon',
 'Previous Region',
 'TimeInPrevPositionMonth',
 'Current Functional Area',
 'Current Job Level',
 'Current Career Path',
 'Current Performance Rating',
 'Current Region',
 'Current Country',
 'CurCountryLat',
 'CurCountryLon',
 'Promotion within last 3 years',
 'Changed Position within last 2 years',
 'Change in Performance Rating',
 'FunctionalAreaChangeType',
 'JobLevelChangeType',
 'Flight_Risk']
len(list(df))
38
df.shape
(19115, 38)
df['Employee_ID'].nunique()
19115
df['Age'].unique()
array([26, 46, 27, 30, 32, 49, 34, 29, 25, 24, 20, 18, 21, 22, 23, 45, 35,
       38, 41, 43, 31, 37, 28, 36, 40, 39, 42, 48, 47, 50, 44, 33, 19])
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 19115 entries, 0 to 19114
Data columns (total 38 columns):
Employee_ID                             19115 non-null int64
Age                                     19115 non-null int64
Critical_Job_Role                       19115 non-null object
Risk_of_Loss                            19115 non-null object
Impact_of_Loss                          19115 non-null object
Future_Leader                           19115 non-null object
Gender                                  19115 non-null object
Generation                              19115 non-null object
Managerial_Employee                     19115 non-null object
Minority                                19115 non-null object
Organization_Tenure_Months              19115 non-null int64
Salary                                  19115 non-null int64
Employment_Type                         19115 non-null object
Employment_Type_2                       19115 non-null object
High_Potential                          19115 non-null object
Previous Functional Area                12594 non-null object
Previous Job Level                      12594 non-null object
Previous Career Path                    12594 non-null object
Previous Performance Rating             12594 non-null object
Previous Country                        12594 non-null object
PrevCountryLat                          12594 non-null float64
PrevCountryLon                          12594 non-null float64
Previous Region                         12594 non-null object
TimeInPrevPositionMonth                 19115 non-null int64
Current Functional Area                 19115 non-null object
Current Job Level                       19115 non-null object
Current Career Path                     19115 non-null object
Current Performance Rating              19115 non-null object
Current Region                          19115 non-null object
Current Country                         19115 non-null object
CurCountryLat                           19115 non-null float64
CurCountryLon                           19115 non-null float64
Promotion within last 3 years           19115 non-null object
Changed Position within last 2 years    19115 non-null object
Change in Performance Rating            19115 non-null object
FunctionalAreaChangeType                19115 non-null object
JobLevelChangeType                      19115 non-null object
Flight_Risk                             19115 non-null object
dtypes: float64(4), int64(5), object(29)
memory usage: 5.5+ MB
df.loc[df['Previous Region'].isnull()]
Employee_ID	Age	Critical_Job_Role	Risk_of_Loss	Impact_of_Loss	Future_Leader	Gender	Generation	Managerial_Employee	Minority	Organization_Tenure_Months	Salary	Employment_Type	Employment_Type_2	High_Potential	Previous Functional Area	Previous Job Level	Previous Career Path	Previous Performance Rating	Previous Country	PrevCountryLat	PrevCountryLon	Previous Region	TimeInPrevPositionMonth	Current Functional Area	Current Job Level	Current Career Path	Current Performance Rating	Current Region	Current Country	CurCountryLat	CurCountryLon	Promotion within last 3 years	Changed Position within last 2 years	Change in Performance Rating	FunctionalAreaChangeType	JobLevelChangeType	Flight_Risk
0	10032	26	Yes	High	High	Yes	Female	Generation Y	Non-Managerial	Non-Minority	24	40000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Service	4 - Expert / Manager	Project / Management	0 - No performance Measurement	Americas	USA	39.783730	-100.445882	No	No	0 - Not available	No change	No change	No
1	10033	46	Yes	Low	High	Yes	Female	Generation X	Non-Managerial	Non-Minority	48	85000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Support	2 - Specialist	Functional	0 - No performance Measurement	EMEA	Germany	51.083420	10.423447	No	No	0 - Not available	No change	No change	No
2	10034	26	Yes	Medium	High	Yes	Female	Generation Y	Non-Managerial	Non-Minority	11	50000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Sales	3 - Senior	Functional	0 - No performance Measurement	Americas	USA	39.783730	-100.445882	No	No	0 - Not available	External Hire	External Hire	No
3	10035	26	Yes	High	High	Yes	Male	Generation Y	Non-Managerial	Non-Minority	22	40000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Service	1 - Associate	Functional	0 - No performance Measurement	Americas	USA	39.783730	-100.445882	No	No	0 - Not available	No change	No change	No
4	10038	26	Yes	Unallocated	Unallocated	Yes	Female	Generation Y	Non-Managerial	Non-Minority	34	30000	Part-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Service	4 - Expert / Manager	Functional	0 - No performance Measurement	Americas	USA	39.783730	-100.445882	No	No	0 - Not available	No change	No change	No
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
19110	17237	46	No	High	High	Yes	Male	Generation X	Managerial	Non-Minority	60	120000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	1	Sales	3 - Senior	Functional	4 - Exceeds Expectations	Americas	Canada	61.066692	-107.991707	No	No	0 - Not available	No change	No change	Yes
19111	17303	46	No	Unallocated	Unallocated	No	Female	Generation X	Non-Managerial	Non-Minority	204	70000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	1	Sales	4 - Expert / Manager	Functional	4 - Exceeds Expectations	Americas	USA	39.783730	-100.445882	Yes	No	0 - Not available	No change	No change	Yes
19112	17380	46	Yes	Unallocated	Unallocated	Yes	Male	Generation X	Non-Managerial	Non-Minority	136	50000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	1	R&D	3 - Senior	Functional	4 - Exceeds Expectations	Americas	USA	39.783730	-100.445882	No	No	0 - Not available	No change	No change	Yes
19113	27082	46	No	Unallocated	Unallocated	No	Female	Generation X	Non-Managerial	Non-Minority	204	70000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	0	Sales	2 - Specialist	Functional	2 - Partially Meets Expectations	EMEA	South Africa	-28.816624	24.991639	No	No	0 - Not available	External Hire	External Hire	Yes
19114	27342	46	No	Unallocated	Unallocated	No	Female	Generation X	Non-Managerial	Non-Minority	204	70000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	0	Sales	2 - Specialist	Functional	3 - Meets Expectations	EMEA	Saudi Arabia	25.624262	42.352833	No	No	0 - Not available	No change	No change	Yes
6521 rows × 38 columns

df.loc[(df['Previous Functional Area'].isnull())].to_csv('Fresher.csv')
df.loc[~(df['Previous Functional Area'].isnull())].to_csv('Experience.csv')
df.describe()
Employee_ID	Age	Organization_Tenure_Months	Salary	PrevCountryLat	PrevCountryLon	TimeInPrevPositionMonth	CurCountryLat	CurCountryLon
count	19115.000000	19115.000000	19115.000000	19115.000000	12594.000000	12594.000000	19115.000000	19115.000000	19115.000000
mean	19589.000000	30.206958	48.716191	62819.325137	38.768486	5.960068	19.885901	39.749109	4.282763
std	5518.169533	10.395162	79.363950	24133.731432	18.956135	71.502329	19.864530	18.354538	69.918683
min	10032.000000	18.000000	2.000000	4900.000000	-41.500083	-107.991707	0.000000	-41.500083	-107.991707
25%	14810.500000	20.000000	2.000000	40000.000000	35.000074	-7.979460	3.000000	36.574844	-7.979460
50%	19589.000000	28.000000	22.000000	63000.000000	40.033265	10.423447	9.000000	46.603354	10.423447
75%	24367.500000	39.000000	72.000000	70000.000000	51.083420	78.667743	36.000000	51.083420	25.920916
max	29146.000000	50.000000	1108.000000	120000.000000	64.686314	172.834408	396.000000	64.686314	172.834408
df.loc[~df['Previous Functional Area'].isnull()]['Previous Functional Area'].unique()
array(['R&D', 'Sales', 'Support', 'Marketing', 'Service'], dtype=object)
df.loc[~df['Previous Job Level'].isnull()]['Previous Job Level'].unique()
array(['2 - Specialist', '4 - Expert / Manager',
       '5 - Senior Expert / Senior Manager', '3 - Senior',
       '1 - Associate', '6 - Executive'], dtype=object)
df['Flight_Risk'].value_counts(dropna=False)
No     17015
Yes    2100 
Name: Flight_Risk, dtype: int64
df2 = df.copy()
df2.head()
Employee_ID	Age	Critical_Job_Role	Risk_of_Loss	Impact_of_Loss	Future_Leader	Gender	Generation	Managerial_Employee	Minority	Organization_Tenure_Months	Salary	Employment_Type	Employment_Type_2	High_Potential	Previous Functional Area	Previous Job Level	Previous Career Path	Previous Performance Rating	Previous Country	PrevCountryLat	PrevCountryLon	Previous Region	TimeInPrevPositionMonth	Current Functional Area	Current Job Level	Current Career Path	Current Performance Rating	Current Region	Current Country	CurCountryLat	CurCountryLon	Promotion within last 3 years	Changed Position within last 2 years	Change in Performance Rating	FunctionalAreaChangeType	JobLevelChangeType	Flight_Risk
0	10032	26	Yes	High	High	Yes	Female	Generation Y	Non-Managerial	Non-Minority	24	40000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Service	4 - Expert / Manager	Project / Management	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	No change	No change	No
1	10033	46	Yes	Low	High	Yes	Female	Generation X	Non-Managerial	Non-Minority	48	85000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Support	2 - Specialist	Functional	0 - No performance Measurement	EMEA	Germany	51.08342	10.423447	No	No	0 - Not available	No change	No change	No
2	10034	26	Yes	Medium	High	Yes	Female	Generation Y	Non-Managerial	Non-Minority	11	50000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Sales	3 - Senior	Functional	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	External Hire	External Hire	No
3	10035	26	Yes	High	High	Yes	Male	Generation Y	Non-Managerial	Non-Minority	22	40000	Full-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Service	1 - Associate	Functional	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	No change	No change	No
4	10038	26	Yes	Unallocated	Unallocated	Yes	Female	Generation Y	Non-Managerial	Non-Minority	34	30000	Part-Time	Regular	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	4	Service	4 - Expert / Manager	Functional	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	No change	No change	No
list(df2)
['Employee_ID',
 'Age',
 'Critical_Job_Role',
 'Risk_of_Loss',
 'Impact_of_Loss',
 'Future_Leader',
 'Gender',
 'Generation',
 'Managerial_Employee',
 'Minority',
 'Organization_Tenure_Months',
 'Salary',
 'Employment_Type',
 'Employment_Type_2',
 'High_Potential',
 'Previous Functional Area',
 'Previous Job Level',
 'Previous Career Path',
 'Previous Performance Rating',
 'Previous Country',
 'PrevCountryLat',
 'PrevCountryLon',
 'Previous Region',
 'TimeInPrevPositionMonth',
 'Current Functional Area',
 'Current Job Level',
 'Current Career Path',
 'Current Performance Rating',
 'Current Region',
 'Current Country',
 'CurCountryLat',
 'CurCountryLon',
 'Promotion within last 3 years',
 'Changed Position within last 2 years',
 'Change in Performance Rating',
 'FunctionalAreaChangeType',
 'JobLevelChangeType',
 'Flight_Risk']
del(df2['Previous Functional Area'])
del(df2['Previous Job Level'])
del(df2['Previous Career Path'])
del(df2['Previous Performance Rating'])
del(df2['Previous Country'])
del(df2['PrevCountryLat'])
del(df2['PrevCountryLon'])
del(df2['Previous Region'])
list(df2)
['Employee_ID',
 'Age',
 'Critical_Job_Role',
 'Risk_of_Loss',
 'Impact_of_Loss',
 'Future_Leader',
 'Gender',
 'Generation',
 'Managerial_Employee',
 'Minority',
 'Organization_Tenure_Months',
 'Salary',
 'Employment_Type',
 'Employment_Type_2',
 'High_Potential',
 'TimeInPrevPositionMonth',
 'Current Functional Area',
 'Current Job Level',
 'Current Career Path',
 'Current Performance Rating',
 'Current Region',
 'Current Country',
 'CurCountryLat',
 'CurCountryLon',
 'Promotion within last 3 years',
 'Changed Position within last 2 years',
 'Change in Performance Rating',
 'FunctionalAreaChangeType',
 'JobLevelChangeType',
 'Flight_Risk']
# Binning customers as Big spender, Moderate spender and Low spender
bins = [1, 22, 26, 28, 32, 36, 40, 44, 48, 52]
labels = [1,2,3, 4, 5, 6, 7, 8, 9]
df2['age_binned'] = pd.cut(df2['Age'], bins=bins, labels=labels)
df2.head()
Employee_ID	Age	Critical_Job_Role	Risk_of_Loss	Impact_of_Loss	Future_Leader	Gender	Generation	Managerial_Employee	Minority	Organization_Tenure_Months	Salary	Employment_Type	Employment_Type_2	High_Potential	TimeInPrevPositionMonth	Current Functional Area	Current Job Level	Current Career Path	Current Performance Rating	Current Region	Current Country	CurCountryLat	CurCountryLon	Promotion within last 3 years	Changed Position within last 2 years	Change in Performance Rating	FunctionalAreaChangeType	JobLevelChangeType	Flight_Risk	age_binned
0	10032	26	Yes	High	High	Yes	Female	Generation Y	Non-Managerial	Non-Minority	24	40000	Full-Time	Regular	No	4	Service	4 - Expert / Manager	Project / Management	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	No change	No change	No	2
1	10033	46	Yes	Low	High	Yes	Female	Generation X	Non-Managerial	Non-Minority	48	85000	Full-Time	Regular	No	4	Support	2 - Specialist	Functional	0 - No performance Measurement	EMEA	Germany	51.08342	10.423447	No	No	0 - Not available	No change	No change	No	8
2	10034	26	Yes	Medium	High	Yes	Female	Generation Y	Non-Managerial	Non-Minority	11	50000	Full-Time	Regular	No	4	Sales	3 - Senior	Functional	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	External Hire	External Hire	No	2
3	10035	26	Yes	High	High	Yes	Male	Generation Y	Non-Managerial	Non-Minority	22	40000	Full-Time	Regular	No	4	Service	1 - Associate	Functional	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	No change	No change	No	2
4	10038	26	Yes	Unallocated	Unallocated	Yes	Female	Generation Y	Non-Managerial	Non-Minority	34	30000	Part-Time	Regular	No	4	Service	4 - Expert / Manager	Functional	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	No change	No change	No	2
bins1 = [1, 12, 21, 40, 80, 1109]
labels1 = [1,2,3, 4, 5]
df2['tenure_binned'] = pd.cut(df2['Organization_Tenure_Months'], bins=bins1, labels=labels1)
df2.head()
Employee_ID	Age	Critical_Job_Role	Risk_of_Loss	Impact_of_Loss	Future_Leader	Gender	Generation	Managerial_Employee	Minority	Organization_Tenure_Months	Salary	Employment_Type	Employment_Type_2	High_Potential	TimeInPrevPositionMonth	Current Functional Area	Current Job Level	Current Career Path	Current Performance Rating	Current Region	Current Country	CurCountryLat	CurCountryLon	Promotion within last 3 years	Changed Position within last 2 years	Change in Performance Rating	FunctionalAreaChangeType	JobLevelChangeType	Flight_Risk	age_binned	tenure_binned
0	10032	26	Yes	High	High	Yes	Female	Generation Y	Non-Managerial	Non-Minority	24	40000	Full-Time	Regular	No	4	Service	4 - Expert / Manager	Project / Management	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	No change	No change	No	2	3
1	10033	46	Yes	Low	High	Yes	Female	Generation X	Non-Managerial	Non-Minority	48	85000	Full-Time	Regular	No	4	Support	2 - Specialist	Functional	0 - No performance Measurement	EMEA	Germany	51.08342	10.423447	No	No	0 - Not available	No change	No change	No	8	4
2	10034	26	Yes	Medium	High	Yes	Female	Generation Y	Non-Managerial	Non-Minority	11	50000	Full-Time	Regular	No	4	Sales	3 - Senior	Functional	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	External Hire	External Hire	No	2	1
3	10035	26	Yes	High	High	Yes	Male	Generation Y	Non-Managerial	Non-Minority	22	40000	Full-Time	Regular	No	4	Service	1 - Associate	Functional	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	No change	No change	No	2	3
4	10038	26	Yes	Unallocated	Unallocated	Yes	Female	Generation Y	Non-Managerial	Non-Minority	34	30000	Part-Time	Regular	No	4	Service	4 - Expert / Manager	Functional	0 - No performance Measurement	Americas	USA	39.78373	-100.445882	No	No	0 - Not available	No change	No change	No	2	3
df2['tenure_binned'].value_counts(dropna=False)
1    8384
5    4539
3    2735
4    2467
2    990 
Name: tenure_binned, dtype: int64
df2['age_binned'].value_counts(dropna=False)
1    6059
4    2361
2    2188
8    1818
3    1470
5    1449
6    1443
7    1311
9    1016
Name: age_binned, dtype: int64
bins2 = [4500, 20000, 40000, 60000, 80000, 100000, 125000]
labels2 = [1,2,3, 4, 5, 6]
df2['salary_binned'] = pd.cut(df2['Salary'], bins=bins2, labels=labels2)
df2['salary_binned'].value_counts(dropna=False)
4    7466
2    4806
3    3346
6    2010
5    1431
1    56  
Name: salary_binned, dtype: int64
(df2['Previous Functional Area']) = df['Previous Functional Area']
(df2['Previous Job Level']) = df['Previous Job Level']
(df2['Previous Career Path']) = df['Previous Career Path']
(df2['Previous Performance Rating']) = df['Previous Performance Rating']
(df2['Previous Country']) = df['Previous Country']
(df2['PrevCountryLat']) = df['PrevCountryLat']
(df2['PrevCountryLon']) = df['PrevCountryLon']
(df2['Previous Region']) = df['Previous Region']
list(df2)
['Employee_ID',
 'Age',
 'Critical_Job_Role',
 'Risk_of_Loss',
 'Impact_of_Loss',
 'Future_Leader',
 'Gender',
 'Generation',
 'Managerial_Employee',
 'Minority',
 'Organization_Tenure_Months',
 'Salary',
 'Employment_Type',
 'Employment_Type_2',
 'High_Potential',
 'TimeInPrevPositionMonth',
 'Current Functional Area',
 'Current Job Level',
 'Current Career Path',
 'Current Performance Rating',
 'Current Region',
 'Current Country',
 'CurCountryLat',
 'CurCountryLon',
 'Promotion within last 3 years',
 'Changed Position within last 2 years',
 'Change in Performance Rating',
 'FunctionalAreaChangeType',
 'JobLevelChangeType',
 'Flight_Risk',
 'age_binned',
 'tenure_binned',
 'salary_binned',
 'Previous Functional Area',
 'Previous Job Level',
 'Previous Career Path',
 'Previous Performance Rating',
 'Previous Country',
 'PrevCountryLat',
 'PrevCountryLon',
 'Previous Region']
df2.loc[df2['Previous Functional Area'].isnull(), 'Previous Functional Area'] = 'Fresher'
df2.loc[df2['Previous Job Level'].isnull(), 'Previous Job Level'] = 'Fresher'
df2.loc[df2['Previous Career Path'].isnull(), 'Previous Career Path'] = 'Fresher'
df2.loc[df2['Previous Performance Rating'].isnull(), 'Previous Performance Rating'] = 'Fresher'
df2.loc[df2['Previous Country'].isnull(), 'Previous Country'] = 'Fresher'
df2.loc[df2['PrevCountryLat'].isnull(), 'PrevCountryLat'] = 'Fresher'
df2.loc[df2['PrevCountryLon'].isnull(), 'PrevCountryLon'] = 'Fresher'
df2.loc[df2['Previous Region'].isnull(), 'Previous Region'] = 'Fresher'
from sklearn.preprocessing import LabelEncoder
Y = df2.iloc[list(df2).str.contains('Previous'), :]
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-58-a72ed89dbdd2> in <module>
----> 1 Y = df2.iloc[list(df2).str.contains('Previous'), :]

AttributeError: 'list' object has no attribute 'str'
df2.columns.get_loc("Previous Functional Area")
33
df2.columns.get_loc("Previous Region")
40
Y = df2.iloc[:, 33:40]
Y
Previous Functional Area	Previous Job Level	Previous Career Path	Previous Performance Rating	Previous Country	PrevCountryLat	PrevCountryLon
0	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher
1	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher
2	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher
3	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher
4	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher
...	...	...	...	...	...	...	...
19110	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher
19111	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher
19112	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher
19113	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher
19114	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher
19115 rows × 7 columns

lb_make = LabelEncoder()
df2['Previous Functional Area_new'] = lb_make.fit_transform(df2["Previous Functional Area"])
df2['Previous Job Level_new'] = lb_make.fit_transform(df2["Previous Job Level"])
df2['Previous Career Path_new'] = lb_make.fit_transform(df2["Previous Career Path"])
df2['Previous Performance Rating_new'] = lb_make.fit_transform(df2["Previous Performance Rating"])
df2['Previous Country_new'] = lb_make.fit_transform(df2["Previous Country"])
#df2['PrevCountryLat_new'] = lb_make.fit_transform(df2["PrevCountryLat"])
#df2['PrevCountryLon_new'] = lb_make.fit_transform(df2["PrevCountryLon"])
df2['Previous Region_new'] = lb_make.fit_transform(df2['Previous Region'])
df2["Previous Performance Rating"].value_counts(dropna=False)
Fresher                                  6521
3 - Meets Expectations                   5358
4 - Exceeds Expectations                 4929
5 - Consistently Exceeds Expectations    1875
2 - Partially Meets Expectations         394 
1 - Does Not Meet Expectations           38  
Name: Previous Performance Rating, dtype: int64
list(df2)
['Employee_ID',
 'Age',
 'Critical_Job_Role',
 'Risk_of_Loss',
 'Impact_of_Loss',
 'Future_Leader',
 'Gender',
 'Generation',
 'Managerial_Employee',
 'Minority',
 'Organization_Tenure_Months',
 'Salary',
 'Employment_Type',
 'Employment_Type_2',
 'High_Potential',
 'TimeInPrevPositionMonth',
 'Current Functional Area',
 'Current Job Level',
 'Current Career Path',
 'Current Performance Rating',
 'Current Region',
 'Current Country',
 'CurCountryLat',
 'CurCountryLon',
 'Promotion within last 3 years',
 'Changed Position within last 2 years',
 'Change in Performance Rating',
 'FunctionalAreaChangeType',
 'JobLevelChangeType',
 'Flight_Risk',
 'age_binned',
 'tenure_binned',
 'salary_binned',
 'Previous Functional Area',
 'Previous Job Level',
 'Previous Career Path',
 'Previous Performance Rating',
 'Previous Country',
 'PrevCountryLat',
 'PrevCountryLon',
 'Previous Region',
 'Previous Functional Area_new',
 'Previous Job Level_new',
 'Previous Career Path_new',
 'Previous Performance Rating_new',
 'Previous Country_new']
df2['Flight_Risk'].value_counts(dropna=False)
No     17015
Yes    2100 
Name: Flight_Risk, dtype: int64
df2_no = df2.loc[df2['Flight_Risk'] == 'No'].sample(n = 2100)
df2_no.shape
(2100, 46)
df2_no['Flight_Risk'].unique()
array(['No'], dtype=object)
df2_yes = df2.loc[df2['Flight_Risk'] == 'Yes']
df2_yes.shape
(2100, 46)
df2_yes['Flight_Risk'].unique()
array(['Yes'], dtype=object)
final_df = pd.concat([df2_yes, df2_no])
final_df.head()
Employee_ID	Age	Critical_Job_Role	Risk_of_Loss	Impact_of_Loss	Future_Leader	Gender	Generation	Managerial_Employee	Minority	Organization_Tenure_Months	Salary	Employment_Type	Employment_Type_2	High_Potential	TimeInPrevPositionMonth	Current Functional Area	Current Job Level	Current Career Path	Current Performance Rating	Current Region	Current Country	CurCountryLat	CurCountryLon	Promotion within last 3 years	Changed Position within last 2 years	Change in Performance Rating	FunctionalAreaChangeType	JobLevelChangeType	Flight_Risk	age_binned	tenure_binned	salary_binned	Previous Functional Area	Previous Job Level	Previous Career Path	Previous Performance Rating	Previous Country	PrevCountryLat	PrevCountryLon	Previous Region	Previous Functional Area_new	Previous Job Level_new	Previous Career Path_new	Previous Performance Rating_new	Previous Country_new
177	29137	18	No	Medium	Medium	No	Male	Generation Z	Non-Managerial	Non-Minority	2	30000	Full-Time	Temporary	No	0	Sales	4 - Expert / Manager	Project / Management	4 - Exceeds Expectations	EMEA	Germany	51.083420	10.423447	No	No	3 - Decreasing	Cross-Functional Move	Same Level	Yes	1	1	2	Support	4 - Expert / Manager	Project / Management	5 - Consistently Exceeds Expectations	Germany	51.0834	10.4234	EMEA	5	3	2	4	17
178	29138	18	No	Medium	Medium	Yes	Male	Generation Z	Non-Managerial	Non-Minority	2	30000	Full-Time	Temporary	No	0	Sales	4 - Expert / Manager	Functional	1 - Does Not Meet Expectations	EMEA	Germany	51.083420	10.423447	No	No	3 - Decreasing	Cross-Functional Move	Same Level	Yes	1	1	2	Support	4 - Expert / Manager	Functional	4 - Exceeds Expectations	Italy	42.6384	12.6743	EMEA	5	3	1	3	24
179	28107	18	No	Medium	Medium	Yes	Male	Generation Z	Non-Managerial	Non-Minority	2	30000	Full-Time	Temporary	No	0	Marketing	4 - Expert / Manager	Functional	4 - Exceeds Expectations	Americas	USA	39.783730	-100.445882	No	No	3 - Decreasing	Cross-Functional Move	Same Level	Yes	1	1	2	Sales	4 - Expert / Manager	Project / Management	5 - Consistently Exceeds Expectations	USA	39.7837	-100.446	Americas	3	3	2	4	54
180	18819	21	Yes	Unallocated	Unallocated	Yes	Male	Generation Y	Non-Managerial	Non-Minority	2	30000	Full-Time	Temporary	No	52	Service	4 - Expert / Manager	Functional	4 - Exceeds Expectations	EMEA	Netherlands	52.237989	5.534607	No	No	3 - Decreasing	Intra-Functional Move	Same Level	Yes	1	1	2	Service	4 - Expert / Manager	Project / Management	5 - Consistently Exceeds Expectations	Netherlands	52.238	5.53461	EMEA	4	3	2	4	29
181	18963	21	Yes	Unallocated	Unallocated	Yes	Female	Generation Y	Non-Managerial	Non-Minority	2	30000	Full-Time	Temporary	No	52	R&D	4 - Expert / Manager	Functional	3 - Meets Expectations	APJ	India	22.351115	78.667743	No	Yes	2 - Constant	Intra-Functional Move	Same Level	Yes	1	1	2	R&D	4 - Expert / Manager	Functional	3 - Meets Expectations	India	22.3511	78.6677	APJ	2	3	1	2	20
final_df.shape
(4200, 46)
final_df.to_csv('Refined.csv')
final_df.loc[final_df['Previous Country'] == 'Fresher'].shape
(1382, 46)
del(df2["Previous Country"])
del(df2["Previous Country_new"])
#del(df2["PrevCountryLat"])
#del(df2["PrevCountryLon"])
df2.shape
(19115, 45)
df2.loc[(df2['Flight_Risk'] == 'Yes') & (df2['Previous Functional Area'] == 'Fresher')].shape
(655, 45)
df2.loc[(df2['Flight_Risk'] == 'No') & (df2['Previous Functional Area'] == 'Fresher')].shape
(5866, 45)
df2.loc[(df2['Previous Functional Area'] == 'Fresher')].shape
(6521, 45)
sample_fresher_df = df2.loc[(df2['Previous Functional Area'] == 'Fresher')].sample(frac = 0.1)
experienced_df = df2.loc[(df2['Previous Functional Area'] != 'Fresher')]
experienced_df.shape
(12594, 45)
sample_df = pd.concat([sample_fresher_df, experienced_df])
sample_df.shape
(13246, 45)
sample_df['Flight_Risk'].value_counts(dropna=False)
No     11748
Yes    1498 
Name: Flight_Risk, dtype: int64
verification_yes = sample_df.loc[sample_df['Flight_Risk'] == 'Yes'].sample(n = 500)
verification_no = sample_df.loc[sample_df['Flight_Risk'] != 'Yes'].sample(n = 500)
verification_df = pd.concat([verification_yes, verification_no])
verification_df.shape
(1000, 45)
verification_df['Flight_Risk'].value_counts(dropna=False)
Yes    500
No     500
Name: Flight_Risk, dtype: int64
verification_df.head()
Employee_ID	Age	Critical_Job_Role	Risk_of_Loss	Impact_of_Loss	Future_Leader	Gender	Generation	Managerial_Employee	Minority	Organization_Tenure_Months	Salary	Employment_Type	Employment_Type_2	High_Potential	TimeInPrevPositionMonth	Current Functional Area	Current Job Level	Current Career Path	Current Performance Rating	Current Region	Current Country	CurCountryLat	CurCountryLon	Promotion within last 3 years	Changed Position within last 2 years	Change in Performance Rating	FunctionalAreaChangeType	JobLevelChangeType	Flight_Risk	age_binned	tenure_binned	salary_binned	Previous Functional Area	Previous Job Level	Previous Career Path	Previous Performance Rating	PrevCountryLat	PrevCountryLon	Previous Region	Previous Functional Area_new	Previous Job Level_new	Previous Career Path_new	Previous Performance Rating_new	Previous Region_new
17312	27911	18	Yes	High	High	Yes	Male	Generation Z	Non-Managerial	Non-Minority	2	63000	Full-Time	Temporary	No	0	Sales	3 - Senior	Functional	4 - Exceeds Expectations	APJ	Japan	36.574844	139.239418	No	Yes	2 - Constant	Cross-Functional Move	Same Level	Yes	1	1	4	Marketing	3 - Senior	Functional	4 - Exceeds Expectations	36.5748	139.239	APJ	1	2	1	3	0
17454	28053	18	Yes	High	High	Yes	Female	Generation Z	Non-Managerial	Non-Minority	2	63000	Full-Time	Temporary	No	0	F&A. HR. Administration	2 - Specialist	Functional	3 - Meets Expectations	APJ	Singapore	1.290475	103.852036	No	Yes	2 - Constant	Cross-Functional Move	Same Level	Yes	1	1	4	Sales	2 - Specialist	Functional	3 - Meets Expectations	1.29048	103.852	APJ	3	1	1	2	0
18726	26318	39	No	Low	Medium	No	Male	Generation X	Non-Managerial	Non-Minority	196	50000	Full-Time	Regular	No	24	R&D	3 - Senior	Functional	5 - Consistently Exceeds Expectations	Americas	USA	39.783730	-100.445882	Yes	Yes	2 - Constant	Intra-Functional Move	Promotion	Yes	6	5	3	R&D	2 - Specialist	Functional	5 - Consistently Exceeds Expectations	39.7837	-100.446	Americas	2	1	1	4	1
17455	28054	18	Yes	High	High	Yes	Female	Generation Z	Non-Managerial	Non-Minority	2	63000	Full-Time	Temporary	No	0	Support	2 - Specialist	Functional	3 - Meets Expectations	APJ	India	22.351115	78.667743	No	Yes	2 - Constant	Cross-Functional Move	Same Level	Yes	1	1	4	R&D	2 - Specialist	Functional	3 - Meets Expectations	22.3511	78.6677	APJ	2	1	1	2	0
18476	20056	32	No	Low	Medium	No	Male	Generation Y	Non-Managerial	Non-Minority	22	70000	Full-Time	Regular	No	52	Sales	4 - Expert / Manager	Functional	4 - Exceeds Expectations	Americas	USA	39.783730	-100.445882	No	No	3 - Decreasing	Intra-Functional Move	Same Level	Yes	4	3	4	Sales	4 - Expert / Manager	Functional	5 - Consistently Exceeds Expectations	39.7837	-100.446	Americas	3	3	1	4	1
del(verification_df['Flight_Risk'])
verification_df.shape
(1000, 44)
verification_df.to_csv('validation.csv', index = False)
sample_df_no = sample_df.loc[sample_df['Flight_Risk'] == 'No'].sample(n = 1498)
sample_df_no.shape
(1498, 45)
sample_df_yes = sample_df.loc[sample_df['Flight_Risk'] == 'Yes']
sample_df_yes.shape
(1498, 45)
final_df = pd.concat([sample_df_yes, sample_df_no])
final_df.shape
(2996, 45)
final_df.to_csv('Final_data.csv')
final_df.describe()
Employee_ID	Age	Organization_Tenure_Months	Salary	TimeInPrevPositionMonth	CurCountryLat	CurCountryLon	Previous Functional Area_new	Previous Job Level_new	Previous Career Path_new	Previous Performance Rating_new	Previous Region_new
count	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000
mean	22873.901869	28.748331	42.401869	62650.200267	21.395861	37.669055	11.083926	2.851469	2.245995	1.115154	2.730307	1.215621
std	4898.488692	10.475478	76.419810	22282.563984	20.704507	18.625920	76.737569	1.300431	1.267772	0.435208	0.899655	0.921404
min	10142.000000	18.000000	2.000000	20000.000000	0.000000	-41.500083	-107.991707	0.000000	0.000000	0.000000	0.000000	0.000000
25%	19432.750000	18.000000	2.000000	50000.000000	0.000000	35.000074	-53.200000	2.000000	1.000000	1.000000	2.000000	0.000000
50%	23547.000000	27.000000	11.000000	63000.000000	18.000000	39.783730	10.423447	3.000000	2.000000	1.000000	3.000000	1.000000
75%	27920.250000	38.000000	60.000000	65000.000000	37.000000	51.083420	78.667743	4.000000	3.000000	1.000000	3.000000	2.000000
max	29145.000000	50.000000	1108.000000	120000.000000	180.000000	64.686314	172.834408	5.000000	6.000000	2.000000	5.000000	3.000000
bins4 = [0, 3, 6, 9, 36, 400]
labels4 = [1,2,3, 4, 5]
final_df['TimeInPrevPositionMonth_binned'] = pd.cut(final_df['TimeInPrevPositionMonth'], bins=bins4, labels=labels4)
list(final_df)
['Employee_ID',
 'Age',
 'Critical_Job_Role',
 'Risk_of_Loss',
 'Impact_of_Loss',
 'Future_Leader',
 'Gender',
 'Generation',
 'Managerial_Employee',
 'Minority',
 'Organization_Tenure_Months',
 'Salary',
 'Employment_Type',
 'Employment_Type_2',
 'High_Potential',
 'TimeInPrevPositionMonth',
 'Current Functional Area',
 'Current Job Level',
 'Current Career Path',
 'Current Performance Rating',
 'Current Region',
 'Current Country',
 'CurCountryLat',
 'CurCountryLon',
 'Promotion within last 3 years',
 'Changed Position within last 2 years',
 'Change in Performance Rating',
 'FunctionalAreaChangeType',
 'JobLevelChangeType',
 'Flight_Risk',
 'age_binned',
 'tenure_binned',
 'salary_binned',
 'Previous Functional Area',
 'Previous Job Level',
 'Previous Career Path',
 'Previous Performance Rating',
 'PrevCountryLat',
 'PrevCountryLon',
 'Previous Region',
 'Previous Functional Area_new',
 'Previous Job Level_new',
 'Previous Career Path_new',
 'Previous Performance Rating_new',
 'Previous Region_new']
final_df.describe()
Employee_ID	Age	Organization_Tenure_Months	Salary	TimeInPrevPositionMonth	CurCountryLat	CurCountryLon	Previous Functional Area_new	Previous Job Level_new	Previous Career Path_new	Previous Performance Rating_new	Previous Region_new
count	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000	2996.000000
mean	22873.901869	28.748331	42.401869	62650.200267	21.395861	37.669055	11.083926	2.851469	2.245995	1.115154	2.730307	1.215621
std	4898.488692	10.475478	76.419810	22282.563984	20.704507	18.625920	76.737569	1.300431	1.267772	0.435208	0.899655	0.921404
min	10142.000000	18.000000	2.000000	20000.000000	0.000000	-41.500083	-107.991707	0.000000	0.000000	0.000000	0.000000	0.000000
25%	19432.750000	18.000000	2.000000	50000.000000	0.000000	35.000074	-53.200000	2.000000	1.000000	1.000000	2.000000	0.000000
50%	23547.000000	27.000000	11.000000	63000.000000	18.000000	39.783730	10.423447	3.000000	2.000000	1.000000	3.000000	1.000000
75%	27920.250000	38.000000	60.000000	65000.000000	37.000000	51.083420	78.667743	4.000000	3.000000	1.000000	3.000000	2.000000
max	29145.000000	50.000000	1108.000000	120000.000000	180.000000	64.686314	172.834408	5.000000	6.000000	2.000000	5.000000	3.000000
final_df.to_csv('Final_Data.csv')
final_df.to_csv('Final_Data_1.csv')
final_df.head()
Employee_ID	Age	Critical_Job_Role	Risk_of_Loss	Impact_of_Loss	Future_Leader	Gender	Generation	Managerial_Employee	Minority	Organization_Tenure_Months	Salary	Employment_Type	Employment_Type_2	High_Potential	TimeInPrevPositionMonth	Current Functional Area	Current Job Level	Current Career Path	Current Performance Rating	Current Region	Current Country	CurCountryLat	CurCountryLon	Promotion within last 3 years	Changed Position within last 2 years	Change in Performance Rating	FunctionalAreaChangeType	JobLevelChangeType	Flight_Risk	age_binned	tenure_binned	salary_binned	Previous Functional Area	Previous Job Level	Previous Career Path	Previous Performance Rating	PrevCountryLat	PrevCountryLon	Previous Region	Previous Functional Area_new	Previous Job Level_new	Previous Career Path_new	Previous Performance Rating_new	Previous Region_new	TimeInPrevPositionMonth_binned
18249	13587	32	No	Low	Medium	No	Female	Generation Y	Non-Managerial	Non-Minority	48	50000	Full-Time	Regular	No	5	R&D	3 - Senior	Functional	0 - No performance Measurement	Americas	Canada	61.066692	-107.991707	No	No	0 - Not available	No change	No change	Yes	4	4	3	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	0	6	0	5	3	2
1048	12225	20	Yes	Low	Low	Yes	Male	Generation Y	Non-Managerial	Non-Minority	24	40000	Full-Time	Temporary	No	3	Marketing	2 - Specialist	Functional	3 - Meets Expectations	Americas	Canada	61.066692	-107.991707	No	No	0 - Not available	No change	No change	Yes	1	3	2	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	0	6	0	5	3	1
3028	11589	20	Yes	High	High	Yes	Female	Generation Z	Non-Managerial	Non-Minority	15	65000	Full-Time	Temporary	No	2	Support	3 - Senior	Functional	2 - Partially Meets Expectations	APJ	China	35.000074	104.999927	No	No	0 - Not available	External Hire	External Hire	Yes	1	2	4	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	0	6	0	5	3	1
18077	13613	32	No	Medium	High	No	Female	Generation Y	Non-Managerial	Non-Minority	96	70000	Full-Time	Regular	No	5	Marketing	5 - Senior Expert / Senior Manager	Functional	0 - No performance Measurement	EMEA	Spain	40.002803	-4.003104	No	No	0 - Not available	No change	No change	Yes	4	5	4	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	0	6	0	5	3	2
18044	13331	25	Yes	High	High	Yes	Male	Generation Y	Non-Managerial	Minority	96	50000	Full-Time	Regular	No	5	Marketing	4 - Expert / Manager	Functional	0 - No performance Measurement	EMEA	Germany	51.083420	10.423447	No	No	0 - Not available	External Hire	External Hire	Yes	2	5	3	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	Fresher	0	6	0	5	3	2
refined_final_df = final_df[['Organization_Tenure_Months', 'Salary']]
refined_final_df
Organization_Tenure_Months	Salary
18249	48	50000
1048	24	40000
3028	15	65000
18077	96	70000
18044	96	50000
...	...	...
9380	120	40000
17156	2	63000
17998	2	20000
13444	2	63000
8585	108	50000
2996 rows × 2 columns

 