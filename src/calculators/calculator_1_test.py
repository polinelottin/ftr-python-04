from typing import Dict
from pytest import raises
from src.main.factories.calculator1_factory import calculator1_factory
from src.mocks.request_mock import MockRequest

def test_calculate():
  mock_request = MockRequest({"number": 10})
  calc = calculator1_factory()

  response = calc.calculate(mock_request)

  # formato da resposta
  assert "data" in response
  assert "result" in response["data"]
  assert "success" in response["data"]
  assert "Calculator" in response["data"]

  # assertividade da resposta
  assert response["data"]["result"] == 45.81
  assert response["data"]["Calculator"] == "1"

def test_calculate_with_invalid_body():
  mock_request = MockRequest(body={"wrong_key": 1})
  calc = calculator1_factory()

  with raises(Exception) as e:
    calc.calculate(mock_request)

    assert str(e.value) == "Body mal formatado"
    assert e.value.status_code == 422
