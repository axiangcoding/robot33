from robot33.internal.schema.response import CommonResult


def test_common_result_success():
    cr = CommonResult.success()
    assert cr.code == 0
    assert cr.message == "success"


def test_common_result_error():
    cr = CommonResult.error()
    assert cr.code == 1000
    assert cr.message == "internal error"
