select * from layoffs_staging_duplicates;

# checking maximum for toatal and percentage laid off
select max(total_laid_off), max(percentage_laid_off)
from layoffs_staging_duplicates;

# looking at 100% laid offs -- ordering by total laid off
select *
from layoffs_staging_duplicates
where percentage_laid_off = 1
order by total_laid_off desc;

# looking at funds raised by those companies
select *
from layoffs_staging_duplicates
where percentage_laid_off = 1
order by funds_raised_millions desc;

# looking at which companies had the most lay offs
select company, sum(total_laid_off)
from layoffs_staging_duplicates
group by company
# ordering by 2nd column
order by 2 desc;

# checking the time range -- 3 years
select min(`date`), max(`date`)
from layoffs_staging_duplicates;

# looking at which industry had the most lay offs
select industry, sum(total_laid_off)
from layoffs_staging_duplicates
group by industry
# ordering by 2nd column
order by 2 desc;

# looking at which countries had the most lay offs
select country, sum(total_laid_off)
from layoffs_staging_duplicates
group by country
# ordering by 2nd column
order by 2 desc;

# layoffs per year
select year(`date`), sum(total_laid_off)
from layoffs_staging_duplicates
group by year(`date`)
# ordering by 2nd column
order by 1 desc;

# looking at what stage the companies were in
select stage, sum(total_laid_off)
from layoffs_staging_duplicates
group by stage
# ordering by 2nd column
order by 2 desc;

# didn't find percentage_laid_off too useful to use
select company, sum(percentage_laid_off)
from layoffs_staging_duplicates
group by company
# ordering by 2nd column
order by 2 desc;

# getting the year and month of total lay offs, ordering by the months
select substring(`date`, 1, 7) as `month`, sum(total_laid_off)
from layoffs_staging_duplicates
where substring(`date`, 1,7) is not null
group by `month`
order by 1;

# rolling total of total laid off
with Rolling_Total as
(
select substring(`date`, 1, 7) as `month`, sum(total_laid_off) total_off
from layoffs_staging_duplicates
where substring(`date`, 1,7) is not null
group by `month`
order by 1
)
select `month`, total_off,
sum(total_off) over(order by `month`) as rolling_total
from Rolling_Total;

# looking at companies with most layoffs for each years
select company, year(`date`), sum(total_laid_off)
from layoffs_staging_duplicates
group by company, year(`date`)
order by 3 desc;

# 1st CTE -- getting the total laid off for each company for the year
with Company_Year(company, years, total_laid_off) as
(
select company, year(`date`), sum(total_laid_off)
from layoffs_staging_duplicates
group by company, year(`date`)
),

# 2nd CTE -- giving each company a ranking based on how many laid off for the year
Company_Year_Rank as
(
select *, dense_rank() over (partition by years order by total_laid_off desc) as Ranking
from Company_Year
where years is not null
)
# getting the top 5 companies only -- will show ties because of dense_rank
select *
from Company_Year_Rank
where Ranking <= 5;