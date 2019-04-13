import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  

  

#==============================================================================
# 1. Reaad in the Batting.csv and Pitching.csv files into two pandas dataframes.
#==============================================================================
read_batting_df = pd.read_csv("Batting.csv")
read_pitching_df = pd.read_csv("Pitching.csv")

#==============================================================================
# 2. Create Two dataframes are for the hitting statistics from the 20 years prior to integration 
# and 20 years after integration, and two dataframes are for the pitching statistics from the 20 years prior to integration.
# I used the .isin() function to isolate the years for each period.
#==============================================================================

prior_hitting_df = read_batting_df[read_batting_df['yearID'].isin(range(1926, 1947))]
post_hitting_df = read_batting_df[read_batting_df['yearID'].isin(range(1947, 1968))]

prior_pitching_df = read_pitching_df[read_pitching_df['yearID'].isin(range(1926, 1947))]
post_pitching_df = read_pitching_df[read_pitching_df['yearID'].isin(range(1947, 1968))]

#==============================================================================
# 2a. Check that the data frames are accurate
#==============================================================================
check1 = set(prior_hitting_df['yearID'])
check2 = set(post_hitting_df['yearID'])
check3 = set(prior_pitching_df['yearID'])
check4 = set(post_pitching_df['yearID'])
print('2a. Check to ensure that the years are accurate')
print(sorted(check1))
print(sorted(check2))
print(sorted(check3))
print(sorted(check4))
print('##############################################')
print('')
print('')

#==============================================================================
# 3. Summary statistics for hitting
#==============================================================================
print('3. Below are the Summary statistics for hitting:')

print("Runs prior and post:")
print(prior_hitting_df.groupby(prior_hitting_df['yearID'])['R'].sum()) 
print(post_hitting_df.groupby(post_hitting_df['yearID'])['R'].sum())

print("Stolen bases prior and post:")
print(prior_hitting_df.groupby(prior_hitting_df['yearID'])['SB'].sum()) 
print(post_hitting_df.groupby(post_hitting_df['yearID'])['SB'].sum())

print("Hits prior and post:")
print(prior_hitting_df.groupby(prior_hitting_df['yearID'])['H'].sum()) 
print(post_hitting_df.groupby(post_hitting_df['yearID'])['H'].sum())

print("Home Runs prior and post:")
print(prior_hitting_df.groupby(prior_hitting_df['yearID'])['HR'].sum()) 
print(post_hitting_df.groupby(post_hitting_df['yearID'])['HR'].sum())

print("Run difference between post and prior: {0}".format(post_hitting_df['R'].sum() - prior_hitting_df['R'].sum()))
print("Stolen Bases difference between post and prior: {0}".format(post_hitting_df['SB'].sum() - prior_hitting_df['SB'].sum()))
print("Hits difference between post and prior: {0}".format(post_hitting_df['H'].sum() - prior_hitting_df['H'].sum()))
print("Home Run difference between post and prior: {0}".format(post_hitting_df['HR'].sum() - prior_hitting_df['HR'].sum()))
print('#######################################################')
print('')
print('')
#==============================================================================
# 4. Advanced Hitting statistic - Slugging Percentage
#==============================================================================
print('4. Below is an advanced statistic for hitting:')

#Formula for SLG percentage
def calc_SLG(Single, Double, Triple, HR, AB):
    return (Single + (2 *Double) + (3*Triple) + (4*HR)) / AB

#limit the statistics on more than the average ABs
prior_hitting_no_0_ABs_df = prior_hitting_df[prior_hitting_df['AB'] >= prior_hitting_df['AB'].mean() ]
post_hitting_no_0_ABs_df = post_hitting_df[post_hitting_df['AB'] >= post_hitting_df['AB'].mean()]


#Add a column for singles
prior_hitting_no_0_ABs_df.loc[:,'1B'] = prior_hitting_no_0_ABs_df['H'] - (prior_hitting_no_0_ABs_df['2B']+ prior_hitting_no_0_ABs_df['3B']+ prior_hitting_no_0_ABs_df['HR'])
post_hitting_no_0_ABs_df.loc[:,'1B'] = post_hitting_no_0_ABs_df['H'] - (post_hitting_no_0_ABs_df['2B']+ post_hitting_no_0_ABs_df['3B']+ post_hitting_no_0_ABs_df['HR'])

