def choose_feature():
    df = pd.DataFrame(data.groupby('session ID')[['session ID', 'country', 'price']].mean())
    df[['session ID', 'country']] = df[['session ID', 'country']].astype(int)
    df.rename(columns={'session ID': 'customers'}, inplace= True)
    df[['trousers', 'skirts', 'blouses', 'sale']] = 0 

def type_df()
    # make a list to divide type
    page_1 = ['', 'trousers', 'skirts', 'blouses', 'sale']
    # Count
    cr = 0
    for i, row in df.iterrows():
        print(i,end= ': ')
        while data['session ID'].iloc[cr] == row['customers']:
            row[page_1[data['page 1 (main category)'].iloc[cr]]]  += 1
            cr += 1
            if cr == 165474:
                break
        df.loc[i,['trousers', 'skirts', 'blouses', 'sale']] = row[['trousers', 'skirts', 'blouses', 'sale']]
