# Importa la biblioteca pandas
import pandas 

#NOTE: "The same data analysis exercise using the Pandas library to analyze and filter squirrel data in Central Park, but using object-oriented programming."


# Define la clase Calculate para realizar cálculos sobre los datos del censo de ardillas
class Calculate:
    
    # Define el método inicializador de la clase
    def __init__(self, color):
        
        # Lee el archivo CSV del censo de ardillas y almacena los datos en el atributo squirrel_information
        self.squirrel_information = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
        
        # Asigna el color recibido como argumento al atributo color
        self.color = color  
    
    
    # Define el método para obtener las filas y columnas que coinciden con el color especificado
    def get_rows_columns(self):
        
        # Filtra las filas del DataFrame que tienen el color especificado y las almacena en color_squirrel
        self.color_squirrel = self.squirrel_information[self.squirrel_information['Primary Fur Color'] == self.color]
        
        # Retorna el DataFrame con las filas que coinciden con el color
        return self.color_squirrel  
    
    
    # Define el método para obtener la columna 'Primary Fur Color' del DataFrame resultante
    def primary_fur_color_column(self):
        
        # Obtiene la columna 'Primary Fur Color' del DataFrame con las filas que coinciden con el color
        self.color_squirrel_column = self.color_squirrel['Primary Fur Color']
        
        # Retorna la columna 'Primary Fur Color'
        return self.color_squirrel_column  


    # Define el método para calcular el número de ardillas de un color específico
    def color_number(self):
        # Calcula el número de ardillas en la columna 'Primary Fur Color' del DataFrame
        self.number = self.color_squirrel_column.size
        
        # Retorna el número de ardillas del color especificado
        return self.number  



