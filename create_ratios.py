import pandas as pd


def create_price_ratios():
    mkt_cap = pd.read_csv("mktcap_df.csv")
    net_inc = pd.read_csv("Net_income_df.csv")
    book = pd.read_csv("Book_df.csv")
    mkt_cap_1 = pd.merge(mkt_cap, book, on=["Original Announcement Date Time", "Instrument"])
    mkt_cap = pd.merge(mkt_cap_1, net_inc, on=["Original Announcement Date Time", "Instrument"]).dropna()
    mkt_cap["e_p"] = mkt_cap["Income Available to Common Shares"] / mkt_cap["Market Capitalization"]
    mkt_cap["b_p"] = mkt_cap['Common Equity - Total'] / mkt_cap["Market Capitalization"]
    price_features = mkt_cap.drop(['Common Equity - Total', 'Income Available to Common Shares',
                                   'Market Capitalization'], axis=1)
    price_features.to_csv('price_ratios.csv', index=False)

    return


def create_ev_ratios():
    ev = pd.read_csv("EV_df.csv")
    ebit = pd.read_csv("EBIT_df.csv")
    rev = pd.read_csv("Revenue_df.csv")
    ev_1 = pd.merge(ev, ebit, on=["Original Announcement Date Time", "Instrument"])
    ev = pd.merge(ev_1, rev, on=["Original Announcement Date Time", "Instrument"]).dropna()
    ev["ebit_ev"] = ev["Earnings before Interest & Taxes (EBIT) - Normalized"] / ev["Enterprise Value"]
    ev["rev_ev"] = ev["Revenue from Business Activities - Total"] / ev["Enterprise Value"]
    ev_features = ev.drop(["Enterprise Value", "Revenue from Business Activities - Total",
                           "Earnings before Interest & Taxes (EBIT) - Normalized"], axis=1).drop_duplicates()

    ev_features.to_csv('ev_ratios.csv', index=False)

    return


def combine_ratios():
    price = pd.read_csv("price_ratios.csv")
    ev = pd.read_csv("ev_ratios.csv")
    combined = pd.merge(price, ev, on=["Original Announcement Date Time", "Instrument"]).drop_duplicates()
    combined.to_csv("valuation_features.csv", index=False)

    return


if __name__ == "__main__":
    create_price_ratios()
    create_ev_ratios()
    combine_ratios()
