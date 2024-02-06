# Create a CSV file called "squirel_count"

#Tthe dataframe should have 2 columns "Fur color" and "count" how many squirrels are of each color


import pandas

#TODO : importmaos la informacion del archivo
squirrel_information=pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")

def gray_color(squirrel_information):
    #de el dataframe obtenemos todas las filas y columnas donde Primary Fur Color es igual a Gray
    gray_squirel=squirrel_information[squirrel_information['Primary Fur Color']=="Gray"]

    #imprimimos este dataframe con la informacion filtrada para visualizar los datos
    print("filas y columnas donde el primaryfur color es gray")
    print(gray_squirel)

    #espacio en blanco
    print()

    #de gray_squirel obtenemos la columna de primary fur
    gray_squirel_column=gray_squirel['Primary Fur Color']

    #imprimimos esta serie para verificar que la informacion se filtro
    print("columna Primary fur color con solamente los valores de Gray")
    print(gray_squirel_column)

    #espacio en blanco
    print()

    #calculamos el numero de elementos en la columna
    print('calculamos el numero de elementos en la columna, que corresponderia al numero de gray color squirrel')
    print(gray_squirel_column.size)

    
    #TODO: guardamos el valor en una variable, correspondiente al numero de gray squirels
    gray_number=gray_squirel_column.size
    
    return gray_number


def Cinnamon_color(squirrel_information):
    #de el dataframe obtenemos todas las filas y columnas donde Primary Fur Color es igual a Cinnamon 
    cinnamon_squirel=squirrel_information[squirrel_information['Primary Fur Color']=="Cinnamon"]

    #imprimimos este dataframe con la informacion filtrada para visualizar los datos
    print("filas y columnas donde el primaryfur color es cinnamon")
    print(cinnamon_squirel)

    #espacio en blanco
    print()

    #de cinnamon_squirel obtenemos la columna de primary fur
    cinnamon_squirel_column=cinnamon_squirel['Primary Fur Color']


    #imprimimos esta serie para verificar que la informacion se filtro
    print("columna Primary fur color con solamente los valores de cinnamon")
    print(cinnamon_squirel_column)

    #espacio en blanco
    print()

    #calculamos el numero de elementos en la columna
    print('calculamos el numero de elementos en la columna, que corresponderia al numero de cinnamon color squirrel')
    print(cinnamon_squirel_column.size)

    
    #TODO: guardamos el valor en una variable, correspondiente al numero de cinnamon squirels
    cinnamon_number=cinnamon_squirel_column.size
    
    return cinnamon_number


def Black_color(squirrel_information):
    #de el dataframe obtenemos todas las filas y columnas donde Primary Fur Color es igual a black
    black_squirel=squirrel_information[squirrel_information['Primary Fur Color']=="Black"]

    #imprimimos este dataframe con la informacion filtrada para visualizar los datos
    print("filas y columnas donde el primaryfur color es black")
    print(black_squirel)

    #espacio en blanco
    print()

    #de black_squirel obtenemos la columna de primary fur
    black_squirel_column=black_squirel['Primary Fur Color']


    #imprimimos esta serie para verificar que la informacion se filtro
    print("columna Primary fur color con solamente los valores de black")
    print(black_squirel_column)

    #espacio en blanco
    print()

    #calculamos el numero de elementos en la columna
    print('calculamos el numero de elementos en la columna, que corresponderia al numero de cinnamon color squirrel')
    print(black_squirel_column.size)

    
    #TODO: guardamos el valor en una variable, correspondiente al numero de black squirels
    black_number=black_squirel_column.size
    
    return black_number


gray_color

# Black_color(squirrel_information
#             )


#TODO: creando a DATAFRAME de un diccionario
squirrel_colors={"fur Color": ["Gray", "Cinnamon", "Black Color"], "Count":[gray_color(squirrel_information), Cinnamon_color(squirrel_information), Black_color(squirrel_information)]}

squirrel_colors_dataframe=pandas.DataFrame.from_dict(squirrel_colors)

print(squirrel_colors_dataframe)

squirrel_colors_dataframe.to_csv('out.csv')

#TODO: Finally use the dataframe to create a CSV file
