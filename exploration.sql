-- =============================================
-- Question 1: What's the cancellation rate for each hotel type?
-- =============================================

-- View first few rows of the data
SELECT 
    hotel as hotel_type, 
    sum(is_canceled) as cancellations,
    count(*) as total_bookings,
    ROUND((SUM(is_canceled) * 100.0) / COUNT(*), 2) as cancellation_rate
    FROM hotel_bookings
    GROUP BY hotel
    ORDER BY cancellation_rate DESC; 


-- =============================================
-- Question 2: Which months see the most bookings?
-- =============================================

-- Count of bookings by hotel type
SELECT 
    arrival_date_month as month,
    COUNT(*) AS total_bookings
    FROM hotel_bookings
    GROUP BY arrival_date_month
    ORDER BY total_bookings DESC;

-- =============================================
-- Question 3: Which countries have the highest cancellation rates?
-- =============================================

-- Monthly booking trends
SELECT 
    arrival_date_month,
    COUNT(*) as monthly_bookings
FROM hotel_bookings
GROUP BY arrival_date_month
ORDER BY 
    CASE arrival_date_month
        WHEN 'January' THEN 1
        WHEN 'February' THEN 2
        WHEN 'March' THEN 3
        WHEN 'April' THEN 4
        WHEN 'May' THEN 5
        WHEN 'June' THEN 6
        WHEN 'July' THEN 7
        WHEN 'August' THEN 8
        WHEN 'September' THEN 9
        WHEN 'October' THEN 10
        WHEN 'November' THEN 11
        WHEN 'December' THEN 12
    END;

-- =============================================
-- SECTION 4: Revenue Analysis
-- =============================================

-- Average daily rate by hotel
SELECT 
    hotel,
    ROUND(AVG(adr), 2) as avg_daily_rate,
    MIN(adr) as min_rate,
    MAX(adr) as max_rate
FROM hotel_bookings
GROUP BY hotel
ORDER BY avg_daily_rate DESC;