import pandas as pd
df = pd.read_csv('/work/adult.data.csv')
df.head()

# race_count
df.groupby('race')['race'].count()

# average_age_men
round(df.groupby('sex')['age'].mean()[1], 1)

# percentage_bachelors
round(df['education'].value_counts(normalize=True)['Bachelors'] * 100, 1)

# higher_education
# `Bachelors`, `Masters`, or `Doctorate`
round(df['education'].value_counts(normalize=True)[['Bachelors', 'Masters', 'Doctorate']].sum() * 100, 1)

# lower_education
# not `Bachelors`, `Masters`, or `Doctorate`
1 - df['education'].value_counts(normalize=True)[['Bachelors', 'Masters', 'Doctorate']].sum()

# higher_education_rich
df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['salary'].value_counts(normalize=True)['>50K']
round(df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['salary'].value_counts(normalize=True)['>50K'] * 100, 1)

# lower_education_rich
round(df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['salary'].value_counts(normalize=True)['>50K'] * 100, 1)


# min_work_hours
df['hours-per-week'].min()

# num_min_workers
df[df['hours-per-week'] == 1].shape[0]

# rich_percentage
round(df[df['hours-per-week'] == 1]['salary'].value_counts(normalize=True)['>50K'] * 100, 1)

# highest_earning_country
df.groupby('native-country')['salary'].value_counts(normalize=True).loc[:, ('>50K')].idxmax()

# highest_earning_country_percentage
round(df.groupby('native-country')['salary'].value_counts(normalize=True).loc[:, ('>50K')].max() * 100, 1)


# top_IN_occupation
df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
