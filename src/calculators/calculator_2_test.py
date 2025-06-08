from pytest import raises
from src.calculators.calculator_2 import Calculator2
from src.mocks.driver_handler_mock import MockDriverHandler
from src.mocks.request_mock import MockRequest

def test_calculate_integration():
  mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
  calc = Calculator2(MockDriverHandler())

  response = calc.calculate(mock_request)

  assert isinstance(response, dict)
  assert response == {
    "data": {
      "Calculator": "2",
      "result": 0.5,
      "success": True,
    }
  }

def test_calculate_with_invalid_body():
  mock_request = MockRequest({"wrong_key": 1})
  calc = Calculator2(MockDriverHandler())

  with raises(Exception) as e:
    calc.calculate(mock_request)
    assert str(e.value) == "Body mal formatado"
    assert str(e.status_code) == 422
