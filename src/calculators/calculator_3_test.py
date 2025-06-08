from pytest import raises
from src.calculators.calculator_3 import Calculator3
from src.mocks.driver_handler_mock import MockDriverHandler
from src.mocks.request_mock import MockRequest

def test_calculate():
    mock_request = MockRequest(body={"numbers": [5]})
    calc = Calculator3(MockDriverHandler())

    response = calc.calculate(mock_request)

    assert isinstance(response, dict)
    assert response == {
        "data": {
            "Calculator": "3",
            "result": 5.0,
            "success": True,
        }
    }

def test_calculate_integration_with_exception():
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
    calc = Calculator3(MockDriverHandler())

    with raises(Exception) as e:
        response = calc.calculate(mock_request)
        assert str(e.value) == "Variance é menor que a multiplicação"
        assert e.value.status_code == 400

def test_calculate_with_invalid_body():
    mock_request = MockRequest({"wrong_key": 1})
    calc = Calculator3(MockDriverHandler())

    with raises(Exception) as e:
        calc.calculate(mock_request)
        assert str(e.value) == "Body mal formatado"
        assert e.value.status_code == 422