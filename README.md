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
![Figure1-DataVis](https://github.com/jtegler11/mgt4250spring2024/assets/167884630/45f61816-0521-4c4c-aac4-77c9d15bc497)

Figure 1 is a map of the United States color coordinated to where each state stands regarding its legality of sports betting. Since it is up to the state whether or not they want to allow their population to place a bet, it is a useful graphic for people to figure out if they are able to place bets in their state, if a bill has been introduced to potentially allow sports betting, or the individual is not allowed to place a bet in that state. As of that graphic, 38 states have legalized sports betting, however some major states such as Texas and California currently do not allow sports betting. This figure helps to understand the geographical spread and regulatory landscape of sports betting, which is crucial for analyzing market potential. 

![Figure2-DataVis](https://github.com/jtegler11/mgt4250spring2024/assets/167884630/cd8f5bab-4d2f-45f3-9904-d7ce7a262a89)


Figure 2 shows how total handle and revenue for each state in 2023. Revenue in this case refers to how much money the sportsbooks made from each state, and handle refers to the total amount of money wagered on sports in that state. In this graphic, we get a breakdown, state-by-state, of how well they are performing since sports betting became legal. Then if a state is not performing as well, some sportsbooks may see that as an opportunity to increase marketing in that area to convince more people to sign up for their app and place bets.This is vital in addressing questions regarding economic implications of sports betting for states, and helps to identify which states are earning major revenue from sports betting. 

![Figure3-DataVis](https://github.com/jtegler11/mgt4250spring2024/assets/167884630/30e95b16-c418-4f3e-a56c-a5106f09103c)

Figure 3 takes population information from the most recent U.S. Census and plots populations broken down into specific age groups. The age groups are 18-24,25-34,35-44,45-54,55-64, and 65+. This gives the reader a general idea of the population of the United States and how it breaks down by age group. I used this figure in conjunction with figure 4 to help estimate the amount of bettors in the United States. Understanding demographic distribution aids in identifying potential market size for sports betting in different regions and age groups. We can pinpoint what age groups are being under represented in the betting market and could benefit from an effective marketing campaign.

![Figure4-DataVis](https://github.com/jtegler11/mgt4250spring2024/assets/167884630/6f2174c9-2c1e-430c-b4d0-5cb84ca9442f)

Figure 4 is an estimation of how many people are placing bets per state as well as broken down by age group. This figure provides useful insights into how many people are placing bets. Typically the younger generation is more likely to place bets, as evident in the figure as well as my next visualization. Sports apps such as FanDuel and DraftKings and states can utilize this data to infer what states and age groups are targets to increase their market share and improve performance. This visualization is key for quantigying the betting population and understanding demographic tendencies in gambling behaviors. It will help to identify untapped groups in the market and can help influence marketing and operational strategies.

![Figure5-DataVis](https://github.com/jtegler11/mgt4250spring2024/assets/167884630/59e724ee-e9fc-463e-b445-906887270aca)

Figure 5 is a representaion of the percentage of sports bettors by age group. People in age groups 18-24, and 25-34 are most likely to place bets, because sports betting is more popular among younger generations. This visualization was used along with figure 3 to help create figure 4, where I was able to estimate how many people in each state and each age group are placing bets. This can reveal age-related trends in sports betting, and help to assess the effectiveness of current marketing strategies and alter the development of promotional campaigns to increase participation among older age demographics.





## Discussions and Summary

https://www.fool.com/research/sports-betting-tax-revenue-by-state/#:~:text=Sports%20betting%20is%20now%20legal%20in%2038%20states,betting%20and%20where%20gamblers%20are%20wagering%20the%20most.

This article is an overall summary of sports betting in the United States. It states that since 2018 states have generated $4.33 billion in tax revenue from sports betting. New York has generated the most tax revenue from sports betting and it is currently legal in 38 states. It then details total tax revenue and gross sportsbook revenue of ecah state where it is legal, and includes a map of legalization of sports betting across the United States. The article then mentions that sports betting is here to stay, with the prevalence of advertisements and odds being discussed on sports media  every day, and it is hard to imagine it going anywhere with the amount of money being generated. $104 billion was wagered in 2023 according to the article, and sportsbook companies took home 9% of that, totaling $9.3 billion.  

ChatGPT Answer to the Questions:

Question 1: What is the legal status of sports betting of each state in the United States?

As of 2024, sports betting is legal and operational in various forms in 38 states plus Washington D.C., with different states allowing a mix of retail and online betting options. States like Arizona, Colorado, Illinois, and New Jersey offer both online and retail sports betting, while others like Mississippi and Montana only permit retail betting or on-premises mobile betting​.

Question 2: How much revenue has each state generated in the past year from sports betting?

The revenue generated from sports betting can vary significantly by state due to factors like population, the maturity of the sports betting market, and tax rates. For example, New York, with its high population and mobile betting options, is among the states generating significant revenue from sports betting. Detailed state-by-state revenue data would typically be found in specialized reports or databases from gaming associations or state regulatory bodies.

Question 3: What is the estimated population of sporst bettors in each state, and what markets or age groups are of interest?

Estimating the population of sports bettors in each state can be complex, as it depends on numerous factors including legal status, accessibility, and demographic interest in sports betting. Markets of particular interest often include young adults and frequent sports viewers. States with legal, accessible online betting platforms, such as New Jersey and Pennsylvania, likely see higher participation rates due to the ease of placing bets. For specific demographic data, surveys or studies from market research firms or analyses from sportsbooks could provide insights into the age groups and behaviors of bettors in each state​.

For detailed, up-to-date information on the legal status, revenue, and demographic analysis of sports bettors by state, consulting resources like the American Gaming Association or state-specific gaming boards would be beneficial.

Discussion 

My visualizations match what the article has detailed, we have similar maps, but differ in numbers because they've used total revenue since 2018, while I just looked at 2023. The maps are the most up to date visualizations of where sports betting is legal in the United States. However the trends are still similar, with the states who legalized first performing the best as well as bigger states such as New York perform extremely well. There is not concrete statistics on the total number of bettors per state, which is why I have estimated the number of bettors per state. 


References 


Bonesteel, Matt. “The History of Legal Sports Gambling in the U.S. - The Washington Post.” The Washington Post, 29 Aug. 2022, www.washingtonpost.com/sports/2022/08/29/history-of-sports-gambling/. 

Bureau, US Census. “Measuring America’s People, Places, and Economy.” Census.Gov, 30 Apr. 2024, www.census.gov/en.html. 

Clement, David, et al. “U.S Sports Betting Index.” Consumer Choice Center, 2021, consumerchoicecenter.org/wp-content/uploads/2022/07/US-Sports-Betting-Index.pdf. 

Dellafave, Robert. “US Sports Betting Map 2024 - Where You Can Play.” USBets, 8 May 2024, www.usbets.com/sports-betting/. 

Feeney, Don. “National Detail Report National Survey On ...” National Council on Problem Gambling, 2021, www.ncpgsurvey.org/wp-content/uploads/2021/03/NCPG_NGAGE-Natl_Detailed_Report-Public.pdf. 

James, Brant. “States with Legal Sports Betting in 2024 - Legislation Tracker.” Gaming Today, 2024, www.gamingtoday.com/states/. 


Lopez, German. “The Rise of Sports Betting.” The New York Times, The New York Times, 5 Apr. 2024, www.nytimes.com/2024/04/05/briefing/the-rise-of-sports-betting.html#:~:text=The%20American%20Gaming%20Association%20says%20that%20sports%20betting,But%20advertising%20also%20convinces%20more%20people%20to%20gamble. 

Oddspedia. “U.S Sports Betting Revenue and Handle Tracker.” Oddspedia, 2024, oddspedia.com/us/betting/sports-betting-revenue. 


Schafer, Josh. “Sports Betting Boom: Gross Revenue Hit $7.5 Billion in 2022, Shattering Record.” Yahoo! Finance, Yahoo!, finance.yahoo.com/news/sports-betting-boom-gross-revenue-record-2022-163013125.html. Accessed 8 May 2024.  


