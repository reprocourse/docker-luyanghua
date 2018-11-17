import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('na_values')
args = parser.parse_args()

import pandas as pd

hie = pd.read_csv(args.file, na_values=args.na_values)

from statsmodels.formula.api import MNLogit

#hie['copeptin'] = hie['copeptin_6h_pmol_l'] + hie['copeptin_12h_pmol_l'] + hie['copeptin_24h_pmol_l'] + hie['copeptin_48h_pmol_l'] + hie['copeptin_72h_pmol_l'] + hie['copeptin_168h_pmol_l']

#hie['NSE'] = hie['NSE_6h_ng_ml'] + hie['NSE_12h_ng_ml'] + hie['NSE_24h_ng_ml'] + hie['NSE_48h_ng_ml'] + hie['NSE_72h_ng_ml'] + hie['NSE_168h_ng_ml']

#print(MNLogit(hie['outcome'], hie['copeptin'], missing='drop').fit().summary())

#print(MNLogit(hie['outcome'], hie['NSE'], missing='drop').fit().summary())

hie['intercept'] = 1

print(MNLogit(hie['outcome'], hie.filter(regex='intercept|copeptin_6h_pmol_l'), missing='drop').fit().summary())
print(MNLogit(hie['outcome'], hie.filter(regex='intercept|copeptin_12h_pmol_l'), missing='drop').fit().summary())
print(MNLogit(hie['outcome'], hie.filter(regex='intercept|copeptin_24h_pmol_l'), missing='drop').fit().summary())
print(MNLogit(hie['outcome'], hie.filter(regex='intercept|copeptin_48h_pmol_l'), missing='drop').fit().summary())
print(MNLogit(hie['outcome'], hie.filter(regex='intercept|copeptin_72h_pmol_l'), missing='drop').fit().summary())
print(MNLogit(hie['outcome'], hie.filter(regex='intercept|copeptin_168h_pmol_l'), missing='drop').fit().summary())

print(MNLogit(hie['outcome'], hie.filter(regex='intercept|NSE_6h_ng_ml'), missing='drop').fit().summary())
print(MNLogit(hie['outcome'], hie.filter(regex='intercept|NSE_12h_ng_ml'), missing='drop').fit().summary())
print(MNLogit(hie['outcome'], hie.filter(regex='intercept|NSE_24h_ng_ml'), missing='drop').fit().summary())
print(MNLogit(hie['outcome'], hie.filter(regex='intercept|NSE_48h_ng_ml'), missing='drop').fit().summary())
print(MNLogit(hie['outcome'], hie.filter(regex='intercept|NSE_72h_ng_ml'), missing='drop').fit().summary())
print(MNLogit(hie['outcome'], hie.filter(regex='intercept|NSE_168h_ng_ml'), missing='drop').fit().summary())
