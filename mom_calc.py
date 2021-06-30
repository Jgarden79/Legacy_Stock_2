import pandas as pd


def mom_calc():
    px_df = pd.read_csv("price_dat.csv")
    vx_df = pd.read_csv("valuation_features.csv")
    dates = list(vx_df['Original Announcement Date Time'])
    adj_dates = [i.split("T")[0] for i in dates]
    vx_df['Original Announcement Date Time'] = adj_dates
    vx_df = vx_df.rename(columns={"Original Announcement Date Time": "Date"})
    px_df = px_df.set_index('Date')
    features = pd.DataFrame()

    for stock in vx_df['Instrument'].unique():
        try:
            px = px_df[stock]
            ninety_days = px.pct_change(63)
            ninety_days.name = "90_days"
            one_year = px.pct_change(250)
            one_year.name = "1_yr"
            px_sub = pd.concat([px, ninety_days, one_year], axis=1)
            vx = vx_df[vx_df['Instrument'] == stock].set_index('Date')
            comb = vx.join(px_sub, how='inner')
            comb = comb.rename(columns={stock: "price"})
            comb = comb.sort_index()
            comb['ret'] = comb['price'].pct_change()
            comb['fwd_ret'] = comb['ret'].shift(-1)
            comb = comb.drop(["price", "ret"], axis=1)
            features = pd.concat([features, comb])
            print('{} Passed'.format(stock))
        except:
            print('{} Fail'.format(stock))
            pass
    features = features.sort_index()
    features = features.drop_duplicates().dropna()
    print(features)
    features.to_csv("val_mo_features.csv")
    return features


if __name__ == "__main__":
    mom_calc()
