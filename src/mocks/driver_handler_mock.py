from typing import List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 2.0
    
    def variance(self, numbers: List[float]) -> float:
        return 5.0
    
    def average(self, numbers: List[float]) -> float:
        return 3.0 