#Now compute the slugging percentage
prior_hitting_no_0_ABs_df.loc[:, 'SLG'] = calc_SLG(prior_hitting_no_0_ABs_df['1B'], prior_hitting_no_0_ABs_df['2B'], prior_hitting_no_0_ABs_df['3B'], prior_hitting_no_0_ABs_df['HR'], prior_hitting_no_0_ABs_df['AB'])
post_hitting_no_0_ABs_df.loc[:, 'SLG'] = calc_SLG(post_hitting_no_0_ABs_df['1B'], post_hitting_no_0_ABs_df['2B'], post_hitting_no_0_ABs_df['3B'], post_hitting_no_0_ABs_df['HR'], post_hitting_no_0_ABs_df['AB'])

print("The average Slugging percentage prior to integration was:{0}".format(prior_hitting_no_0_ABs_df['SLG'].mean()))
print("The average Slugging percentage post integration was:{0}".format(post_hitting_no_0_ABs_df['SLG'].mean()))
print("The max Slugging percentage prior to integration was:{0}".format(prior_hitting_no_0_ABs_df['SLG'].max()))
print("The max Slugging percentage post integration was:{0}".format(post_hitting_no_0_ABs_df['SLG'].max()))
print('#######################################################')
print('')
print('')


#==============================================================================
# 5. Summary statistics for pitching
#==============================================================================
print('5. Summary statistics for pitching')
print("ERA prior and post:")
print(prior_pitching_df.groupby(prior_pitching_df['yearID'])['ERA'].mean()) 
print(post_pitching_df.groupby(post_pitching_df['yearID'])['ERA'].mean())

print("Earned runs prior and post:")
print(prior_pitching_df.groupby(prior_pitching_df['yearID'])['ER'].sum()) 
print(post_pitching_df.groupby(post_pitching_df['yearID'])['ER'].sum())

print("Strikeouts prior and post:")
print(prior_pitching_df.groupby(prior_pitching_df['yearID'])['SO'].sum()) 
print(post_pitching_df.groupby(post_pitching_df['yearID'])['SO'].sum())

print("Opponents batting average against:")
print(prior_pitching_df.groupby(prior_pitching_df['yearID'])['BAOpp'].mean()) 
print(post_pitching_df.groupby(post_pitching_df['yearID'])['BAOpp'].mean())

print("The ERA difference between post and prior: {0}".format(post_pitching_df['ERA'].mean() - prior_pitching_df['ERA'].mean()))
print("The number of Earned Runs difference between post and prior: {0}".format(post_pitching_df['ER'].sum() - prior_pitching_df['ER'].sum()))
print("The strikeouts difference between post and prior: {0}".format(post_pitching_df['SO'].sum() - prior_pitching_df['SO'].sum()))
print("The opponents batting average against between post and prior: {0}".format(post_pitching_df['BAOpp'].mean() - prior_pitching_df['BAOpp'].mean()))
print('##############################################')
print('')
print('')
#==============================================================================
# 6. Advanced Pitching statistic - Walks + Hits to Innings Pitched (WHIP)
#==============================================================================
print('6. Advanced Pitching statistic - Walks + Hits to Innings Pitched (WHIP)')
#Formula for WHIP
def calc_WHIP(BB, H, IP):
    return (BB + H) / (IP / 3)
#Remove all rows from dataframes where IP = 0
prior_pitching_no_0_IP_df = prior_pitching_df[prior_pitching_df['IPouts'] > 0 ]
post_pitching_no_0_IP_df = post_pitching_df[post_pitching_df['IPouts'] > 0 ]

