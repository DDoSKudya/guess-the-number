"""
The main file for launching the game.
"""


from resources.constants import Constants
from resources.messages import Messages
from resources.functions import custom_functions


while True:
    random_value = custom_functions.get_random_value()
    user_value = custom_functions.input_user_value()
    if not user_value.isdigit():
        if custom_functions.check_stop_key(user_value):
            print(
                Messages.statistics.format(
                    total_attempts=Constants.total_attempts,
                    total_wins=Constants.total_wins,
                )
            )
            break
        else:
            continue

    user_value = int(user_value)

    if not custom_functions.check_valid_range(user_value):
        print(
            Messages.error_msg.format(
                min_value=Constants.min_value,
                max_value=Constants.max_value,
                stop_key=Constants.stop_key,
            )
        )
        continue

    Constants.total_attempts += 1
    win = custom_functions.compare_values(user_value, random_value)
    Constants.total_wins = (
        Constants.total_wins + 1
        if win
        else Constants.total_wins
    )
    game_again = custom_functions.game_status()

    if not game_again:
        print(
            Messages.statistics.format(
                total_attempts=Constants.total_attempts,
                total_wins=Constants.total_wins,
            )
            + Messages.bye_msg
        )
        break
    else:
        continue
