import pytest
import solve

@pytest.mark.parametrize("expr, result", [
        ("1 + 1", 2),
        (" 4 / 2", 2),
        (" 5 / 2", 2.5),
        ("10 / 3", (10/3)),
        ("( 1024 / 8 ) + 1", 129),
        ("( 1024 / 7 ) + 9", (1024/7)+9),
        ("1000000000", 1000000000)
        ])

def test_solve(expr, result):
        assert solve.solveExpression(expr) == result
