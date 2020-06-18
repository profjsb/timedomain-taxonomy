from tdtax import schema
from tdtax.validate import is_valid


def test_validate_bad_yaml():
    ret = is_valid("tdtax/test/bad.yaml", schema)
    assert ret.find("not against") != -1


def test_validate_top_yaml():
    ret = is_valid("tdtax/top.yaml", schema)
    assert ret.find("valid") != -1
