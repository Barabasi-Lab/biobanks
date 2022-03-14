# Biobanks

This repository contains the code to create a table of articles taken from Microsoft Academic Graph introducing biobanks.


- **Version**: V1 
- **Creator**: Rodrigo Dorantes Gilardi [rodrigo.dorantes.gilardi\@gmail.com](mailto:rodrigo.dorantes.gilardi@gmail.com)
- **Last code update**: 03/14/2022 
- **Last data update**: 08/31/2021 
- **Keywords**: Biobanks; Cohort Studies;
- **Rights Statement**: Open Data Commons Attribution License (ODC-By) v1.0


## Methods

In order to obtain the dataset one needs to first obtain the full [Microsoft Academic Graph](https://www.microsoft.com/en-us/research/project/microsoft-academic-graph/) (MAG) in a directory where the code is going to be run.

The path to the MAG should be set in the script `serendipity.py` in the `python` subdirectory. Once this is set, the script `keywords.py` will return a first list of articles. These articles are based on a set of keywords usually contained in papers introducing biobanks (in the broad term, including cohorts of different sizes and purposes.).


The jupyter notebook `initial.ipynb` should be then run to obtain the final list from the automatized process. Both steps are explained in this notebook.

The final list of biobanks was manually curated to remove duplicates, and biobanks not human-based. In order to obtain the last version of this table, you need to run the script `manual_table.py` in the `python` directory. Note that in order to do so you will need to install the python module [gspread](https://docs.gspread.org/en/latest/).

The final list of biobanks is `biobanks.csv`.