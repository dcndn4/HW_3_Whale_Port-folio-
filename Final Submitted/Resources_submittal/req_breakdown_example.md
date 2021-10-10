# Homework 4: Pandas

Use **Jupyter Lab** to:

1. Read & clean csv data, given the portfolios' returns
2. Calc each Portfolio's performance
3. Choose and Evaluate a Custom Portfolio

Calc **volatility, returns, risk, Sharpe**

Which portfolio is best?

Given that, create a custom portfolio of stocks and compare its performance to others, as well as the larger market ([S&P 500 Index](https://en.wikipedia.org/wiki/S%26P/TSX_60)).

## Instructions

**File:** [Whale Analysis Starter Code](Starter_Code/whale_analysis.ipynb)


### Prepare the Data

Read, clean the CSV files. Use the [Whale Analysis Starter Code](Starter_Code/whale_analysis.ipynb) to do the following:

1. Read the CSV files as a df. Convert dates to a `DateTimeIndex`.

    * `whale_returns.csv`

    * `algo_returns.csv`

    * `sp500_history.csv`

2. Remove nulls.

3. Remove dollar signs, etc, and convert the data types as needed.

4. The S&P 500 CSV file contains closing prices. Convert the closing prices to daily returns.

5. Join all three dfs

    ![returns-dataframe.png](Images/returns-dataframe.png)

### Conduct Quantitative Analysis

Analyze the data to see if any of the portfolios outperform the stock market (S&P 500).

#### Performance Analysis

1. All portfolios: Calculate and plot daily returns.

2. All portfolios: Calculate and plot cumulative returns. Which outperform S&P 500?

#### Risk Analysis

1. Create a box plot for each of the returns. 

2. Each portfolio: Calculate the standard deviation.

3. Which portfolios are riskier than the S&P 500?

4. Calculate the Annualized Standard Deviation.

#### Rolling Statistics

1. Calculate and plot the rolling standard deviation for using a 21-day window.

2. Calculate and plot the correlation between each stock to determine which portfolios mimick the S&P 500.

3. Choose one portfolio, then calculate and plot the 60-day rolling beta between it and the S&P 500.

#### Rolling Statistics Challenge: Exponentially Weighted Average

An alternative method to calculate a rolling window is to take the **exponentially weighted moving average** (moving window average), but it assigns greater importance to more recent observations. Calculate the [`ewm`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html) with a 21-day half-life.

### Sharpe Ratios

If you have two portfolios that each offer a 10% return, yet one is lower risk, you would invest in the lower-risk portfolio, right? So Sharpe ratio.

1. Using the daily returns, calculate and visualize the Sharpe ratios using a bar plot.

2. Determine whether the algorithmic strategies outperform both the market (S&P 500) and other portfolios.

### Create a Custom Portfolio

Can you choose your own portfolio that performs just as well as the others?

1. Visit [Google Sheets](https://docs.google.com/spreadsheets/) and use the built-in Google Finance function to choose 3-5 stocks for your portfolio.

2. Download the data as CSV files and calculate the portfolio returns.

3. Calculate the weighted returns for your portfolio, assuming equal number of shares per stock.

4. Add your portfolio returns to the DataFrame with the other portfolios.

5. Run the following analyses:

    * Calculate the Annualized Standard Deviation.
    * Calculate and plot rolling `std` with a 21-day window.
    * Calculate and plot the correlation.
    * Calculate and plot beta for your portfolio compared to the S&P 60 TSX.
    * Calculate the Sharpe ratios and generate a bar plot.

4. How does your portfolio do?

## Hints

* After reading each CSV file, don't forget to sort each DataFrame in ascending order by the Date using `sort_index`. This is especially important when working with time series data, as we want to make sure Date indexes go from earliest to latest.

* The Pandas functions used in class this week will be useful for this assignment.

* Be sure to use `head()` or `tail()` when you want to look at your data, but don't want to print to a large DataFrame.


## Submission

1. Use the provided starter Jupyter Notebook to house the code for your data preparation, analysis, and visualizations. Put any analysis or answers to assignment questions in raw text (markdown) cells in the report.