prior_pitching_no_0_IP_df.loc[:, 'WHIP'] = calc_WHIP(prior_pitching_no_0_IP_df['BB'], prior_pitching_no_0_IP_df['H'], prior_pitching_no_0_IP_df['IPouts'])
post_pitching_no_0_IP_df.loc[:, 'WHIP'] = calc_WHIP(post_pitching_no_0_IP_df['BB'], post_pitching_no_0_IP_df['H'], post_pitching_no_0_IP_df['IPouts'])

print("The WHIP over years")
print(prior_pitching_no_0_IP_df.groupby(prior_pitching_df['yearID'])['WHIP'].mean()) 
print(post_pitching_no_0_IP_df.groupby(post_pitching_df['yearID'])['WHIP'].mean())

print("The average WHIP prior to integration was:{0}".format(prior_pitching_no_0_IP_df['WHIP'].mean()))
print("The average WHIP post integration was:{0}".format(post_pitching_no_0_IP_df['WHIP'].mean()))
print('##############################################')
print('')
print('')

#==============================================================================
# 7. Team Data
#==============================================================================
print('7. Team Data')
read_Team_Table_df = pd.read_csv("Teams.csv")
Prior_Teams_df = read_Team_Table_df[read_Team_Table_df['yearID'].isin(range(1926, 1946))]
Post_Teams_df = read_Team_Table_df[read_Team_Table_df['yearID'].isin(range(1947, 1967))]

Prior_Teams_df.loc[:,'Win_Pct'] = Prior_Teams_df['W'] / Prior_Teams_df['G']
Post_Teams_df.loc[:,'Win_Pct'] = Post_Teams_df['W'] / Post_Teams_df['G']

print(Prior_Teams_df.groupby(Prior_Teams_df['franchID'])['W'].sum())
print(Post_Teams_df.groupby(Post_Teams_df['franchID'])['W'].sum()) 

Prior_Cum_Teams_Records_df = pd.concat([Prior_Teams_df['franchID'], Prior_Teams_df['W'], Prior_Teams_df['L'], Prior_Teams_df['Win_Pct']], axis=1, keys=['Team', 'Wins', 'Losses', 'PCT'])


Prior_Cum_Teams_Records_df = pd.concat([Prior_Teams_df['franchID'], Prior_Teams_df['W'], Prior_Teams_df['L'], Prior_Teams_df['Win_Pct']], axis=1, keys=['Team', 'Wins', 'Losses', 'PCT'])
Post_Cum_Teams_Records_df = pd.concat([Post_Teams_df['franchID'], Post_Teams_df['W'], Post_Teams_df['L'], Post_Teams_df['Win_Pct']], axis=1, keys=['Team', 'Wins', 'Losses', 'PCT'])



print(Prior_Teams_df.groupby(Prior_Teams_df['franchID'])['Win_Pct'].mean())
print(Post_Teams_df.groupby(Post_Teams_df['franchID'])['Win_Pct'].mean())
print(Post_Teams_df.groupby(Post_Teams_df['franchID'])['Win_Pct'].mean() - Prior_Teams_df.groupby(Prior_Teams_df['franchID'])['Win_Pct'].mean())
print('##############################################')
print('')
print('')
#==============================================================================
#8. Analysis of HR data
#==============================================================================
print('Summary of HR and Strikeouts')
print('')
read_Master_df = pd.read_csv("Master.csv")

post_HR_hitters_df = pd.concat([post_hitting_df['playerID'], post_hitting_df['HR']], axis=1, keys=['playerID', 'HR'])
post_SO_pitchers_df = pd.concat([post_pitching_df['playerID'], post_pitching_df['SO']], axis=1, keys=['playerID', 'SO'])


post_HR_Master_df = post_HR_hitters_df.merge(read_Master_df, on='playerID')
post_SO_Master_df = post_SO_pitchers_df.merge(read_Master_df, on='playerID')
print('HR hitters post-integration')
print(post_HR_Master_df.groupby(['playerID','nameLast','nameFirst'])['HR'].sum().sort_values(ascending=False))
print('')
print('Top Strikeouts post-integration')
print(post_SO_Master_df.groupby(['playerID','nameLast','nameFirst'])['SO'].sum().sort_values(ascending=False)) 
































