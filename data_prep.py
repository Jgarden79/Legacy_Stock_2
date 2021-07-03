import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def data_prep():
    data = pd.read_csv("val_mo_features.csv")
    data["Date"] = pd.to_datetime(data["Date"])
    qrt = list(data["Date"].dt.quarter)
    yr =  list(data["Date"].dt.year)
    q_dat = ['{}-{}'.format(qrt[i], yr[i]) for i in range(0, len(yr))]
    data['Timeframe'] = q_dat
    dat_df = pd.DataFrame()
    for d in data['Timeframe'].unique():
        x = data[data['Timeframe']==d]
        x['quartiles'] = pd.qcut(x["fwd_ret"], 2, labels=False)
        dat_df = pd.concat([dat_df, x])
    sectors = pd.read_csv("sectors.csv", index_col=0)
    data = dat_df
    data = data.merge(sectors, on="Instrument", how='outer')
    ohe = OneHotEncoder(sparse=False)
    ohe_dat = ohe.fit_transform(data["GICS Sector Name"].to_numpy().reshape(-1, 1))
    ohe_df = pd.DataFrame(ohe_dat, columns=ohe.get_feature_names())
    data = pd.concat([data, ohe_df], axis=1).sort_values("Date")
    data.to_csv("clean_raw.csv", index=False)
    #print(data)
    return data


if __name__ in "__main__":
    data_prep()
