from dataclasses import dataclass
from os import listdir
from os.path import isfile, join, split
from typing import List

BASE_YEAR = 2018

_BIRTH_YEAR = "BirthYear: "
_GENDER = "Gender: "
_PARKINSONS = "Parkinsons: "
_TREMORS = "Tremors: "
_DIAGNOSIS_YEAR = "DiagnosisYear: "
_SIDED = "Sided: "
_UPDRS = "UPDRS: "
_IMPACT = "Impact: "
_LEVADOPA = "Levadopa: "
_DA = "DA: "
_MAOB = "MAOB: "
_OTHER = "Other: "

_FILE_USER = "User_"


@dataclass
class UserData:
    user_id: str
    birthday_year: int
    gender: str
    parkinsons: bool
    tremors: bool
    diagnosis_year: int
    sided: str
    updrs: str
    impact: str
    levadopa: bool
    da: bool
    maob: bool
    other: bool
    age: int
    diagnosis_age: int


def _load_from_file(full_file_path: str) -> UserData:
    _, tail = split(full_file_path)
    id = tail[len(_FILE_USER):-4]

    with open(full_file_path, "r") as user_data_file:
        for line in user_data_file.readlines():
            line = line.strip("\n")

            if line.startswith(_BIRTH_YEAR):
                birthday_year = line[len(_BIRTH_YEAR):]

                try:
                    birthday_year = int(birthday_year)
                except ValueError:
                    birthday_year = 0

                age = 0
                if birthday_year > 0:
                    age = BASE_YEAR - birthday_year

            elif line.startswith(_GENDER):
                gender = line[len(_GENDER):]
            elif line.startswith(_PARKINSONS):
                parkinsons = line[len(_PARKINSONS):]
                parkinsons = parkinsons == "True"
            elif line.startswith(_TREMORS):
                tremors = line[len(_TREMORS):]
                tremors = bool(tremors)
            elif line.startswith(_DIAGNOSIS_YEAR):
                diagnosis_year = line[len(_DIAGNOSIS_YEAR):]

                try:
                    diagnosis_year = int(diagnosis_year)
                except ValueError:
                    diagnosis_year = 0

                diagnosis_age = 0
                if diagnosis_age > 0:
                    diagnosis_age = BASE_YEAR - diagnosis_age

            elif line.startswith(_SIDED):
                sided = line[len(_SIDED):]
            elif line.startswith(_UPDRS):
                updrs = line[len(_UPDRS):]
            elif line.startswith(_IMPACT):
                impact = line[len(_IMPACT):]
            elif line.startswith(_LEVADOPA):
                levadopa = line[len(_LEVADOPA):]
                levadopa = levadopa == "True"
            elif line.startswith(_DA):
                da = line[len(_DA):]
                da = bool(da)
            elif line.startswith(_MAOB):
                maob = line[len(_MAOB):]
                maob = bool(maob)
            elif line.startswith(_OTHER):
                other = line[len(_OTHER):]
                other = bool(other)

        u = UserData(
            id,
            birthday_year,
            gender,
            parkinsons,
            tremors,
            diagnosis_year,
            sided,
            updrs,
            impact,
            levadopa,
            da,
            maob,
            other,
            age,
            diagnosis_age
        )

    return u


def load_user_data(file_path: str) -> List[UserData]:
    users = []

    for file_name in listdir(file_path):
        full_file_path = join(file_path, file_name)

        if not isfile(full_file_path):
            continue

        user_data = _load_from_file(full_file_path)
        users.append(user_data)

    return users
