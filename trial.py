import time
import pandas as pd
import numpy as np

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}

month_index_1 = {
    "JAN": "1",
    "FEB": "2",
    "MAR": "3",
    "APR": "4",
    "MAY": "5",
    "JUN": "6",
    "JUL": "7",
    "AUG": "8",
    "SEP": "9",
    "OCT": "10",
    "NOV": "11",
    "DEC": "12",
    "All": "All",
}

month_index_2 = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

day_index_1 = {
    "MON": 0,
    "TUE": 1,
    "WED": 2,
    "THU": 3,
    "FRI": 4,
    "SAT": 5,
    "SUN": 6,
    "All": "All",
}

day_index_2 = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "All" to apply no month filter
        (str) day - name of the day of week to filter by, or "All" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")

    city_found, month_found, day_found = False, False, False

    while True:

        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        if not city_found:
            city = input(
                "Choose one of these cities to explore Chicago, Washington, New York City: "
            )
            city = city.lower()
            if city not in CITY_DATA:
                print(
                    "City not found. Please choose one of these: Chicago, Washington, New York City"
                )
                continue
            else:
                city_found = True

        print("\n")

        # get user input for month (All, january, february, ... , june)
        if not month_found:
            month = input(
                "Choose one of these months: JAN, FEB, MAR, APR, MAY, JUN or All to explore All months: "
            )
            month = month.upper()
            if month not in month_index_1:
                print("Not available. Please, enter a valid month!")
                continue
            else:
                month_found = True

        print("\n")

        # get user input for day of week (All, monday, tuesday, ... sunday)
        day = input(
            "Choose one of these day: MON, TUE, WED, THU, FRI, SAT, SUN, or All to explore All days: "
        )
        day = day.upper()
        if day not in day_index_1:
            print("Not available. Please, enter a valid day!")
            continue
        else:
            break

    print("-" * 40)
    print("\n")
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "All" to apply no month filter
        (str) day - name of the day of week to filter by, or "All" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    start_time = time.time()
    print("Data is being prepared!")

    df = pd.read_csv(CITY_DATA.get(city))

    # extract start month from the Start time column to create Start Month column
    df["Start Month"] = pd.DatetimeIndex(df["Start Time"]).month

    # extract start day from the Start time column to create Start Day column
    df["Start Day"] = pd.to_datetime(
        df["Start Time"], format="%Y-%m-%d %H:%M:%S"
    ).dt.dayofweek

    # extract start hour from the Start Time column to create an Start Hour column
    df["Start Hour"] = pd.DatetimeIndex(df["Start Time"]).hour

    # filter on month, if month is specified
    if month != month_index_1.get("All"):
        df = df[df["Start Month"] == int(month_index_1.get(month))]

    # filter on day, if day is specified
    if day != day_index_1.get("All"):
        df = df[df["Start Day"] == int(day_index_1.get(day))]

    print("Done!")
    print("\nIt took {} seconds.".format(round((time.time() - start_time), 2)))
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print("\nDisplaying statistics on the most frequent times of travel...\n")
    start_time = time.time()

    # display the most common month
    if month == month_index_1.get("All"):
        popular_month = df["Start Month"].dropna()
        if popular_month.empty:
            print("No popular month found. Please, refilter your data again!")
        else:
            popular_month = popular_month.mode()[0]
            print("Most popular month is: {}".format(month_index_2.get(popular_month)))
    else:
        print("Select All to get the most popular month instead of {}".format(month))

    # display the most common day of week
    if day == day_index_1.get("All"):
        popular_day = df["Start Day"].dropna()  # .mode()[0]
        if popular_day.empty:
            print("No popular day found. Please, refilter your data again!")
        else:
            popular_day = popular_day.mode()[0]
            print("Most popular day is: {}".format(day_index_2.get(popular_day)))
    else:
        print(
            "Select All to get the most popular day instead of {}".format(day.title())
        )

    # display the most common start hour
    popular_start_hour = df["Start Hour"].dropna()
    if popular_start_hour.empty:
        print("No popular start hour found. Please, refilter your data again!")
    else:
        popular_start_hour = popular_start_hour.mode()[0]
        print("Most popular start hour is : {}:00 hrs".format(popular_start_hour))

    print("\nIt took {} seconds.".format(round((time.time() - start_time), 2)))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nDisplaying statistics on the most popular stations and trip...\n")
    start_time = time.time()

    # display most commonly used start station
    most_popular_start_station = df["Start Station"]
    if most_popular_start_station.empty:
        print("No start station found. Please, refilter your data again!")
    else:
        most_popular_start_station = most_popular_start_station.mode()[0]
        print("Most popular start station: {}".format(most_popular_start_station))

    # display most commonly used end station
    most_popular_end_station = df["End Station"]
    if most_popular_end_station.empty:
        print("No End station found. Please, refilter your data again!")
    else:
        most_popular_end_station = most_popular_end_station.mode()[0]
        print("Most popular end station is: {}".format(most_popular_end_station))

    # display most frequent combination of start station and end station trip
    most_frequent_start_and_end_station = df[["Start Station", "End Station"]].dropna()
    if most_frequent_start_and_end_station.empty:
        print("No data found. Please, refilter your data again!")
    else:
        most_frequent_start_and_end_station = (
            most_frequent_start_and_end_station.groupby(
                ["Start Station", "End Station"]
            )
            .size()
            .sort_values(ascending=False)
        )
        trip_count = most_frequent_start_and_end_station.iloc[0]
        stations = most_frequent_start_and_end_station[
            most_frequent_start_and_end_station == trip_count
        ].index[0]

        start_station, end_station = stations
        print(
            "Most frequent start station is: {} and end station is: {} which were part of trips {} times".format(
                start_station, end_station, trip_count
            )
        )

    print("\nIt took {} seconds.".format(round((time.time() - start_time), 2)))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    valid_time = df["Trip Duration"].dropna()
    if valid_time.empty:
        print("No record found!! Please adjust your filter")
    else:
        total_time = valid_time.sum()
        print("Total travel time in seconds is : {}".format(total_time))

        # display mean travel time
        mean_travel_time = valid_time.mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    user_type = df["User Type"].dropna()

    if user_type.empty:
        print("No data available for specified filter, please adjust your filter!!")
    else:
        user_type = user_type.value_counts()
        print("User type details for the filter specified : {}".format(user_type))

        # Display counts of gender
        if "Gender" in df:
            user_gender = df["Gender"].dropna()
            if user_gender.empty:
                print(
                    "No data available for specified filter, please adjust your filter!!"
                )
            else:
                user_gender = user_gender.value_counts()
                print("User gender count : {}".format(user_gender))

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        birth_years = df["Birth Year"].dropna()
        if birth_years.empty:
            print("No data available for specified filter, please adjust your filter!!")
        else:
            user_birth_year = df["Birth Year"].dropna()
            if user_birth_year.empty:
                print("No data available for your filter, please adjust your filter!!!")
            else:
                oldest_user = user_birth_year.min()
                print(
                    "Earliest year of birth for the selected filter : {}".format(
                        int(oldest_user)
                    )
                )

                youngest_user = user_birth_year.max()
                print(
                    "Most recent year of birth for the selected filter : {}".format(
                        int(youngest_user)
                    )
                )

                most_common_year_of_birth = user_birth_year.mode()[0]
                print(
                    "Most common year of birth for the selected filter : {}".format(
                        int(most_common_year_of_birth)
                    )
                )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def show_raw_data(df):
    """method to print the selected data frame, 5 at a time """
    choice = input("Would you like to see raw data? [Y/n] : ")
    choice = choice.upper()

    count = 0
    if choice == "Y":
        for row in df.iterrows():
            print(row)
            count += 1
            if count != 0 and count % 5 == 0:
                choice = input("Would you like to see raw data? [Y/n] : ")
                if choice.upper() != "Y":
                    break


def main():
    while True:
        city, month, day = get_filters()
        print(
            "Input to be processed -> City : {}, Month : {}, Day : {}".format(
                city, month, day
            )
        )

        df = load_data(city, month, day)

        if df.empty:
            print("No data found for specified filter, please adjust your filters!!!")
            continue

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        show_raw_data(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()