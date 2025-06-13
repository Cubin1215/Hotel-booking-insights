# Hotel Booking Insights 🏨

A comprehensive SQL-based business analytics project that explores hotel booking trends and provides valuable insights for hotel management and revenue optimization.

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

### Setup Instructions

1. Clone the repository
2. Install required Python packages:
   ```bash
   pip install pandas psycopg2-binary python-dotenv tabulate
   ```
3. Create a `.env` file with your database credentials:
   ```
   DB_PASSWORD=your_password_here
   DB_USER=postgres
   DB_NAME=hotel_booking
   DB_HOST=localhost
   DB_PORT=5432
   ```
4. Load the data:
   ```bash
   python load_csv.py
   ```

## 📈 Analysis Questions & Insights

### 1. Hotel Type Cancellation Analysis
**Question:** What's the cancellation rate for each hotel type?
![Query 1 Results](Query_Images/query%201.jpg)
*Insight: Understanding which hotel types experience higher cancellation rates helps in implementing targeted retention strategies.*

### 2. Monthly Booking Trends
**Question:** Which months see the most bookings?
![Query 2 Results](Query_Images/query%202.jpg)
*Insight: Identifying peak booking months helps in resource allocation and pricing strategy.*

### 3. Country-wise Cancellation Analysis
**Question:** Which countries have the highest cancellation rates?
![Query 3 Results](Query_Images/query%203.jpg)
*Insight: Helps in understanding market-specific booking behaviors and implementing region-specific policies.*

### 4. Distribution Channel Effectiveness
**Question:** Which distribution channels are most effective (least cancellations)?
![Query 4 Results](Query_Images/query%204.jpg)
*Insight: Guides marketing budget allocation and channel optimization.*

### 5. Lead Time Impact
**Question:** Does a longer lead time increase the likelihood of cancellation?
![Query 5 Results](Query_Images/query%205.jpg)
*Insight: Helps in understanding booking window patterns and optimizing cancellation policies.*

### 6. Revenue Loss Analysis
**Question:** What's the revenue lost due to cancellations by hotel type?
![Query 6 Results](Query_Images/query%206.jpg)
*Insight: Quantifies the financial impact of cancellations and helps in revenue management.*

### 7. Room Upgrade Analysis
**Question:** Which reserved room types are most often upgraded?
![Query 7 Results](Query_Images/query%207.jpg)
*Insight: Helps in understanding room type preferences and optimizing room allocation.*

### 8. ADR Trend Analysis
**Question:** What's the ADR (Average Daily Rate) trend over time?
![Query 8 Results](Query_Images/query%208.jpg)
*Insight: Tracks pricing trends and helps in revenue optimization.*

### 9. Guest Type Cancellation Analysis
**Question:** Do families or solo travelers cancel more often?
![Query 9 Results](Query_Images/query%209.jpg)
*Insight: Helps in understanding customer segment behavior and tailoring policies accordingly.*

### 10. Market Segment Revenue Analysis
**Question:** What's the average ADR by market segment?
![Query 10 Results](Query_Images/query%2010.jpg)
*Insight: Guides pricing strategy for different market segments.*

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

## 🤝 Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a feature branch
3. Submitting a pull request

## 📝 License

This project is open source and available under the MIT License.

