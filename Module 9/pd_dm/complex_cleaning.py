import pandas as pd

data = {'text_column': ['Hello World', 'Python is AWESOME', 'Pandas is useful']}

df = pd.DataFrame(data)

df['lowercase_text'] = df['text_column'].str.lower()

df['replaced-text'] = df['text_column'].str.replace('is', 'is really')

df['contains_Python'] = df['text_column'].str.contains('Python')

print(df)