from langchain_core.tools import tool
import datetime
import pytz

@tool
def calculate(expression: str) -> float:
    """
    Evaluates a simple mathematical expression as a string and returns the result as a float.
    
    Args:
        expression: The mathematical expression to evaluate (e.g., "5 + 3").
        
    Returns:
        The numerical result of the expression.
    """
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"
    

@tool
def get_current_time(timezone: str = "UTC") -> str:
    """
    Returns the current date and time in a specified timezone.

    Args:
        timezone: The timezone to get the current time for (e.g., "America/New_York").
                  Defaults to "UTC" if not specified.

    Returns:
        The current date and time as a string.
    """
    try:
        # Get the current time in UTC
        now_utc = datetime.datetime.now(datetime.UTC)
        
        # Get the timezone object using pytz
        target_timezone = pytz.timezone(timezone)
        
        # Convert the UTC time to the target timezone
        return now_utc.astimezone(target_timezone).strftime("%Y-%m-%d %H:%M:%S %Z")
    except pytz.UnknownTimeZoneError:
        return f"Error: Unknown timezone '{timezone}'"
    except Exception as e:
        return f"Error: {e}"