import pytest
from idms.common.constants import ATTR_SYS_PREFIX, ATTR_USR_PREFIX

@pytest.mark.unit
def test_constants():
    assert ATTR_SYS_PREFIX == "sys::"
    assert ATTR_USR_PREFIX == "user::"