from typing import List, Optional, Union
from warnings import warn

class ApiKeyMissingError(Exception):
    """Raise Exception in case if no API KEY in Environment Variables"""