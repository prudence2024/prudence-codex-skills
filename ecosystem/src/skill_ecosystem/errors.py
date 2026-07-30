"""Domain exceptions raised by ecosystem infrastructure."""


class EcosystemError(Exception):
    """Base exception for expected ecosystem failures."""


class DataError(EcosystemError):
    """Raised when structured data cannot be loaded safely."""


class ValidationFailure(EcosystemError):
    """Raised when an operation requires valid input but validation fails."""

