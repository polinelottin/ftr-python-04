from typing import Dict, List
from flask import Request
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity
from src.errors.http_bad_request import HttpBadRequest

class Calculator3:
  def __init__(self, driver_handler: DriverHandlerInterface) -> None:
    self.__driver_handler = driver_handler

  def calculate(self, request: Request) -> Dict:
    body = request.json
    input_data = self.__validate_body(body)

    variance = self.__calculate_variance(input_data)
    multiplication = self.__calculate_multiplication(input_data)
    self.__verify_result(variance, multiplication)

    return self.__format_response(variance)
    
  def __validate_body(self, body: Dict) -> float:
    if "numbers" not in body:
        raise HttpUnprocessableEntity("Body mal formatado")
    
    input_data = body["numbers"]
    return input_data
  
  def __format_response(self, result: float) -> Dict:
    return {
      "data": {
        "Calculator": "3",
        "result": result,
        "success": True,
      }
    }
  
  def __calculate_variance(self, numbers: List[float]) -> float:
    variance = self.__driver_handler.variance(numbers)
    return variance
  
  def __calculate_multiplication(self, numbers: List[float]) -> float:
    multiplication = 1
    for num in numbers: multiplication *= num

    return multiplication
  
  def __verify_result(self, variance: float, multiplication: float) -> bool:
    if variance < multiplication:
      return HttpBadRequest("Variance é menor que a multiplicação")