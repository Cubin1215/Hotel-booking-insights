-- =============================================
-- Question 1: What's the cancellation rate for each hotel type?
-- =============================================

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

SELECT 
    arrival_date_month as month,
    COUNT(*) AS total_bookings
    FROM hotel_bookings
    GROUP BY arrival_date_month
    ORDER BY total_bookings DESC;

-- =============================================
-- Question 3: Which countries have the highest cancellation rates?
-- =============================================

SELECT 
    country,
    sum(is_canceled) as cancellations,
    count(*) as total_bookings,
    ROUND((SUM(is_canceled) * 100.0) / COUNT(*), 2) as cancellation_rate
    FROM hotel_bookings
    GROUP BY country
    HAVING COUNT(*) > 50
    ORDER BY cancellation_rate DESC
    LIMIT 10;

-- =============================================
-- Question 4: Which distribution channels are most effective (least cancellations)?
-- =============================================

SELECT 
    distribution_channel,
    sum(is_canceled) as cancellations,
    count(*) as total_bookings,
    ROUND((SUM(is_canceled) * 100.0) / COUNT(*), 2) as cancellation_rate
    FROM hotel_bookings
    GROUP BY distribution_channel
    ORDER BY cancellation_rate ASC;

-- =============================================
-- Question 5: Does a longer lead time increase the likelihood of cancellation? 
-- =============================================

SELECT 
    width_bucket(lead_time, 0, 740, 10) AS lead_time_bin,
    sum(is_canceled) as cancellations,
    count(*) as total_bookings,
    ROUND((SUM(is_canceled) * 100.0) / COUNT(*), 2) as cancellation_rate
    FROM hotel_bookings
    GROUP BY lead_time_bin
    ORDER BY lead_time_bin DESC;

-- =============================================
-- Question 6: What’s the revenue lost due to cancellations by hotel type?
-- =============================================

SELECT 
    width_bucket(lead_time, 0, 740, 10) AS lead_time_bin,
    sum(is_canceled) as cancellations,
    count(*) as total_bookings,
    ROUND((SUM(is_canceled) * 100.0) / COUNT(*), 2) as cancellation_rate
    FROM hotel_bookings
    GROUP BY lead_time_bin
    ORDER BY lead_time_bin DESC;