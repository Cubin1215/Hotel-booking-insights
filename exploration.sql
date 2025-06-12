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
-- Question 6: What's the revenue lost due to cancellations by hotel type?
-- =============================================

SELECT 
    hotel,
    TO_CHAR(SUM(CASE WHEN is_canceled = 1 THEN adr * (stays_in_week_nights + stays_in_weekend_nights) ELSE 0 END), 'FM999,999,999,999.99') as revenue_lost
    FROM hotel_bookings
    GROUP BY hotel;

-- =============================================
-- Question 7: Which reserved room types are most often upgraded?
-- =============================================

SELECT 
    reserved_room_type,
    assigned_room_type,
    COUNT(*) as upgrade_count
    FROM hotel_bookings
    WHERE assigned_room_type != reserved_room_type
    GROUP BY reserved_room_type, assigned_room_type
    ORDER BY upgrade_count DESC
    LIMIT 10;

-- =============================================
-- Question 8: What’s the ADR trend over time? (Year + Month)
-- =============================================

SELECT 
    arrival_date_year,
    arrival_date_month,
    TO_DATE(arrival_date_year || '-' || TRIM(arrival_date_month) || '-01', 'YYYY-Month-DD') AS full_date,
    ROUND(AVG(adr), 2) as avg_adr
    FROM hotel_bookings
    GROUP BY arrival_date_year, arrival_date_month
    ORDER BY full_date
    LIMIT 10;


-- =============================================
-- Question 9: Do families or solo travelers cancel more often?
-- =============================================

SELECT 
    CASE WHEN COALESCE(NULLIF(children, '')::FLOAT, 0)  + CAST(adults AS FLOAT) + CAST(babies AS FLOAT) = 1 THEN 'SOLO'
    WHEN COALESCE(NULLIF(children, '')::FLOAT, 0)  + CAST(adults AS FLOAT) + CAST(babies AS FLOAT) IN (2, 3) THEN 'COUPLE/SMALL FAMILY'
    ELSE 'LARGE FAMILY/GROUP'
    END AS guest_type,
    sum(is_canceled) as cancellations,
    count(*) as total_bookings,
    ROUND((SUM(is_canceled) * 100.0) / COUNT(*), 2) as cancellation_rate
    FROM hotel_bookings
    GROUP BY guest_type
    ORDER BY cancellation_rate DESC;

-- =============================================
-- Question 10: What’s the average ADR by market segment?
-- =============================================

SELECT 
    market_segment,
    TO_CHAR(SUM(adr * stays_in_weekend_nights + adr * stays_in_week_nights), 'FM999,999,999.00') AS total_revenue
FROM hotel_bookings
GROUP BY market_segment
ORDER BY SUM(adr * stays_in_weekend_nights + adr * stays_in_week_nights) DESC;

