import pandas as pd
import os


# Change working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Current working directory:", os.getcwd())
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    

    # What is the average age of men?
    men_df = df[df['sex']== "Male"]
    average_age_men = men_df['age'].mean()
    average_age_men = round(average_age_men,1 )
    # What is the percentage of people who have a Bachelor's degree?
    deg_count = df['education'].value_counts()
    summ = sum(deg_count)
    bach = deg_count['Bachelors']
    
    percentage_bachelors = round(bach/summ*100 , 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    new = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])][['education', 'salary']]
    count = new['salary'].value_counts()

    higher_education = None
    lower_education = None
    
    low_ed = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])][['education', 'salary']]
    cnt  = low_ed['salary'].value_counts()

    # percentage with salary >50K
    higher_education_rich = round(count['>50K']/sum(count)*100,1)
    lower_education_rich = round(cnt['>50K']/sum(cnt)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    ddf =df[df['hours-per-week']==1][['hours-per-week','salary']]
    count = ddf['salary'].value_counts()
    num_min_workers =None

    rich_percentage =  round(count['>50K']/sum(count)*100,1)
    
    
    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).max() * 100
    highest_earning_country_percentage = round(highest_earning_country_percentage,1)
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

