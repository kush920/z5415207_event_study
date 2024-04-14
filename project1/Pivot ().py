import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-01', '2023-01-01',
             '2023-02-01', '2023-02-01', '2023-02-01', '2023-02-01',
             '2023-03-01', '2023-03-01'],
    'Region': ['North', 'East', 'South', 'West',
               'North', 'East', 'South', 'West',
               'North', 'East'],
    'Sales': [150, 200, 100, 130,
              180, 220, 110, 140,
              200, 210]
}

df = pd.DataFrame(data)

pivot_df = df.pivot_table(index='Date', columns='Region', values='Sales', aggfunc='sum')

print(pivot_df)
