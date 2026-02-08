class AutomationError(Exception):
    """Base class for all automation errors."""
    pass


class SystemException(AutomationError):
    pass


class BusinessException(AutomationError):
    pass