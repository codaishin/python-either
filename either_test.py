"""tests"""

from unittest import TestCase

from either import Either


class TestEither(TestCase):
    """test either"""

    def test_fold_right(self) -> None:
        """fold right"""

        either = Either[str, int].right(42)
        right = either.fold(
            lambda _: -1,
            lambda r: r,
        )
        self.assertEqual(42, right)

    def test_fold_left(self) -> None:
        """fold right"""

        either = Either[int, str].left(42)
        left = either.fold(
            lambda l: l,
            lambda _: -1,
        )
        self.assertEqual(42, left)

    def test_map_right(self) -> None:
        """right map right"""

        right = (
            Either.right(11)
            .map_right(lambda v: float(v) / 2)
            .fold(
                lambda _: -1,
                lambda r: r,
            )
        )
        self.assertEqual(5.5, right)

    def test_map_left(self) -> None:
        """right map left"""

        left = (
            Either.left(11)
            .map_left(lambda v: float(v) / 2)
            .fold(
                lambda l: l,
                lambda _: -1,
            )
        )
        self.assertEqual(5.5, left)
