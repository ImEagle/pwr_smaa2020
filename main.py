from load.keystroke_data import load_keystroke_data
from load.user_data import load_user_data

if __name__ == "__main__":
    user_data_dir = "/Users/eagle/pwr_smaa/archive/Archived-users/Archived users"
    keystroke_data_dir = "/Users/eagle/pwr_smaa/archive/Archived-Data/Tappy Data"

    users_data = load_user_data(user_data_dir)
    keystroke_data = load_keystroke_data(keystroke_data_dir)

    debug = 1
    debug += 1
