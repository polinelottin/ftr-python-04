from typing import Dict
from flask import Request
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity

class Calculator1:
    def calculate(self, request: Request) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        splitted_number = input_data / 3

        first_step_result = self.__first_step(splitted_number)
        second_step_result = self.__second_step(splitted_number)

        result = first_step_result + second_step_result + splitted_number
        return self.__format_response(result)
    
    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntity("Body mal formatado")
        
        input_data = body["number"]
        return input_data
    
    def __first_step(self, number: float) -> float:
        first_step = (number / 4) + 7
        second_step = (first_step ** 2) * 0.257
        return second_step
    
    def __second_step(self, number: float) -> float:
        first_step = (number ** 2.121)
        second_step = (first_step / 0.5) +1
        return second_step
    
    def __format_response(self, result: float) -> Dict:
        return {
            "data": {
                "Calculator": "1",
                "result": round(result, 2),
                "success": True,
            }
        }