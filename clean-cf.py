import pandas as pd

years = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013']

for year in years:
	new_ranks = pd.DataFrame()
	curr = pd.read_csv('./Data/' + year + '/cf' + year + '.csv')
	for index, row in curr.iterrows():
		if row[3] != "ARG":
			new_ranks.append(row)
	new_ranks.to_csv('ARGranks' + year + '.csv')
