SELECT 
    COUNT(transaction_id) AS total_transactions,
    SUM(revenue_gbp) AS total_revenue,
    AVG(revenue_gbp) AS average_order_value,
    MIN(revenue_gbp) AS smallest_purchase,
    MAX(revenue_gbp) AS largest_purchase
FROM transactions;