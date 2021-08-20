# %%

import pandas as pd
import yaml

with open(r"backend/scraper/configs.yaml") as file:
    configs = yaml.load(file, Loader=yaml.FullLoader)

dat_raw = pd.read_excel(
    configs["resources"]["spreadsheet_output"], sheet_name=None
)

# %%
