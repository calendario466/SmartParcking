class SmartParkingError(Exception): 
class ErrorValidacion(SmartParkingError): pass
class ErrorStock(SmartParkingError): pass
class ErrorPago(SmartParkingError): pass
