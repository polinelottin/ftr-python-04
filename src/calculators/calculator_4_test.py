from typing import Dict, List
from pytest import raises
from src.calculators.calculator_4 import Calculator4
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandler(DriverHandlerInterface):
  def standard_derivation(self, numbers: List[float]) -> float:
    return 2.0
  
  def variance(self, numbers: List[float]) -> float:
    return 5.0
  
  def average(self, numbers: List[float]) -> float:
    return 3.0

def test_calculate_integration():
  mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
  calc = Calculator4(MockDriverHandler())

  response = calc.calculate(mock_request)

  assert isinstance(response, dict)
  assert response == {
    "data": {
      "Calculator": "4",
      "result": 3.0,
      "success": True,
    }
  }

def test_calculate_integration_with_exception():
  mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
  calc = Calculator4(MockDriverHandler())

  response = calc.calculate(mock_request)

  assert isinstance(response, dict)
  assert response == {
    "data": {
      "Calculator": "4",
      "result": 3.0,
      "success": True,
    }
  }

def test_calculate_with_invalid_body():
  mock_request = MockRequest({"wrong_key": 1})
  calc = Calculator4(MockDriverHandler())

  with raises(Exception) as e:
    calc.calculate(mock_request)
    assert str(e.value) == "Body mal formatado"