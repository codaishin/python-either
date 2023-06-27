"""either"""
from abc import abstractmethod
from typing import Any, Callable, Generic, TypeVar

L = TypeVar("L")
R = TypeVar("R")
T = TypeVar("T")


class Either(Generic[L, R]):
    """Basic either interface"""

    @classmethod
    def left(cls, left: L) -> "Either[L, R]":
        """get an either with an error"""
        return _Left(left)

    @classmethod
    def right(cls, right: R) -> "Either[L, R]":
        """get a partial right object"""
        return _Right(right)

    @abstractmethod
    def fold(self, left: Callable[[L], T], right: Callable[[R], T]) -> T:
        """fold either"""

    def map_left(self, map_fn: Callable[[L], T]) -> "Either[T, R]":
        """map left"""

        return self.fold(lambda l: Either.left(map_fn(l)), Either.right)

    def map_right(self, map_fn: Callable[[R], T]) -> "Either[L, T]":
        """map right"""

        return self.fold(Either.left, lambda r: Either.right(map_fn(r)))


class _Left(Either[L, Any]):
    def __init__(self, value: L) -> None:
        self._value = value

    def fold(self, left: Callable[[L], T], right: Callable[[Any], T]) -> T:
        return left(self._value)


class _Right(Either[Any, R]):
    def __init__(self, value: R) -> None:
        self._value = value

    def fold(self, left: Callable[[Any], T], right: Callable[[R], T]) -> T:
        return right(self._value)
