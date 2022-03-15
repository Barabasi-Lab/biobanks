import pandas as pd

# Path to the micrsofot academic graph
PATH = "/work/ccnr/r.dorantesgilardi/2021-08-30"

def read_chunks(db, chunksize=10**6, sep='\t', base='mag'):
    with open(f"../headers/{db}") as f:
        cols = f.read().splitlines()
    return pd.read_csv(f"{PATH}/{base}/{db}",
                       chunksize=chunksize,
                       sep='\t',
                       names=cols,
                       low_memory=False)

def get_all_citations(papers):
    cites = []
    for chunk in read_chunks('PaperReferences.txt'):
        chunk = chunk[chunk['PaperReferenceId'].isin(papers)]
        cites.append(chunk)
    cites = pd.concat(cites)
    unique_cites = cites['PaperId'].unique()
    full = []
    for chunk in read_chunks('Papers.txt'):
        chunk = chunk[chunk['PaperId'].isin(unique_cites)]
        full.append(chunk)
    full = pd.concat(full)
    cites = cites.merge(full, how='left')
    
    return cites

def get_all_references(papers):
    cites = []
    for chunk in read_chunks('PaperReferences.txt'):
        chunk = chunk[chunk['PaperId'].isin(papers)]
        cites.append(chunk)
    cites = pd.concat(cites)
    unique_cites = cites['PaperId'].unique()
    full = []
    for chunk in read_chunks('Papers.txt'):
        chunk = chunk[chunk['PaperId'].isin(unique_cites)]
        full.append(chunk)
    full = pd.concat(full)
    cites = cites.merge(full, how='left')
    
    return cites