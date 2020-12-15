import pickle
from dataclasses import asdict
from typing import List, Dict

import pandas

from load.keystroke_data import load_keystroke_data, Keystroke
from load.user_data import load_user_data, UserData
from render import render_age, render_gender, render_diagnosis_age, render_impact, render_hold_time, \
    render_latency_time, render_flight_time


def load_raw_data() -> (List[UserData], Dict[str, List[Keystroke]]):
    user_data_dir = "/Users/eagle/pwr_smaa/archive/Archived-users/Archived users"
    keystroke_data_dir = "/Users/eagle/pwr_smaa/archive/Archived-Data/Tappy Data"

    users_data = load_user_data(user_data_dir)
    keystroke_data = load_keystroke_data(keystroke_data_dir)

    return users_data, keystroke_data


def get_users_data_as_dataframe(user_data: List[UserData]) -> pandas.DataFrame:
    users_list = [asdict(user) for user in user_data]
    return pandas.DataFrame(users_list)


def get_keystrokes_data_as_dataframe(
        keystroke_data: Dict[str, List[Keystroke]]
) -> Dict[str, pandas.DataFrame]:
    keystroke_dataframe_dict = {}

    for keystroke_id, keystroke_list in keystroke_data.items():
        dataframe_list = [asdict(ks) for ks in keystroke_list]
        keystroke_dataframe_dict[keystroke_id] = pandas.DataFrame(dataframe_list)

    return keystroke_dataframe_dict


def get_keystrokes_df_as_list(keystrokes_dataframe: Dict[str, List[pandas.DataFrame]]) -> pandas.DataFrame:
    base_df = pandas.DataFrame([])

    for df in keystrokes_dataframe.values():
        base_df = base_df.append(df, sort=False)

    return base_df


def load_data():
    load_cached = False

    if load_cached:
        with open("users_pickle", "rb") as f_u:
            users_dataframe = pickle.load(f_u)

        with open("keystroke_pickle", "rb") as f_k:
            keystrokes_dataframe = pickle.load(f_k)

        with open("keystroke_list", "rb") as f_kl:
            keystrokes_df_list = pickle.load(f_kl)
    else:
        users_data, keystroke_data = load_raw_data()

        users_dataframe = get_users_data_as_dataframe(users_data)
        keystrokes_dataframe = get_keystrokes_data_as_dataframe(keystroke_data)
        keystrokes_df_list = get_keystrokes_df_as_list(keystrokes_dataframe)

        with open("users_pickle", "wb") as f_u:
            pickle.dump(users_dataframe, f_u)

        with open("keystroke_pickle", "wb") as f_k:
            pickle.dump(keystrokes_dataframe, f_k)

        with open("keystroke_list", "wb") as f_kl:
            pickle.dump(keystrokes_df_list, f_kl)

    return users_dataframe, keystrokes_dataframe, keystrokes_df_list


if __name__ == "__main__":
    users_dataframe, keystroke_dataframe, keystrokes_df_list = load_data()

    render_age(users_dataframe)
    render_gender(users_dataframe)
    render_diagnosis_age(users_dataframe)
    render_impact(users_dataframe)

    render_hold_time(keystrokes_df_list)
    render_latency_time(keystrokes_df_list)
    render_flight_time(keystrokes_df_list)

    debug = 1
    debug += 1
