import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'Project/chicago.csv',
              'new york city': 'Project/new_york_city.csv',
              'washington': 'Project/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get desired city for evaluation
    cities = ['Chicago', 'New York City', 'Washington']
    print("Please choose a City:")
    for i, city in enumerate(cities, 1):
        print(f"{i}: {city}")
    # Test for valid input
    while True:
        try:
            choice = int(input("Choose a number: "))
            if 1 <= choice <= len(cities):
                chosen_City = cities[choice - 1].lower()
                break
            else:
                print("Invalid number, please choose a valid city number.")
        except ValueError:
            print("Please enter a valid number.")
    city = chosen_City.lower()
    # get desired months
    while True:
        try:
            choice = input("Please enter a specific month or leave empty: ").lower()
            if choice == '':
                month = 'all'
                break
            elif choice in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                month = choice
                break
            else:
                print("Invalid month, please choose a valid month.")
        except ValueError:
            print("Please enter a valid month.")
    # get desired day of week
    while True:
        try:
            choice = input("Please enter a weekday or leave empty: ").lower()
            if choice == '':
                day = 'all'
                break
            elif choice in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                day = choice
                break
            else:
                print("Invalid month, please choose a valid month.")
        except ValueError:
            print("Please enter a valid month.")

    print('\n')
    print('-'*80)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # read general DataFrame
    df = pd.read_csv(CITY_DATA[city])
    # splitting time information
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    # filter by month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month_idx =  months.index(month) + 1
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_idx =  months.index(month) + 1
        df = df[df['month'] == month_idx]
    # filter by day
    if day != 'all':
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day_idx = days.index(day)
        df = df[df['day_of_week'] == day_idx]
    if day == 'all' and month == 'all':
        print(f"\nLet's look at the data for {city.title()} in all months and all days.")
    elif day == 'all' and month != 'all':
        print(f"\nLet's look at the data for {city.title()} in month {month.title()} and all days.")
    elif day != 'all' and month == 'all':
        print(f"\nLet's look at the data for {city.title()} in all months and at {day.title()}.")
    print('\n'+'-'*80)
    return df


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel:\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month_idx = df['month'].mode()[0]
    popular_month = months[popular_month_idx - 1]
    print(f"The most popular month is {popular_month.capitalize()}.")

    # TO DO: display the most common day of week
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    popular_day_idx = df['day_of_week'].mode()[0]
    popular_day = days[popular_day_idx]
    print(f"The most popular day is {popular_day.capitalize()}.")

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print(f"The most popular hour is from {popular_hour} o'clock to {popular_hour + 1} o'clock.")

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip:')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f"The most popular start station is {popular_start_station}.")
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f"The most popular end station is {popular_end_station}.")
    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Station'] = df['Start Station'] + " to " + df['End Station']
    popular_start_end = df['Start-End Station'].mode()[0]
    print(f"The most popular trip is from {popular_start_end}.")
    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration:\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_seconds = int(total_travel_time)
    print(f"The total travel time sums up to {total_seconds:,} seconds.")
    print(f" -> This is the equivalent to {total_travel_time / 3600:.2f} hours.")
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_seconds = int(mean_travel_time)
    mean_minutes = int(mean_travel_time / 60)
    mean_left = mean_travel_time % 60
    print(f"The mean travel time sums up to {mean_seconds:,} seconds.")
    print(f" -> This is the equivalent to {mean_minutes:.0f} minutes & {mean_left:.0f} seconds.")

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats:\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    users_total = df['User Type'].count()
    print(f"There are a total of {users_total:,} users.")
    print("The different user types are:")
    for user_type, count in user_types.items():
        print(f" - {user_type}: {count}") 
    # TO DO: Display counts of gender
    if 'Gender' not in df.columns:
        print("No user gender data available for this city.")
        return
    else:
        user_gender = df['Gender'].value_counts()
        male_count = user_gender.get('Male', 0)
        female_count = user_gender.get('Female', 0)
        nan_count = df['Gender'].isna().sum()
        print(f"\n{male_count} customers registered as male")
        print(f"{female_count} customers registered as female")
        print(f"{nan_count} customers did not register any gender")
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = int(df['Birth Year'].min())
    most_recent_year = int(df['Birth Year'].max())
    most_common_year = int(df['Birth Year'].mode()[0])
    print(f"\nThe youngest customer was born in {most_recent_year}.")
    print(f"The oldest customer was born in {earliest_year}.")
    print(f"The most common birth year is {most_common_year}.")
    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("\nWould you like to see 5 lines of raw data? Enter yes or no.\n")
    start_loc = 0
    while True:
        if view_data != 'yes':
            break
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
