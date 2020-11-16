import csv
from dataclasses import dataclass
from os import listdir
from os.path import join, isfile
from typing import List, Dict


@dataclass
class Keystroke:
    user_id: str
    date: str
    timestamp: str
    hand: str
    hold_time: float
    direction: str
    latency_time: float
    flight_time: float


def _load_from_file(full_file_path: str) -> List[Keystroke]:
    keystroke_data = []

    print(full_file_path)

    with open(full_file_path, "r") as keystroke_csv_file:
        reader = csv.reader(keystroke_csv_file, delimiter="\t")

        try:
            for row in reader:
                try:
                    ks = Keystroke(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        float(row[4]),
                        row[5],
                        float(row[6]),
                        float(row[7]),
                    )
                except ValueError:
                    continue

                keystroke_data.append(ks)
        except csv.Error:
            pass

    return keystroke_data


def load_keystroke_data(file_path: str) -> Dict[str, List[Keystroke]]:
    keystrokes = {}

    for file_name in listdir(file_path):
        full_file_path = join(file_path, file_name)

        if not isfile(full_file_path):
            continue

        keystroke_list = _load_from_file(full_file_path)
        if keystroke_list:
            ks = keystroke_list[0]

            keystrokes[ks.user_id] = keystroke_list

    return keystrokes
