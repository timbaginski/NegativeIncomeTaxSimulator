# NegativeIncomeTaxSimulator
<h1>Sources</h1>
Income percentiles: https://dqydj.com/income-percentile-calculator/ <br></br>
Number of workers in the US: https://www.statista.com/statistics/193953/seasonally-adjusted-monthly-civilian-labor-force-in-the-us/ <br></br>
Number of adults in the US: https://www.census.gov/library/stories/2021/08/united-states-adult-population-grew-faster-than-nations-total-population-from-2010-to-2020.html <br></br>
Number of retired adults in the US: https://www.statista.com/statistics/194295/number-of-us-retired-workers-who-receive-social-security/#:~:text=Number%20of%20retired%20workers%20receiving%20Social%20Security%20in%20the%20U.S.%202010%2D2020&text=The%20number%20of%20retired%20workers,to%2046.33%20million%20in%202020. <br></br>
Tax rates: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets <br></br>

<h1>Basic Info</h1>
This code intends to estimate the costs of a negative income tax (NIT) if implemented in the United States. The program is written in Python3 and uses pandas for the data analysis. <br></br>

<h1>About the Negative Income Tax</h1>
The NIT is a welfare program which can be used to guarantee income. Unlike a Universal basic income, the payments phase out as income increases, so a greater poverty reduction is achieved with a smaller total cost. Unlike means-tested welfare, recipients do not face a "welfare cliff" in which increasing their earnings can sometimes lower their income <br></br>
The NIT can be implemented using two parameters: a threshold and a percentage. Under the NIT, each individual which makes an income lower than the threshold would recieve payments. The NIT works by first substracting the recipients income from the threshold, and then multiplying this result by the percentage. <br></br>As an example, If an NIT program had a threshold of $40,000 and a percent of 50, an individual making $30,000 would recieve $5,000, equal to ($40,000 - $30,000) * 0.5. An individual making $0, would recieve ($40,000 - $0) * 0.5, or $20,000. 

<h1>Algorithms Used</h1>
The first algorithm uses the data to estimate the percentage of individuals at or below a given income level. This algorithm first figures out the two percentiles (and the corresponding incomes) from the data set the given income lies between. If v represents the difference between the higher and lower percentiles, w represents the lower of the two percentiles, x represents the given income, y represents the income associated with the lower percentile, z represents the income associated with the higher percentile, the income percentile of an individual can be estimated with:<br></br>

P = w + v * (x - y) / (z - y) <br></br>

The second algorithm takes a threshold and a percent (which is converted to a decimal) in order to approximate the total cost of implementing a given NIT scheme. It does this by totalling the approximate cost for each income group from $0 to the dollar amount denoted by the threshold (the width of each group being $100). For each income group, it estimates the number of individuals which belong to the group, and uses the threshold and percentage formula mentioned above to find the total cost for that income group. It adds this result to the total, and returns the total after it is done iterating. <br></br>

Finally, the program estimates the amount each individual saves on taxes in order to represent the full cost of the NIT. Under a NIT, the marginal tax rate under the threshold is zero. In order to factor this in, the program uses data on income tax brackets and then determines if the given income group makes more or less than the threshold. If the individual makes less than the threshold, it means they pay zero federal income tax: The program iterates through each income tax bracket and adds the smaller value between the ceiling for that tax bracket and the amount of income the individual has over that tax bracket multiplied by the tax rate to the total. If they have no income left over the tax bracket, it means the algorithm is finished, and the total is returned. In the event the individual makes more than the threshold, the same algorithm is used, only swapping the individuals income for the threshold. 
