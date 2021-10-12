import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count  =df.race.value_counts()

    # What is the average age of men?
    average_age_men = round((df[df['sex']=='Male'].age.mean()),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((((df[df['education']=='Bachelors'].education.count())/len(df))*100),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    m=((df['education']=='Bachelors')|(df['education']=='Doctorate')|(df['education']=='Masters'))&(df.salary=='>50K')
    
    m1=((df['education']=='Bachelors')|(df['education']=='Doctorate')|(df['education']=='Masters'))


    n=~((df['education']=='Bachelors')|(df['education']=='Doctorate')|(df['education']=='Masters'))&(df.salary=='>50K')
    
    n1=~((df['education']=='Bachelors')|(df['education']=='Doctorate')|(df['education']=='Masters'))
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    
    higher_education_rich =round((df[m].salary.count()/df[m1].salary.count()*100),1)
    lower_education_rich = round((df[n].salary.count()/df[n1].salary.count()*100),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers =df[m].salary.count()
    m=(df['hours-per-week']==1)
    n=(df['hours-per-week']==1)&(df['salary']=='>50K')
    rich_percentage =round((df[n].salary.count()/df[m].salary.count()*100),1)


    # What country has the highest percentage of people that earn >50K?
    s=df[df.salary=='>50K']['native-country'].value_counts()
    q= (s.index)
    dt={}
    for j in q:

        p=(df['native-country']==j)&(df['salary']=='<=50K')
        p1=df[p].salary.count()

        r=(df['native-country']==j)&(~(df['salary']=='<=50K'))
        r1=df[r].salary.count()

        v=(r1/(r1+p1))*100
        dt[j]=v


    d=max(zip(dt.values(),dt.keys()))
    
    highest_earning_country = d[1]
    highest_earning_country_percentage = round((d[0]),1)

    # Identify the most popular occupation for those who earn >50K in India.
    m=(df['native-country']=='India')&(df['salary']=='>50K')
    v=df[m].occupation.value_counts()
    top_IN_occupation = v.index[0]

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
