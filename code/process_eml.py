import pandas as pd

with open('eml.cd', 'r') as f:
    lines = f.readlines()
    lines = [l.split("\\") for l in lines]
    lines = [l[:10] for l in lines]

headers = [str(i) for i in range(len(lines[0]))]
headers[1] = 'WordString'
headers[2] = 'Frequency'
headers[3] = 'MorphStatus'
print(headers, len(headers))

df = pd.DataFrame(lines, columns=headers)
df['WordLength'] = df.apply(lambda row: len(row['WordString']), axis=1)
print(df)

df = df.query('WordLength>9 & MorphStatus=="M"')