# Digital-Marketing-Spend-Optimisation-Using-Linear-Programming
Contains a method for optimizing the marketing spending on different channels using google or tools

# It contains python script with streamlit app 

## Steps to run python script

1.  install streamlit 
[install streamlit](https://docs.streamlit.io/en/latest/troubleshooting/clean-install.html)

2.  streamlit run script.py

3.  You can see the output in the web browser

Format: 
![Alt Text](https://github.com/Abhishek-Gargha-Maheshwarappa/Digital-Marketing-Spend-Optimisation-Using-Linear-Programming/blob/master/Streamlit.JPG)

In any business, we would like to make unlimited profit/zero loss/unlimited utilization of resources but there are constraints like capacity constraints/budget constraints/production constraints/resource constraints because of which we cannot achieve them.

There are 3 characteristics of an optimization problem:

Decision Variables -The variables whose value is to be decided in order to achieve our objective
Objective Function – linear function of decision variables
Constraints – restrictions which cause hindrance in achieving the objective.
Linear programming is a simple technique to solve optimisation problems. In Lp, the business problem and constraints are all formulated as a linear function of the variables and hence the name linear programming.

Chief Marketing Officer(CMO) of a company asks the digital marketing manager to allocate an annual budget of 10,00,000 Rs among 4 channels: AdWords, Facebook, email and affiliated such that the number of users visits their website. Cost of acquisition per user from each channel will be 250,200,150 and 100 respectively. Lifetime value (LTV) of the customer from each channel will be 1500,800,300 and 100 respectively. CMO further says that he wants a minimum of 1000 users from each of Adwords and facebook channels and a minimum of 500 users from each email and affiliated. Budget for facebook and adwords together should not exceed 600000. LTV should be more than 500.

Adwords :: B1/250 >=1000
FB :: B2/200 >=1000
Email :: B3/150 >=500
Affiliated :: B4/100>=500
FB and Adwords Budget Constraint:: B1+B2<=600000
Total Budget Constraint :: B1+B2+B3+B4 <=1000000
LTV :: +4 Adword +1.5 Facebook -1.33333333333 Email -4 Affiliated >= 0;
Objective function : Maximize Number of Users = B1/250+B2/200+B3/10+B4/150
