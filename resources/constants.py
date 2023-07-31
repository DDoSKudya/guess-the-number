"""
Changeable data about the game process.
"""


from resources.messages import Messages


__all__ = ["Constants"]


class Constants:
    """Changeable data about the game process
    (score, attempts, range of random numbers, etc.)"""

    min_value: int = 1
    max_value: int = 100

    total_attempts: int = 0
    total_wins: int = 0

    stop_key: str = "stop"

    is_status_key_dict: dict = {
        True: Messages.bye_msg,
        False: Messages.error_msg.format(
            min_value=min_value,
            max_value=max_value,
            stop_key=stop_key,
        ),
        "yes": True,
        "no": False,
        "y": True,
        "n": False,
    }
