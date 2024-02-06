# Crea una instancia de la clase Calculate para calcular el número de ardillas grises
calculate_gray = Calculate(color="Gray")
# Llama al método get_rows_columns para obtener las filas y columnas que coinciden con el color gris
calculate_gray.get_rows_columns()
# Llama al método primary_fur_color_column para obtener la columna 'Primary Fur Color'
calculate_gray.primary_fur_color_column()
# Calcula el número de ardillas grises
gray_number = calculate_gray.color_number()

# Crea una instancia de la clase Calculate para calcular el número de ardillas canela
calculate_cinnamon = Calculate(color="Cinnamon")
# Llama al método get_rows_columns para obtener las filas y columnas que coinciden con el color canela
calculate_cinnamon.get_rows_columns()
# Llama al método primary_fur_color_column para obtener la columna 'Primary Fur Color'
calculate_cinnamon.primary_fur_color_column()
# Calcula el número de ardillas canela
cinnamon_number = calculate_cinnamon.color_number()

# Crea una instancia de la clase Calculate para calcular el número de ardillas negras
calculate_black = Calculate(color="Black")
# Llama al método get_rows_columns para obtener las filas y columnas que coinciden con el color negro
calculate_black.get_rows_columns()
# Llama al método primary_fur_color_column para obtener la columna 'Primary Fur Color'
calculate_black.primary_fur_color_column()
# Calcula el número de ardillas negras
black_number = calculate_black.color_number()

# Imprime el número de ardillas negras
print(black_number)