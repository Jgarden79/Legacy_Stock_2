import time
from datetime import datetime
import eikon as ek
import pandas as pd

import config

ek.set_app_key(config.ek_key())


def get_px_dat():
    valuation = pd.read_csv("valuation_features.csv")
    stock_list = list(valuation["Instrument"].unique())
    ts_list = list(valuation["Original Announcement Date Time"])
    dates = [i.split('T')[0] for i in ts_list]
    valuation["Original Announcement Date Time"] = dates
    valuation["Original Announcement Date Time"] = pd.to_datetime(valuation["Original Announcement Date Time"])
    s_date = valuation["Original Announcement Date Time"].min()
    e_date = valuation["Original Announcement Date Time"].max()
    s_date = datetime.strftime(s_date, "%Y-%m-%d")
    e_date = datetime.strftime(e_date, "%Y-%m-%d")
    px_dat = pd.DataFrame()
    count = 0
    for g in range(0, len(stock_list)):
        s = stock_list[g]
        try:
            x_df = ek.get_timeseries(s, fields='CLOSE', start_date=s_date, end_date=e_date)
            x_df = x_df.rename(columns={"CLOSE": s})
            px_dat = px_dat.join(x_df, how="outer")
            count += 1
            print("{} of {} {} complete w/{} rows".format(s, count, len(stock_list), len(x_df)))
        except:
            count += 1
            print("{} of {} Failed to retrieve data for {}".format(s, count, len(stock_list)))
        if count % 100 == 0:
            time.sleep(40)
        else:
            time.sleep(1)
    px_dat.to_csv("price_dat.csv")

    return px_dat


if __name__ == "__main__":
    get_px_dat()
