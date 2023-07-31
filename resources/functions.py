"""
The entire functionality of the script used for user interaction is stored.
"""


import random
import typing

from resources.constants import Constants
from resources.messages import Messages


__all__ = ["custom_functions"]


class Functions:
    """Custom functions for data processing."""

    @staticmethod
    def get_random_value() -> int:
        """Random number generation according to the data range
        ('min_value' and 'max_value').

        Returns:
            int: Random number.
        """

        return random.randint(Constants.min_value, Constants.max_value)

    @staticmethod
    def input_user_value() -> str:
        """Accepts a custom number.

        Returns:
            str: The value entered by the user.
        """

        return input(
            Messages.welcome_msg.format(
                min_value=Constants.min_value,
                max_value=Constants.max_value,
                stop_key=Constants.stop_key,
            )
        )

    @staticmethod
    def check_stop_key(user_value) -> bool:
        """Checking for a safe word.

        Args:
            user_value (typing.Union[str, int]): The value entered by the user.

        Returns:
            bool: The result of comparing stop words.
        """

        status = all(
            [
                isinstance(user_value, str),
                user_value.lower() == Constants.stop_key,
            ]
        )

        print(Constants.is_status_key_dict.get(status))

        return status

    @staticmethod
    def check_valid_range(user_value) -> bool:
        """Checking for a safe word.

        Args:
            user_value (int): The value entered by the user.

        Returns:
            bool: The result of comparing stop words.
        """

        return Constants.min_value <= user_value <= Constants.max_value

    @staticmethod
    def compare_values(user_value, random_value) -> bool:
        """Comparison of random and custom numbers.

        Args:
            user_value (int): The number made by the user.
            random_value (int): The generated number by the random library.

        Returns:
            bool: Winning status.
        """

        result = Messages.info_msg.format(
            random_value=random_value,
            user_value=user_value,
        )

        if user_value == random_value:
            result += Messages.true_msg
            win = True
        else:
            result += Messages.false_msg
            win = False

        print(result)

        return win

    def game_status(self) -> bool:
        """Checking the status of the current game.

        Returns:
            bool: the status of the choice to play or not.
        """

        user_status_game = input(Messages.again_msg)
        game_again = Constants.is_status_key_dict.get(user_status_game.lower())
        if game_again is None:
            print(Messages.confirmation_error)
            return self.game_status()

        return game_again


custom_functions = Functions()
