import lsst.geom as geom


def test_geom():
    p = geom.Point2I(0, 0)
    assert p.getX() == 0
    assert p.getY() == 0
