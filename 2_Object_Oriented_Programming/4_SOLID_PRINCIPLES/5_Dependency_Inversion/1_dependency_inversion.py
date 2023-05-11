# ======================================================================
#                    Dependency Inversion Principle
# ======================================================================
# The dependency inversion principle states that: 
# High-level modules should not depend on low-level modules. 
# Both should depend on abstractions. 
# Abstractions should depend on details. Details should depend on abstractions.
# The dependency inversion principle aims to reduce the couping between 
# classes by creating an abstraction layer between them.

from abc import ABC

class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount):
        pass
    
class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount):
        print('Converting currency using FX API.')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2

class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount):
        print('Converting currency using FX API.')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.16

class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)

converter = FXConverter()
converter2 = AlphaConverter()
app = App(converter)
app2 = App(converter2)
app.start()
app2.start()