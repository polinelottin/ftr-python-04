from typing import Dict, List
from flask import Request
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity

class Calculator4:
  def __init__(self, driver_handler: DriverHandlerInterface) -> None:
    self.__driver_handler = driver_handler

  def calculate(self, request: Request) -> Dict:
    body = request.json
    input_data = self.__validate_body(body)

    result = self.__calculate_average(input_data)

    return self.__format_response(result)
    
  def __validate_body(self, body: Dict) -> float:
    if "numbers" not in body:
        raise HttpUnprocessableEntity("Body mal formatado")
    
    input_data = body["numbers"]
    return input_data
  
  def __format_response(self, result: float) -> Dict:
    return {
      "data": {
        "Calculator": "4",
        "result": result,
        "success": True,
      }
    }
  
  def __calculate_average(self, numbers: List[float]) -> float:
    variance = self.__driver_handler.average(numbers)
    return variance
  