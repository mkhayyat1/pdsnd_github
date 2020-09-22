# Read me.txt
# Websites that helped me to skill up my knowledge in Python
# 1- Stackoverflow
# 2- Pandas
# 3- Geeksforgeeks
# 4- Python

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
      enter1 = input('\nPlease choose a city to explore: chicago - new york city - washington: \n').lower()
      if enter1 not in cities:
        print('Wrong input! ')
        continue
      elif enter1 in cities:
          check1 = input('\nYou choose {}, is that correct? type (yes) to continue or type (no) to re-choose the city \n'.format(enter1))
          if check1 != 'yes' and check1 != 'no':
               print('Wrong input! ')
               continue
          elif check1 == 'no':
            continue
          elif check1 == 'yes':
            city = enter1
      break

    # TO DO: get user input for month (all, january, february, ... , june)

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
      enter2 = input('\nChoose the wanted month to filter by, from January to June or type (all) to continue without filter: \n').lower()
      if enter2 not in months and enter2 != 'all':
         print('wromg input!')
         continue
      elif enter2 == 'all':
         month = 'all'
         break
      elif enter2 in months:
         month = enter2
         break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while True:
      enter3 = input('\nChoose specific day of the week (sunday to saturday) to filter by, or type (all) to continue without filter: \n').lower()
      if enter3 not in days and enter3 != 'all':
         print('wromg input! ')
         continue
      elif enter3 == 'all':
         day = 'all'
         break
      elif enter3 in days:
         day = enter3
         break

    # Details analysis, to perform decribe function for some data (optional function).
    while True:
      enter4 = input('\nDo you want to show detail analysis for the selected data such as min, max, top, unique, etc.. type (yes) or (no) \n').lower()
      if enter4 != 'yes' and enter4 != 'no':
         print('Wrong input! ')
         continue
      else:
         details = enter4
         break
    return city, month, day, details
    print('-'*40)


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df, details):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    com_month = df['month'].value_counts().index[0]
    print('The most common month is: {}'.format(com_month))

    # TO DO: display the most common day of week
    com_day = df['day_of_week'].value_counts().index[0]
    print('The most common day of week is: {}'.format(com_day))

    # TO DO: display the most common start hour
    com_strh = df['Start Time'].value_counts().index[0]
    print('The most common start hour is: {}'.format(com_strh))

    # Details Option
    if details == 'yes':
       det_month = df['month'].describe()
       print('The details analysis about the month is {}'.format(det_month))

       det_days = df['day_of_week'].describe()
       print('The details analysis about the day of the week is{}'.format(det_days))

       det_strt = df['Start Time'].describe()
       print('The details analysis about the start time is{}'.format(det_strt))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, details):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_start = df['Start Station'].value_counts().index[0]
    print('Most commonly used start station: {}.'.format(com_start))

    # TO DO: display most commonly used end station
    com_end = df['End Station'].value_counts().index[0]
    print('Most commonly used end station: {}.'.format(com_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['combine'] = df['Start Station'] + df['End Station']
    com_both = df['combine'].value_counts().index[0]
    print('Most frequent combination of start and end station trip: {}.'.format(com_both))

    # Details Option
    if details == 'yes':
       det_start = df['Start Station'].describe()
       print('The details analysis about the start station is {}'.format(det_start))

       det_end = df['End Station'].describe()
       print('The details analysis about the end station is{}'.format(det_end))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, details):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trvl_time = df['Trip Duration'].sum()
    print('Total travel time: {} seconds.'.format(total_trvl_time))

    # TO DO: display mean travel time
    mean_trvl_time = df['Trip Duration'].mean()
    print('Mean travel time: {} seconds.'.format(mean_trvl_time))

    # Details Option
    if details == 'yes':
       det_trip = df['Trip Duration'].describe()
       print('The details analysis about the trip duration is {}'.format(det_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts().index[0]
    print(user_type)

    # TO DO: Display counts of gender
    city_check = df.columns
    if 'Gender' in city_check:
      user_gender = df['Gender'].value_counts().index[0]
      print(user_gender)
    else :
      print('There is no gender data for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in city_check:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()
        print('Earliest user year of birth: %d.'% (earliest_birth))
        print('Most recent user year of birth: %d.'% (recent_birth))
        print('Most common user year of birth: %d.'% (common_birth))
    else:
        print('There is no birth year data for this city')

    count1 = -5
    count2 = 0
    while True:
      rowenter = input('\nWould like to see more row data? \n')
      count1 += 5
      count2 += 5
      if rowenter == 'yes':
         row_data = pd.read_csv(CITY_DATA[city]).iloc[count1 : count2]
         print('row data goes as follow: \n', row_data)
         continue
      elif rowenter == 'no':
         break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day, details = get_filters()
        df = load_data(city, month, day)

        time_stats(df, details)
        station_stats(df, details)
        trip_duration_stats(df, details)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
     main()
