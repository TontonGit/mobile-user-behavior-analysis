def standardize_columns(df):
    
    ''' Use this function to standardize the columns names.'''

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('(', '', regex=False)
        .str.replace(')', '', regex=False)
        .str.replace('/', '_per_', regex=False)
        )
    return df
    


    
