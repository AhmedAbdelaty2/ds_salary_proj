import glassdoor_scraper as gs
import pandas as pd


path = "C:/Users/hp/Documents/ds_salary_proj/chromedriver"
df = gs.get_jobs('data science', 15, False, path, 15)
