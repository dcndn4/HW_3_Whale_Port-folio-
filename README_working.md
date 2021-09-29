#  Behind-the-Scenes: Whale Portfolio

Having been in theater when I was younger, I always found the activities behind the curtain as fun and interesting as the show itself.

And in life.

So to make the most progress possible, I'm going to write out my process in this space - exploring the topics, putting the info together in my own way. 

Here is the "Returns analysis example" text:

    Example - returns analysis (3.2 exercise)

    What are the average daily returns over each date range?
          1 Year = 0.04538 or 4.53%
          3 Year = 0.03455 or 3.45%
          5 Year = 0.02304 or 2.30%
          10 Year = 0.01488 or 1.49%

    What insights could this provide in regards to wanting to trade AMD stock in the long-term vs. short-term?

        The data shows that AMD had an average daily return over the last 1-year time frame of 0.004538, or 4.53%. This compares with long-term average daily returns of, for example, 3.45% for a 3 year horizon, and 1.49% for a 10 year horizon. By contrasting the short-run (1 year) trend against the long run trend (10 years), it’s apparent that AMD has had much stronger performance only recently.

        As to what this foretells for an investor looking to buy AMD stock now, however, is less clear: it’s possible that this 1-year performance signals a dramatic             change in AMD’s business model, and that this strong performance will continue. On the other hand, the most recent year’s could just be an anomaly, and that performance for AMD will revert to its long run trend.

         A third and entirely alternative explanation is that the equity market overall experienced a boom over this last year, and that AMD—like all stocks in the    market—rose in value. In the next unit, you will learn how to adjust for these market effects, so that you can evaluate stock performance from year-to-year on a more even measure.
  
  And so deconstructing those concepts:
  
 Returns over price changes -- returns are looked at instead of price changes because they are kind of boiled down to the informational nugget. Raw price itself can be very volatile, returns data moves over a much smaller range and each amount change is more meaningful.
        
Possible explanations for the improved performance over the last year are discussed - and they are very different. Returns data alone is not sufficient by itself - it needs to be seen within the context of the overall market. 
        
## Standard Deviation (std in pandas)
measures the distance between a set of values, and their center gravity basically (mathematically, by center gravity we mean average) (class mtls)
        
    from investopedia: measures the dispersion of a dataset relative to its mean (i.e. average). It is calculated as the square root of variance: each data point's deviation from the mean. The greater that distance, the greater the standard deviation. 
        
        Variance itself is an ingredient within standard deviation.. is usually not part of the analysis itself because it doesn't graph out in a way that is helpful 
        (investopedia). Also, variance may end up being in a different unit of measurement than the data itself, which adds to the confusion.
        
  ### benchmarks for std dev: 
  > volatile stocks have high standard deviation
  
  > 'blue chip' stocks tend to have lower standard deviation
  
  > index funds are built in such a way as to have low std dev in relation to their benchmark index - intended to replicate the results of the index.
  
  > std dev is widely reported for any stock or investment instrument, by analysts, portfolio managers and advisors (and investors). 
  
  > std dev can be compared to stocks/funds in a specific asset class or market sector. Mostly, those instruments would be expected to be similar - as they're  
  affected by overall market conditions similarly. Stocks/funds within that group with higher volatility have something else going on (investopedia video).
          
          ### std dev usefulness:
          is shown in the same unit of measurement as the underlying data, which helps make it understandable
          graphical results are clear and easy to discuss
          
          ### <u>Curve of std dev</u>:
          normal curve - then 68% of results fall w/n 1 std dev, or mean, data point. 
          shape with more volatility - fewer than 68% are within the 1 std dev, and more of the data points are outside of those bounds. 
          
         ### std dev downside: 
         the data that std dev is based on does not contain any info as to the reason for the deviation.. could be the company experiences positive growth. That would 
         be variance from the mean, so std dev is higher, so risk/reward are higher.. Kind of circuitious.. when reward is higher, risk is assumed to also be higher. 
         outliers and extreme values skew the shape of the curve, and may reduce the informational value of this calculation. When there are outliers, the normal 
         distribution isn't applicable, but there isn't a different model to use instead basically, so talking about the results is more difficult.
         Past results don't predict the future, of course.
         
         std dev was explored using python prior to pandas section, as pandas has built-in formula. It's included in investopedia of course.. not explored further 
         here. Input to the .std method in pandas is a DF with date-time column as index, and monetary values (close) as the one related column. (so is that a series? 
         or a dataframe still?)
                
        
        ## Primary relationship between standard deviation (1 vs. 2 etc..) and risk/reward. 
        
        1 std dev may equate to being in the group of 70% of the total population of values
        2 std dev for instance might be within 95% of total population of the group
        3 std dev = 100% basically
        bell curve
        little greek o symbol
        is denominator for Sharpe Ratio
        
        std dev applied to stock (morningstar classroom)
        
        A fund with std dev of 4, and average return (or mean) of 10%:
        most of the time (68%), the fund's future returns can be predicted to fall w/n 1 std dev of its historical average
          that translated to its average of 10%, plus or minus 4% -- so within 6% and 14%
        Nearly all the time (95%), the funds future returns should fall within 2 std dev's of mean:
           translated, that is 10% plus/minus 8%, or between 2% and 18%. 
           
         std dev is only helpful within context (morningstar again) - since std dev is not relative measure, so has to have a context built around it.
         That context generally comes from similar funds, (meaning funds with same defining features) and/or a relevant index. 
         For a single stock, context would come from other stockss from similar companies (market sector, size etc.). 
