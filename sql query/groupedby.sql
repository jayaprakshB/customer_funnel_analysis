SELECT 
    user_id,
    COUNT(transaction_id) AS order_count,
    SUM(revenue_gbp) AS total_spent_gbp
FROM transactions
GROUP BY user_id
ORDER BY total_spent_gbp DESC;