-- Customer Funnel Analysis
-- Database: data/raw/funnel.db
-- Goal: Analyze user journey from visit to purchase

-- 1. Check tables exist
SELECT name
FROM sqlite_master
WHERE type = 'table';

-- 2. Funnel stage counts (unique users)

SELECT 'Visit' AS stage, COUNT(DISTINCT user_id) AS users
FROM events
WHERE event_type = 'visit'

UNION ALL

SELECT 'Signup' AS stage, COUNT(DISTINCT user_id) AS users
FROM events
WHERE event_type = 'signup'

UNION ALL

SELECT 'Add to Cart' AS stage, COUNT(DISTINCT user_id) AS users
FROM events
WHERE event_type = 'add_to_cart'

UNION ALL

SELECT 'Purchase' AS stage, COUNT(DISTINCT user_id) AS users
FROM transactions;

