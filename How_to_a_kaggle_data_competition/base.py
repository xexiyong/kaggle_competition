import pandas as pd
import numpy as np

shops_csv = 'data/shops.csv'
sales_train_csv = 'data/sales_train_v2.csv'
item_csv = 'data/items.csv'
item_category_csv = 'data/item_categories.csv'
test_csv = 'data/test.csv'
sample_submission_csv = 'data/sample_submission.csv'


def load_csv(f, index=False):
    if not index:
        raw_df = pd.read_csv(f, index_col=False)
    else:
        raw_df = pd.read_csv(f)
    return raw_df


def load():
    shops_df = load_csv(shops_csv)
    item_df = load_csv(item_csv)
    item_category_df = load_csv(item_category_csv)
    sales_train_df = load_csv(sales_train_csv)

    month_grp = pd.pivot_table(sales_train_df,
        index=['shop_id', 'item_id', 'date_block_num'], values=['item_cnt_day'], aggfunc=np.sum)
    month_grp.reset_index(inplace=True)

    # merge price
    pd.merge(month_grp, )


def get_sales_train_csv():
    sales_train_df = load_csv(sales_train_csv)
    print sales_train_df.head()

    item_id_price_df = sales_train_df.drop_duplicates(['item_id', 'item_price'], inplace=True)
    print item_id_price_df

    print item_id_price_df.shape[0]

    print item_id_price_df['item_id'].nunique()


get_sales_train_csv()
