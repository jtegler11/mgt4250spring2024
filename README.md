# mgt4250spring2024
Author: Jimmy Tegler (jtegler@elon.edu)
## Project Description
https://sportsbettingstatistics.streamlit.app/

This repository is my final project for MGT 4250 and is a dashboard of visualizations of various sports betting statistics created using streamlit.
### Questions of Interest
- Q1: What is the legal status of sports betting of each state in the United States?
- Q2: How much revenue has each state generated in the past year from sports betting?
- Q3: What is the estimated population of sports bettors in each state, and what markets or age groups are of interest?

  ### Important Statement
  These questions are *especially* **important** because
  1. Sports betting is a recent revelation in the United States, with New Jersey being the first state to legalize it in 2018, and it is up to the discretion of the state as to whether or not they would legalize sports betting. Following the passing of the Unlawful Internet Gambling Enforcement Act in 2006, which forbid online gambling, the door opened for fantasy sports betting as it was classified as a skill-based game and not a game of chance. In 2018, the Supreme Court struck down PASPA, which was passed in 1992 and outlawed sports gambling unless the state already had laws allowing it, which Nevada did(Bonesteel). Legalizing sporst betting guides consumers away from illegal markets, which in turn raises tax revenue for governments and states. This made states free to establish their own sports gambling laws, as the law was not consistent with the constitution. In 2018 the first states to legalize sports betting were Delaware, New Jersey, Rhode Island, Mississippi, West Virginia, New Mexico, Arkansas, and Pennsylvania allowed their citizens to place bets(Bonesteel). Since 2018, that number has been steadily rising as states are seeing the lucrative opportunity to generate revenue in their state through sports betting. In the following years, other states have followed suit in legalizing sports betting, which is why it is important to track what states have legalized, and which have not. 
  2. The online sports betting industry has boomed since its inception in 2018, and has garnered many customers from each state where it is legal. States collect taxes on gambling, so the more money people bet on sports, the more the state will collect(Lopez). Revenue from sports betting is breaking records every year outpacing all expectations set when it was legalized. Increased legalization, the addition of mobile gambling states, as well as the maturation of previously legal markets are the main drivers of high revenue numbers(Schafer). Gross revenue hit $7.5 billion in 2022, which is a 75% increase from 2021, and a number that is continuously on the rise(Schafer). With legalization up to 38 states as of 2023, the potential for growth is exponential. 
  3. In analyzing population statistics from the most recent U.S. census as well as researching sports betting participants among age group, I was able to estimate the amount of people who place bets among age groups for all states where betting is legalized and visualize it. Since sports betting is a recent phenomenon in the United States many people may not have been exposed to it yet, and this is a way to find target markets for sports betting apps to get more people involved and generate more revenue for their company. FanDuel and DraftKings are the two most dominant platforms on the market, where most people are placing bets(Bonesteel). The legalization of sports betting makes the average consumer feel safer when placing a bet, as opposed to offshore betting where consumers run the risk of losing deposited money and a lack of data privacy(Clement). Open markets are more enticing to prospective customers because legal markets don't face the same risks as illegal books. Legalization of sports betting is a new market which also creates more jobs for people. Also having mobile sports betting options is more convenient for the consumer as they won't have to travel to the casino to place their bet. 


                                                                  References
Bonesteel, Matt. “The History of Legal Sports Gambling in the U.S. - The Washington Post.” The Washington Post, 29 Aug. 2022, www.washingtonpost.com/sports/2022/08/29/history-of-sports-gambling/. 

Bureau, US Census. “Measuring America’s People, Places, and Economy.” Census.Gov, 30 Apr. 2024, www.census.gov/en.html. 
Clement, David, et al. “U.S Sports Betting Index.” Consumer Choice Center, 2021, consumerchoicecenter.org/wp-content/uploads/2022/07/US-Sports-Betting-Index.pdf. 

Feeney, Don. “National Detail Report National Survey On ...” National Council on Problem Gambling, 2021, www.ncpgsurvey.org/wp-content/uploads/2021/03/NCPG_NGAGE-Natl_Detailed_Report-Public.pdf. 

Lopez, German. “The Rise of Sports Betting.” The New York Times, The New York Times, 5 Apr. 2024, www.nytimes.com/2024/04/05/briefing/the-rise-of-sports-    betting.html#:~:text=The%20American%20Gaming%20Association%20says%20that%20sports%20betting,But%20advertising%20also%20convinces%20more%20people%20to%20gamble. 

Schafer, Josh. “Sports Betting Boom: Gross Revenue Hit $7.5 Billion in 2022, Shattering Record.” Yahoo! Finance, Yahoo!, finance.yahoo.com/news/sports-betting-boom-gross-revenue-record-2022-163013125.html. Accessed 8 May 2024. 



## Data Description
To access the data:

Navigate to the GitHub repository
Click on each file to view the contents
To download them, click "Download" or "Save As"
Make sure that you have an application capable of reading them such as Microsoft Excel

The first file, revenu2.xlsx columns: State(string), 2023 Total Handle(Billions)(float), 2023 Total Revenue(Millions)(float), Total Population(float), Age Groups(18-24,25-34, etc.), and Estimated # of Bettors Aged[Age Group].
  This file provides financial information used to create graphics

The next file demographics.xlsx contains the colunms: State(string), Total Population(float),  Age Groups(18-24,25-34, etc.), and Estimated # of Bettors Aged[Age Group], which are both float variables.
  This file gives me population numbers according to the U.S. census as well as groups them into various age groups.

The numberofbettors.xlsx file contains two columns: Age Groups(18-24,25-34, etc.) in a string and Percentage of Betting Participants, which are integers.
  This file contains the percentage of people within a certain age group that are placing bets.

The final file sports betting stats contains the following columns: State(string), Full Online, Retail Only, Bill Introduced, which are all string variables, as well as 2023 Total Revenue and 2023 Total Handle both of which are float variables:
  In this file I compiled each state's legal status regarding sports betting, as well as revenue and handle by state for the year 2023.
  



## Interpreting Visualizations
![image](https://github.com/jtegler11/mgt4250spring2024/assets/167884630/d7faaf84-a214-41f7-b6d1-39b0f1caf1b0)

## Discussions and Summary

```python
import pandas as pd
```
