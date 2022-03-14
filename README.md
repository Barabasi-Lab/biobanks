# Biobanks


- **Version**: V1 
- **Creator**: Deisy Morselli Gysi [deisy.ccnr\@gmail.com](mailto:deisy.ccnr@gmail.com)
- **Last code update**: 03/10/2022 
- **Last data update**: 01/04/2022 
- **Keywords**: Drug Bank; Drug Targets;
- **Rights Statement**: Creative Common's Attribution-NonCommercial 4.0 International License.

### Methodology

This is a parser for the `XML` file provided by [DrugBank](https://go.drugbank.com/releases/latest).

The file `code/R/parser_db_functions.R` contains the necessary functions for parsing the data - and it is sourced by `code/R/parser_db.R` - the parser.

#### Functions

Four functions are available for parsing:

-   `get_drug_targets(DB)`: This function parses the drug bank to retrieve information regarding drug and target information. Saves a files named `out/DB_Drug_Targets_<version>.csv`, with the following variables: 
    -   ID \<chr>: Drug ID in DrugBank
    -   Name \<chr>: Official drug name in DrugBank
    -   Description \<chr>: Drug description
    -   Started_commer \<date>: Started commercialization
    -   Ended_commer \<date>: Stopped commercialization
    -   ATC \<chr>: Drug ATC code
    -   State \<chr>: Drug state (liquid, solid, gas)
    -   Approved \<chr>: FDA status of the drug (approved, experimental, investigational, nutraceutical, withdrawn, illicit, vet_approved)
    -   Indication \<chr>: Drug indication
    -   Gene_Target \<chr>: Gene target (HGNC symbol)
    -   DB_id \<chr>: Bio-Entity ID
    -   name \<chr>: Gene name descriptor
    -   organism \<chr>: Organism
    -   Type \<chr>: Type of the target (Polypeptide, Enzyme, Carrier, Transporter)
    -   known_action \<chr>: Target has a known action
    -   id_target \<chr>: Protein ID of the target
    -   id_source \<chr>: Platform for the protein ID of the target


-   `get_drug_synonym(DB)`: This functions parses the alternative names for the drugs. This function saves a files named `out/DB_Drug_Dictionary_<version>.csv`, with the following variables:
    -   ID \<chr>: Drug ID in DrugBank
    -   Name \<chr>: Official drug name in DrugBank
    -   Synonym \<chr>: Synonym names for the drug


-   `get_drug_identifier(DB)`: This function identifies the external identifiers for each drug. This function saves a files named `out/DB_Drug_External_ID_<version>.csv`, with the following variables:
    -   ID \<chr>: Drug ID in DrugBank
    -   Name \<chr>: Official drug name in DrugBank
    -   Source \<chr>: External source name (Drugs Product Database (DPD), PubChem Substance, ChEBI, PubChem Compound, ChemSpider, Wikipedia, KEGG Drug, RxCUI, ChEMBL, BindingDB, UniProtKB, KEGG Compound, ZINC)
    -   ID_external \<chr>: External source ID


-   `get_drug_publication(DB)`: This function collects the publications that are associated to each drug. This function saves a files named `out/DB_Drug_Publications_<version>.csv`, with the following variables:
    -   ID \<chr>: Drug ID in DrugBank
    -   Name \<chr>: Official drug name in DrugBank
    -   pubmed-id \<chr>: PUBMED ID
    -   citation \<chr>: Citation
    -   ref-id \<chr>: Reference ID


#### Running the parser

For running `code/R/parser_db.R` you need to define the `version`of the DrugBank - and the `path` where the `raw/` data can be found, and there the output - `out/` - files will be saved.

-   `version = "v5.1.9"`
-   `path = "~/Dropbox (CCNR)/Biology/99_Toolbox/data/DrugBank/data/"`

An option - for speeding the process and saving space - is to store the `XML` as `.RData` (code is commented).

```r
# DB <- xml2::read_xml(paste0(path,  "raw/full database_",version,".xml"))
# DB = xml2::as_list(DB)
# DB = DB$drugbank
# save(DB, file = paste0(path,  "raw/full database_", version,".RData"))
```

Once the functions are loaded, you run them as following: 

```r
get_drug_targets(DB, Path = path, Version = version)
get_drug_synonym(DB, Path = path, Version = version)
get_drug_identifier(DB, Path = path, Version = version)
get_drug_publication(DB, Path = path, Version = version)
```

Data will be saved in the `/out/` folder specified in `path`
