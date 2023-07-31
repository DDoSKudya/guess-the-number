# -*-coding: utf-8 -*-

"""
Stored message blanks for user interaction through game events.
"""


__all__ = ["Messages"]


class Messages:
    """Prepared templates and messages to the user for interactivity."""

    welcome_msg: str = (
        "\nGuess the number from {min_value} to {max_value} "
        "(to finish the game, enter '{stop_key}'):\nNumber: "
    )
    bye_msg: str = "\nThe game is over.\n"
    info_msg: str = (
        "\nThe hidden number {random_value}.\nYour number is {user_value}.\n"
    )
    error_msg: str = (
        "\nEnter a number from {min_value} to {max_value} "
        "(to finish the game, enter {stop_key}).\n"
    )
    true_msg: str = "\nYou've won!\n"
    false_msg: str = "\nYou've lost!\n"

    again_msg: str = "\nPlay some more? (Yes, No)\nAnswer: "
    confirmation_error: str = "\nYou need to enter Yes or No.\n"

    statistics: str = (
        "\nStatistics:\nTotal attempts: {total_attempts},"
        "\nWins: {total_wins}.\n"
    )
