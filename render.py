import matplotlib.pyplot as plt
import pandas


def render_age(users_df: pandas.DataFrame):
    age_parkinsons = users_df.age[(users_df.parkinsons == True)]
    age_no_parkinsons = users_df.age[(users_df.parkinsons == False)]

    plt.hist(
        [age_parkinsons, age_no_parkinsons],
        bins=25,
        histtype="bar",
        color=["#FF0000", "#00FF00"]
    )
    plt.xlabel("Age")
    plt.show()


def render_gender(users_df: pandas.DataFrame):
    gender_parkinson = users_df.gender[(users_df.parkinsons == True)]
    gender_no_parkinson = users_df.gender[(users_df.parkinsons == False)]

    plt.hist(
        [gender_parkinson, gender_no_parkinson],
        bins=2,
        histtype="bar",
    )
    plt.xlabel("Gender")
    plt.show()


def render_diagnosis_age(users_df: pandas.DataFrame):
    diagnosis_year = users_df.age[(users_df.parkinsons == True)]

    plt.hist(
        diagnosis_year,
        bins=25,
        histtype="bar",
        color=["#FF0000"]
    )

    plt.hist(100)
    plt.xlabel("Age at which the disease was diagnosed")
    plt.show()


def render_impact(users_df: pandas.DataFrame):
    impact = users_df.impact[(users_df.parkinsons == True)].value_counts()

    plt.pie(
        impact,
        labels=list(impact.axes[0]),
        startangle=90,
        autopct='%1.1f%%'
    )
    plt.hist(100)
    plt.show()


def render_parkinson(users_df: pandas.DataFrame):
    plot = users_df.plot.pie(
        subplots=True,
        autopct='%1.1f%%',
        xlabel="Parkinson",
    )


def render_hold_time(keystroke_df: pandas.DataFrame):
    hold_time = keystroke_df.groupby(['hold_time']).hold_time.count().sort_values()

    plt.hist(hold_time)
    plt.xlabel("Count of occurrences: Hold Time")
    plt.hist(100)
    plt.show()


def render_latency_time(keystroke_df: pandas.DataFrame):
    latency_time = keystroke_df.groupby(['latency_time']).latency_time.count().sort_values()

    plt.hist(latency_time)
    plt.xlabel("Count of occurrences: Latency Time")
    plt.hist(100)
    plt.show()


def render_flight_time(keystroke_df: pandas.DataFrame):
    flight_time = keystroke_df.groupby(['flight_time']).flight_time.count().sort_values()

    plt.hist(flight_time)
    plt.xlabel("Count of occurrences: Flight Time")
    plt.show()


def render_hold_time_extreme(keystroke_df: pandas.DataFrame, hold_time_min:int, hold_time_max:int):
    hist = keystroke_df[
        (hold_time_min < keystroke_df.hold_time) & (keystroke_df.hold_time < hold_time_max)
        ].hold_time.hist(bins=100).set(xlabel="Hold Time value", ylabel="Count of occurrences")


