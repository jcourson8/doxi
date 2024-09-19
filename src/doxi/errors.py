class RateLimitExceededError(BaseException):
    """Custom exception to indicate rate limit exceeded."""
    pass

class PaymentRequiredError(BaseException):
    """Custom exception to indicate payment required."""
    pass