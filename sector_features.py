import pandas as pd
import eikon as ek
import config
ek.set_app_key(config.ek_key())

def get_sectors():
    stocks = list(pd.read_csv('val_mo_features.csv')['Instrument'].unique())
    field = ek.TR_Field("TR.GICSSector")
    sectors = ek.get_data(stocks, fields=field)[0]
    sectors.to_csv("sectors.csv")
    return

if __name__ == "__main__":
    get_sectors()