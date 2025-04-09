# Data Cleaning Project

select *
from layoffs;

# 1 -- Remove duplicates
# 2 -- standardise the data
# 3 -- null values or blank values
# 4 -- remove any unnecessary columns/rows -- be careful!!

# create a new table without affecting the raw dataset
create table layoffs_staging
like layoffs;

select *
from layoffs_staging;

insert into layoffs_staging
select *
from layoffs;

#-----------------------------------------------------------------------------------------------
# 1 -- Removing Duplicates

# creating a column that counts duplicates
select *,
row_number() over(
partition by company, location, industry, total_laid_off, percentage_laid_off, `date`,
stage, country, funds_raised_millions) as row_num
from layoffs_staging;

# creating a CTE for it
with duplicate_cte as
(
select *,
row_number() over(
partition by company, location, industry, total_laid_off, percentage_laid_off, `date`,
stage, country, funds_raised_millions) as row_num
from layoffs_staging
)
select *
from duplicate_cte
where row_num >1;

# checking companies
select *
from layoffs_staging 
where company = "Casper";

# creating a new table to delete duplicates
CREATE TABLE `layoffs_staging_duplicates` (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` int DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` int
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

select *
from layoffs_staging_duplicates;

# inserting only the duplicates into the table
insert into layoffs_staging_duplicates
select *,
row_number() over(
partition by company, location, industry, total_laid_off, percentage_laid_off, `date`,
stage, country, funds_raised_millions) as row_num
from layoffs_staging;

# deleting the duplicates -- only keeping 1 instance
delete
from layoffs_staging_duplicates
where row_num > 1;

#-----------------------------------------------------------------------------------------------
# 2 -- Standardising data

# getting rid of whitespace
select company, trim(company)
from layoffs_staging_duplicates;

# updating it
update layoffs_staging_duplicates
set company = trim(company);

# checking industry
select distinct industry
from layoffs_staging_duplicates;

# Crypto v/s CryptoCurrency
select *
from layoffs_staging_duplicates
where industry like "Crypto%";

# updating it
update layoffs_staging_duplicates
set industry = "Crypto"
where industry like "Crypto%";

# checking countries
select distinct country
from layoffs_staging_duplicates
order by 1;

# US had a . at the end
select distinct country, trim(trailing "." from country)
from layoffs_staging_duplicates
order by 1;

# removing it
update layoffs_staging_duplicates
set country = trim(trailing "." from country)
where country like "United States%";

select * from layoffs_staging_duplicates;

# date is given as text
describe layoffs_staging_duplicates;

# changing date to date 
select `date`,
str_to_date(`date`, "%m/%d/%Y")
from layoffs_staging_duplicates;

update layoffs_staging_duplicates
set `date` = str_to_date(`date`, "%m/%d/%Y");

alter table layoffs_staging_duplicates
modify column `date` date;

#-----------------------------------------------------------------------------------------------
# Working with Nulls or Blank

# setting null to blank
update layoffs_staging_duplicates
set industry = null
where industry = "";

# getting the nulls and blanks
select *
from layoffs_staging_duplicates
where industry is null
or industry = "";

select * from layoffs_staging_duplicates
where company like "Bally%";

# self join to check for industry if multiple occurances
select t1.industry, t2.industry
from layoffs_staging_duplicates t1
join layoffs_staging_duplicates t2
	on t1.company = t2.company
    and t1.location = t2.location
where (t1.industry is null or t1.industry = "")
and (t2.industry is not null or t2.industry = "");

# updating industry if it is known for another instance
update layoffs_staging_duplicates t1
join layoffs_staging_duplicates t2
	on t1.company = t2.company
set t1.industry = t2.industry
where t1.industry is null
and t2.industry is not null;

select industry from layoffs_staging_duplicates;

select * from layoffs_staging_duplicates;

# total & percentage laid off being null doesn't seem too useful
select *
from layoffs_staging_duplicates
where total_laid_off is null
and percentage_laid_off is null;

# deleting it
delete 
from layoffs_staging_duplicates
where total_laid_off is null
and percentage_laid_off is null;

# dropping the new column made
alter table layoffs_staging_duplicates
drop column row_num;

select * from layoffs_staging_duplicates;