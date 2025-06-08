from typing import Dict, List
from flask import Request
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity

class Calculator2:
  def __init__(self, driver_handler: DriverHandlerInterface) -> None:
    self.__driver_handler = driver_handler

  def calculate(self, request: Request) -> Dict:
    body = request.json
    input_data = self.__validate_body(body)
    calculated_number = self.__calculate_result(input_data)

    return self.__format_response(calculated_number)
    
  def __validate_body(self, body: Dict) -> float:
    if "numbers" not in body:
        raise HttpUnprocessableEntity("Body mal formatado")
    
    input_data = body["numbers"]
    return input_data
  
  def __format_response(self, result: float) -> Dict:
    return {
      "data": {
        "Calculator": "2",
        "result": round(result, 2),
        "success": True,
      }
    }
  
  def __calculate_result(self, numbers: List[float]) -> float:
    first_step_result = [((number * 11) ** 0.95) for number in numbers]

    result = self.__driver_handler.standard_derivation(first_step_result)

    return 1/result