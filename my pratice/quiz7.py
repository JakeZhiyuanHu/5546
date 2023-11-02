
import pandas as pd
import numpy as np


data = {
    'AUD/USD': [ 0.7280, 0.7209, np.nan, 0.7263, 0.7281, 0.7285,],
    'EUR/AUD': [ 1.6232, 1.6321, 1.6221, 1.6282, np.nan, 1.6288,],
    }
index = [ '2020-09-08', '2020-09-09', '2020-09-10', '2020-09-11', '2020-09-14', '2020-09-15',]
df = pd.DataFrame(data, index)



# Q1:

# NOTE: replace `put_your_answer_here`
sel_q1 = ['2020-09-08', '2020-09-14']
q1 = df.loc[sel_q1]



# Q2:

(start_q2, stop_q2) = (0, 2)
q2 = df.iloc[start_q2:stop_q2]


# Q3:

(start_q3, stop_q3) = ('2020-09-08', '2020-09-09')
q3 = df[start_q3:stop_q3]


# Q4:

row_sel_q4 = ['2020-09-08', '2020-09-09']
col_sel_q4 = ['AUD/USD']
q4 = df.loc[row_sel_q4, col_sel_q4]
