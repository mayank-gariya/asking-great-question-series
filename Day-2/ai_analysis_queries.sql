-- SQL Queries for AI Workforce Displacement Analysis

-- ==========================================
-- BASIC QUERIES
-- ==========================================

-- 1. List all unique industry sectors in the dataset.
SELECT DISTINCT industry_sector 
FROM ai_workforce_displacement;

-- 2. Find all records from the 'Technology & Software' sector in the 'High Income' group.
SELECT * FROM ai_workforce_displacement
WHERE industry_sector = 'Technology & Software' 
  AND income_group = 'High Income';

-- 3. Calculate the average AI adoption index across all countries.
SELECT AVG(ai_adoption_index) AS global_avg_ai_adoption 
FROM ai_workforce_displacement;

-- 4. Count the number of layoff announcements cited for each region.
SELECT region, SUM(ai_cited_layoff_announcements) AS total_layoffs
FROM ai_workforce_displacement
GROUP BY region;


-- ==========================================
-- INTERMEDIATE QUERIES
-- ==========================================

-- 1. Find the top 5 countries with the highest average net workforce change percentage for the year 2025.
SELECT country, AVG(net_workforce_change_pct) AS avg_net_change
FROM ai_workforce_displacement
WHERE year = 2025
GROUP BY country
ORDER BY avg_net_change DESC
LIMIT 5;

-- 2. Identify industries where the average automation risk is high (>0.6) and AI adoption is high (>0.7).
SELECT industry_sector, 
       AVG(sector_automation_risk_score) AS avg_risk, 
       AVG(ai_adoption_index) AS avg_adoption
FROM ai_workforce_displacement
GROUP BY industry_sector
HAVING AVG(sector_automation_risk_score) > 0.6 
   AND AVG(ai_adoption_index) > 0.7;

-- 3. Find the maximum GDP per capita for each region and income group.
SELECT region, income_group, MAX(gdp_per_capita_usd) AS max_gdp
FROM ai_workforce_displacement
GROUP BY region, income_group;

-- 4. Calculate total reskilling programs per region, filtering for those with a total > 5000.
SELECT region, SUM(reskilling_programs_count) AS total_reskilling
FROM ai_workforce_displacement
GROUP BY region
HAVING SUM(reskilling_programs_count) > 5000;


-- ==========================================
-- WINDOW FUNCTION QUERIES
-- ==========================================

-- 1. Rank countries within each region based on their AI tool adoption percentage for 2026.
SELECT region, country, ai_tool_adoption_pct,
       RANK() OVER(PARTITION BY region ORDER BY ai_tool_adoption_pct DESC) AS adoption_rank
FROM ai_workforce_displacement
WHERE year = 2026 AND quarter = 1;

-- 2. Calculate the running total of AI-cited layoff announcements for the United States.
SELECT year, quarter, ai_cited_layoff_announcements,
       SUM(ai_cited_layoff_announcements) OVER(ORDER BY year, quarter) AS running_total_layoffs
FROM ai_workforce_displacement
WHERE country = 'United States';

-- 3. Determine the previous quarter's displacement percentage (LAG) for 'Finance & Banking' in the UK.
SELECT year, quarter, pct_sector_workforce_displaced,
       LAG(pct_sector_workforce_displaced) OVER(ORDER BY year, quarter) AS prev_quarter_displacement
FROM ai_workforce_displacement
WHERE country = 'United Kingdom' AND industry_sector = 'Finance & Banking';

-- 4. Calculate a 4-period moving average of the net workforce change for India in Manufacturing.
SELECT year, quarter, net_workforce_change_pct,
       AVG(net_workforce_change_pct) OVER(ORDER BY year, quarter ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS moving_avg_change
FROM ai_workforce_displacement
WHERE country = 'India' AND industry_sector = 'Manufacturing & Industry';
