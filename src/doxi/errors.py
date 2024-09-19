class DoxiError(Exception):
    """Base class for exceptions in Doxi."""
    pass

class RateLimitExceededError(DoxiError):
    pass

class PaymentRequiredError(DoxiError):
    pass

class InvalidURLError(DoxiError):
    pass