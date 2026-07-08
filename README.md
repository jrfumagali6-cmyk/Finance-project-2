# Finance-project-2

Following my personal series on finance in Python, we have the second finance project. 
In this project, the main goal is technical analysis. So, in this project, I calculated the moving average (MA), which is very useful 
to find the right moments to buy and sell the tickers. Here, I have two types of MA: fast and slow. The fast MA tracks the ticker's price closely, while the slow MA has some lag. Normally, the cross between the fast and slow MAs determines the moment to buy or sell the ticker.

For example, consider VALE3.SA (image below): note the decreasing trend in the ticker's price. So, when does the intersection occur between the yellow line (Slow MA) and the blue line (Fast MA)? Since the yellow line is above the blue line, it indicates selling the ticker. In the opposite case, the blue line above the yellow line would indicate buying the ticker. 

And the green line ? Well, the green line in the chart represents the 25-period MA, but it's common to use a 200-period MA (many traders like this) to capture the long-term trend. This is a matter of taste; each trader can set the MA to their own preference. 

<img src="images/image.png" width="900">
