import pandas as pd


def create_mom_features():
    px_dat = pd.read_csv("price_dat.csv", index_col="Date")
    value = pd.read_csv("valuation_features.csv")
    raw_dates = list(value["Original Announcement Date Time"])
    dates = [i.split("T")[0] for i in raw_dates]
    value["Original Announcement Date Time"] = dates
    value = value.rename(columns={"Original Announcement Date Time":"Date"})
    stocks = value['Instrument'].unique()
    for s in stocks:
        try:
            prices = px_dat[s].reset_index()
            val_set = value[value['Instrument']==s]
            joint = pd.merge(val_set, prices, on="Date")
            print(joint)
            print(prices)

        except KeyError:
            print('{} Failed'.format(s))


if __name__ == "__main__":
    create_mom_features()