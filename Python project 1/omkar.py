def find_null_values(dataset):
	dataset.isnull().sum().sum()
	num_null = dataset.isnull().sum()
	print("No of Null Values: {}".format(num_null))

def average_bat(dataset):
  total_bat = dataset['batsman_run'].sum()
  total_bat= len(dataset.index) - 1
  avg_runs = total_bat / total_bat
  print('Average of Batsman run for Ball_to_ball is: {}'.format(avg_runs))

def win_total_maches(dataset, win, total_matches):
  win = dataset.groupby('WinningTeam').count()
  win
  
  total_matches = dataset['Team1'].value_counts()+ dataset['Team2'].value_counts()
  total_matches
  
  win['Total matches']=total_matches
  win[["Total matches","WonBy"]].sort_values(by=["Total matches"],ascending=False).plot.bar(stacked=True,figsize=(7,3))

def runs_scored_ascending(most_runs):
  asc_most_runs = most_runs.sort_values(by="total_run", ascending=True)
  print(asc_most_runs)



