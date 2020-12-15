import matplotlib.pyplot as plt
import pandas


def render_age(users_df: pandas.DataFrame):
    age_parkinsons = users_df.age[(users_df.parkinsons == True)]
    age_no_parkinsons = users_df.age[(users_df.parkinsons == False)]

    plt.hist(
        [age_parkinsons, age_no_parkinsons],
        bins=25, histtype="bar", color=["#FF0000", "#00FF00"]
    )
    plt.xlabel("Age")
    plt.show()


def render_gender(users_df: pandas.DataFrame):
    genders = users_df.gender.value_counts()

    plt.pie(genders, labels=["Male", "Female"])
    plt.show()


def render_diagnosis_age(users_df: pandas.DataFrame):
    diagnosis_year = users_df.age[(users_df.parkinsons == True)]

    plt.hist(
        diagnosis_year,
        bins=25, histtype="bar", color=["#FF0000"]
    )

    plt.xlabel("Age at which the disease was diagnosed")
    plt.show()


def render_impact(users_df: pandas.DataFrame):
    impact = users_df.impact.value_counts()
    labels = ["Medium", "Mild", " ------", "Severe", "UNKNOWN"]

    plt.pie(impact, labels=labels)
    plt.show()


def render_hold_time(keystroke_df: pandas.DataFrame):
    hold_time = keystroke_df.groupby(['hold_time']).hold_time.count().sort_values()

    plt.hist(hold_time)
    plt.xlabel("Count of occurrences: Hold Time")
    plt.show()


def render_latency_time(keystroke_df: pandas.DataFrame):
    latency_time = keystroke_df.groupby(['latency_time']).latency_time.count().sort_values()

    plt.hist(latency_time)
    plt.xlabel("Count of occurrences: Latency Time")
    plt.show()


def render_flight_time(keystroke_df: pandas.DataFrame):
    flight_time = keystroke_df.groupby(['flight_time']).flight_time.count().sort_values()

    plt.hist(flight_time)
    plt.xlabel("Count of occurrences: Flight Time")
    plt.show()
