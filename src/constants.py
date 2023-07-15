from config.settings import settings
from datetime import datetime


JSON_FILE_PATH = settings.JSON_FILE_PATH
"""
str: The path to the JSON file for rates.
"""

FIRST_DAY_OF_CURRENT_MONTH = datetime.now().replace(day=1).date()
"""
datetime.date: The date object representing the first day of the current month.
"""

MIN_VALUE = 500
"""
int: The minimum value allowed for the declared value.
"""

MAX_VALUE = 1_000_000
"""
int: The maximum value allowed for the declared value.
"""
