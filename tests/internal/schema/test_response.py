from typing import Any

import pytest

from robot33.internal.schema.errors import CommonError
from robot33.internal.schema.response import CommonResult


@pytest.mark.parametrize("data", [{"data": "01"}, ("data", 2), "str only", 0.3, 4])
def test_common_result_success(data: object):
    cr = CommonResult.success(data)
    assert cr.code == 0
    assert cr.message == "success"
    assert cr.data == data


@pytest.mark.parametrize("ce,message", [
    (CommonError.ERROR, None),
    (CommonError.ERROR, "custom error"),
])
def test_common_result_error(ce: CommonError, message: str):
    cr = CommonResult.error(ce, message)
    assert cr.code == ce.code
    if message:
        assert cr.message == message
    else:
        assert cr.message == ce.description
