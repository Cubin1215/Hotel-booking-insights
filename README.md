# Hotel Booking Insights 🏨

![Hotel Bookings](Query_Images/hotel-bookings.webp)

A comprehensive SQL-based business analytics project that explores hotel booking trends and provides valuable insights for hotel management and revenue optimization. This project uses the [Hotel Booking Demand Dataset](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand) from Kaggle.

## 📊 Project Overview

This project analyzes a hotel booking dataset to uncover patterns, trends, and insights that can help hotel managers make data-driven decisions. The analysis covers various aspects of hotel bookings including cancellation rates, revenue analysis, customer behavior, and booking patterns.

## 🛠️ Technical Implementation

The project is built using:
- **PostgreSQL** for database management
- **Python** for data loading and query execution
- **SQL** for data analysis and insights
- **Environment Variables** for secure database configuration

### Project Structure
```
hotel-booking-insights/
├── exploration.sql      # SQL queries for analysis
├── load_csv.py         # Data loading script
├── db_connect.py       # Database connection handler
├── run_query.py        # Query execution script
├── Query_Images/       # Visualization of query results
└── .env               # Database configuration (not tracked in git)
```


## 📈 Analysis Questions & Insights

### 1. Hotel Type Cancellation Analysis
**Question:** What's the cancellation rate for each hotel type?
![Query 1 Results](Query_Images/query%201.jpg)

**Results:**  
City hotels show a higher cancellation rate (approximately 41.73%) compared to Resort hotels (approximately 27.76%).

**Insights:**  
Understanding which hotel types experience higher cancellation rates helps in implementing targeted retention strategies. City hotels may need more aggressive retention policies.

### 2. Monthly Booking Trends
**Question:** Which months see the most bookings?
![Query 2 Results](Query_Images/query%202.jpg)

**Results:**  
August and July are the peak booking months, with significantly higher booking volumes compared to other months.

**Insights:**  
Identifying peak booking months helps in resource allocation and pricing strategy. Hotels should prepare for increased demand during summer months.

### 3. Country-wise Cancellation Analysis
**Question:** Which countries have the highest cancellation rates?
![Query 3 Results](Query_Images/query%203.jpg)

**Results:**  
Portugal (PRT) shows one of the highest cancellation rates among countries with significant booking volume. Here, ARE is excluded as the instances provided for it are less and does not give a perfect analysis.

**Insights:**  
Helps in understanding market-specific booking behaviors and implementing region-specific policies. May need to review booking policies for high-cancellation markets.

### 4. Distribution Channel Effectiveness
**Question:** Which distribution channels are most effective (least cancellations)?
![Query 4 Results](Query_Images/query%204.jpg)

**Results:**  
Corporate and Direct channels show lower cancellation rates compared to Online Travel Agents (OTA). GDS is excluded as its entries are less and doesn't give a perfect insight in relate to question.

**Insights:**  
Guides marketing budget allocation and channel optimization. Consider increasing focus on corporate and direct booking channels.

### 5. Lead Time Impact
**Question:** Does a longer lead time increase the likelihood of cancellation?
![Query 5 Results](Query_Images/query%205.jpg)

**Results:**  
Bookings made more than 6 months in advance show significantly higher cancellation rates.

**Insights:**  
Helps in understanding booking window patterns and optimizing cancellation policies. Consider implementing stricter policies for very early bookings.

### 6. Revenue Loss Analysis
**Question:** What's the revenue lost due to cancellations by hotel type?
![Query 6 Results](Query_Images/query%206.jpg)

**Results:**  
City hotels experience higher revenue loss from cancellations, with losses exceeding 5.8 million in the dataset period.

**Insights:**  
Quantifies the financial impact of cancellations and helps in revenue management. City hotels may need to implement stricter cancellation policies.

### 7. Room Upgrade Analysis
**Question:** Which reserved room types are most often upgraded?
![Query 7 Results](Query_Images/query%207.jpg)

**Results:**  
Room type A is most frequently upgraded, with specific patterns in upgrade destinations.

**Insights:**  
Helps in understanding room type preferences and optimizing room allocation. Can guide pricing strategy for different room types.

### 8. ADR Trend Analysis
**Question:** What's the ADR (Average Daily Rate) trend over time?
![Query 8 Results](Query_Images/query%208.jpg)

**Results:**  
ADR shows seasonal patterns with higher rates during summer months and lower rates during winter.

**Insights:**  
Tracks pricing trends and helps in revenue optimization. Can guide dynamic pricing strategies.

### 9. Guest Type Cancellation Analysis
**Question:** Do families or solo travelers cancel more often?
![Query 9 Results](Query_Images/query%209.jpg)

**Results:**  
Large families/groups show higher cancellation rates compared to families and couples.

**Insights:**  
Helps in understanding customer segment behavior and tailoring policies accordingly. May need different cancellation policies for different guest types.

### 10. Market Segment Revenue Analysis
**Question:** What's the average ADR by market segment?
![Query 10 Results](Query_Images/query%2010.jpg)

**Results:**  
Online TA and Offline TA/TO bookings show higher ADR compared to other segments.

**Insights:**  
Guides pricing strategy for different market segments. Can help in optimizing revenue by focusing on higher-value segments.

## 🎯 Business Impact

This analysis provides valuable insights for:
- Revenue Management
- Customer Retention
- Marketing Strategy
- Resource Allocation
- Pricing Optimization
- Market Segmentation

## 🔄 Running Queries

To run any analysis query:
```bash
python run_query.py <query_number>
```
Example: `python run_query.py 1` runs the hotel type cancellation analysis.

## 📝 Conclusion

This comprehensive analysis of hotel booking data reveals several critical insights for hotel management. The study shows that city hotels face higher cancellation rates and revenue loss compared to resort hotels, suggesting a need for different management strategies. Seasonal patterns are evident in both booking volumes and pricing, with summer months showing peak activity. The analysis of distribution channels indicates that corporate and direct bookings are more reliable, while online travel agents show higher cancellation rates. 

Customer behavior analysis reveals that solo travelers and early bookings (more than 6 months in advance) have higher cancellation rates, suggesting the need for targeted policies. The revenue analysis highlights significant financial impact from cancellations, particularly for city hotels. Market segment analysis shows that corporate and direct bookings command higher average daily rates, providing opportunities for revenue optimization.

These insights can guide hotels in:
1. Implementing targeted cancellation policies
2. Optimizing pricing strategies
3. Focusing on more reliable booking channels
4. Managing seasonal demand effectively
5. Developing segment-specific marketing strategies

The findings emphasize the importance of data-driven decision-making in hotel management and provide a foundation for improving operational efficiency and revenue optimization.

