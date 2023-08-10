import panda as pd
df = pd.read_csv('data.csv')
df=df[df['Continent']=='South America']
countries= df['Country'].values
percentages= df['World Population Percentage'].values


