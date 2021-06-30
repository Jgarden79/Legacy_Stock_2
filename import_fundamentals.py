import time
from datetime import datetime
import eikon as ek
import numpy as np
import pandas as pd
from tqdm import tqdm
import config
ek.set_app_key(config.ek_key())


def get_r3k_stocks():
    """This function imports the Symbols (RICS) for all stocks in the iShares Russell 3K ETF do not run w/o a
    subscription to refinitive. """
    date = datetime.now().date().strftime('%Y-%m-%d')
    hold = ek.get_data('IWV', fields=[ek.TR_Field('TR.ETPConstituentRIC', params={'SDate': date})])[0]
    hold = hold[hold['Constituent RIC'] != 'GOOG.OQ']
    rics = [x for x in hold['Constituent RIC']]
    return rics


def get_rev_dat(stocks):
    """Gets Revenue data for a list of stocks and outputs a df"""
    fields = [
        ek.TR_Field('TR.F.OriginalAnnouncementDate', params={'SDate': 0, 'EDate': -19, 'Period': 'FQ0', 'Frq': 'FQ'}),
        ek.TR_Field('TR.F.TotRevBizActiv', params={'SDate': 0, 'EDate': -19, 'Period': 'FQ0', 'Frq': 'FQ'})]
    t = np.linspace(0, len(stocks), num=9, dtype='int')

    rev_df = pd.DataFrame()
    count = 0
    for i in tqdm(range(0, len(t))):
        try:
            df = ek.get_data(stocks[t[i]:t[i + 1]], fields=fields)[0]
        except:
            df = ek.get_data(stocks[t[i]:], fields=fields)[0]

        rev_df = pd.concat([rev_df, df])
        count += 1

    rev_df = rev_df.drop_duplicates()
    rev_df.to_csv('Revenue_df.csv', index=False)
    return rev_df


def get_inc_dat(stocks):
    """Gets Net income after taxes data for a list of stocks and outputs a df"""
    fields = [ek.TR_Field('TR.F.IncAvailToComShr', params={'SDate': 0, 'EDate': -19, 'Period': 'FQ0', 'Frq': 'FQ'}),
              ek.TR_Field('TR.F.OriginalAnnouncementDate',
                          params={'SDate': 0, 'EDate': -19, 'Period': 'FQ0', 'Frq': 'FQ'})]
    t = np.linspace(0, len(stocks), num=9, dtype='int')

    inc_df = pd.DataFrame()
    count = 0
    for i in tqdm(range(0, len(t))):
        try:
            df = ek.get_data(stocks[t[i]:t[i + 1]], fields=fields)[0]
        except:
            df = ek.get_data(stocks[t[i]:], fields=fields)[0]

        inc_df = pd.concat([inc_df, df])
        count += 1

    inc_df = inc_df.drop_duplicates()
    inc_df.to_csv('Net_income_df.csv', index=False)
    return inc_df


def get_ebit_dat(stocks):
    """Gets Normalized EBIT data for a list of stocks and outputs a df"""
    fields = [ek.TR_Field('TR.F.EBITNorm', params={'SDate': 0, 'EDate': -19, 'Period': 'FQ0', 'Frq': 'FQ'}),
              ek.TR_Field('TR.F.OriginalAnnouncementDate',
                          params={'SDate': 0, 'EDate': -19, 'Period': 'FQ0', 'Frq': 'FQ'})]
    t = np.linspace(0, len(stocks), num=9, dtype='int')

    ebit_df = pd.DataFrame()
    count = 0
    for i in tqdm(range(0, len(t))):
        try:
            df = ek.get_data(stocks[t[i]:t[i + 1]], fields=fields)[0]
        except:
            df = ek.get_data(stocks[t[i]:], fields=fields)[0]

        ebit_df = pd.concat([ebit_df, df])
        count += 1

    ebit_df = ebit_df.drop_duplicates()
    ebit_df.to_csv('EBIT_df.csv', index=False)
    return ebit_df


def get_book_dat(stocks):
    """Gets Equity to shareholders data for a list of stocks and outputs a df"""
    fields = [ek.TR_Field('TR.F.ComEqTot', params={'SDate': 0, 'EDate': -19, 'Period': 'FQ0', 'Frq': 'FQ'}),
              ek.TR_Field('TR.F.OriginalAnnouncementDate',
                          params={'SDate': 0, 'EDate': -19, 'Period': 'FQ0', 'Frq': 'FQ'})]
    t = np.linspace(0, len(stocks), num=9, dtype='int')

    book_df = pd.DataFrame()
    count = 0
    for i in tqdm(range(0, len(t))):
        try:
            df = ek.get_data(stocks[t[i]:t[i + 1]], fields=fields)[0]
        except:
            df = ek.get_data(stocks[t[i]:], fields=fields)[0]

        book_df = pd.concat([book_df, df])
        count += 1

    book_df = book_df.drop_duplicates()
    book_df.to_csv('Book_df.csv', index=False)
    return book_df


def get_ev_dat(stocks):
    """Gets Enterprise Value data for a list of stocks and outputs a df"""
    fields = [ek.TR_Field('TR.F.EV', params={'SDate': 0, 'EDate': -19, 'Period': 'FQ0', 'Frq': 'FQ'}),
              ek.TR_Field('TR.F.OriginalAnnouncementDate',
                          params={'SDate': 0, 'EDate': -19, 'Period': 'FQ0', 'Frq': 'FQ'})]
    t = np.linspace(0, len(stocks), num=9, dtype='int')

    ev_df = pd.DataFrame()
    count = 0
    for i in tqdm(range(0, len(t))):
        try:
            df = ek.get_data(stocks[t[i]:t[i + 1]], fields=fields)[0]
        except:
            df = ek.get_data(stocks[t[i]:], fields=fields)[0]

        ev_df = pd.concat([ev_df, df])
        count += 1

    ev_df = ev_df.drop_duplicates()
    ev_df.to_csv('EV_df.csv', index=False)
    return ev_df


def get_mktcap_dat(stocks):
    """Gets Market Cap data for a list of stocks and outputs a df"""
    fields = [ek.TR_Field('TR.F.MktCap', params={'SDate': 0, 'EDate': -19, 'Period': 'FQ0', 'Frq': 'FQ'}),
              ek.TR_Field('TR.F.OriginalAnnouncementDate',
                          params={'SDate': 0, 'EDate': -19, 'Period': 'FQ0', 'Frq': 'FQ'})]
    t = np.linspace(0, len(stocks), num=9, dtype='int')

    mcap_df = pd.DataFrame()
    count = 0
    for i in tqdm(range(0, len(t))):
        try:
            df = ek.get_data(stocks[t[i]:t[i + 1]], fields=fields)[0]
        except:
            df = ek.get_data(stocks[t[i]:], fields=fields)[0]

        mcap_df = pd.concat([mcap_df, df])
        count += 1

    mcap_df = mcap_df.drop_duplicates()
    mcap_df.to_csv('mktcap_df.csv', index=False)
    return mcap_df


if __name__ == "__main__":
    stock_list = get_r3k_stocks()
    time.sleep(3)
    rev_dat = get_rev_dat(stock_list)
    time.sleep(3)
    income = get_inc_dat(stock_list)
    time.sleep(3)
    ebit = get_ebit_dat(stock_list)
    time.sleep(3)
    book = get_book_dat(stock_list)
    time.sleep(3)
    ev = get_ev_dat(stock_list)
    time.sleep(3)
    mkt_cap = get_mktcap_dat(stock_list)
    print('Data Import Complete')
