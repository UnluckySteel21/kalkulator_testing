from ..main import (
    saskaitisana,
    alnemsana,
    dalisana,
    reizinasana,
    kapinasana
)

def test_saskaitisana():
    assert saskaitisana(4, 5) == 9
    assert saskaitisana(-2, 10) == 8
    assert saskaitisana(2.5, 70) == 72.5
    assert saskaitisana(-3.5, 10) == 6.5
    assert saskaitisana(0.0, 0.0) == 0.0

def test_atnesmana():
    assert alnemsana(4, 5) == -1
    assert alnemsana(-2, 10) == -12
    assert alnemsana(20, -2.5) == 22.5
    assert alnemsana(3.5, 2.5) == 1

def test_dalisana():
    assert dalisana(4, 5) == 0.8
    assert dalisana(-10, 2) == -5
    assert dalisana(20, 2.5) == 8
    assert dalisana(3.5, 2.5) == 1.4
    assert dalisana(6, 2) == 3

def test_reizinasana():
    assert reizinasana(4, 5) == 20
    assert reizinasana(-10, 2) == -20
    assert reizinasana(18, 2.6) == 46.8
    assert reizinasana(3.5, 2.5) == 8.75
    assert reizinasana(-6, -2) == 12

def test_kapinasana():
    assert kapinasana(4, 5) == 1024
    assert kapinasana(-10, 2) == 100
    assert kapinasana(18, 2.6) == 1835.306122
    assert kapinasana(3.5, 2.5) == 22.9176515
    assert kapinasana(-6, -2) == 0.0277778