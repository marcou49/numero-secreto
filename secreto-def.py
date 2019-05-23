import datetime
import json
import random

print("\n Muy buenas, bienvenid@ a este juego de adivinar el número secreto. \n Consigue unos de los tres mejores resultados y te llevaras una paletilla. \n De momento la cosa va así \n")

secreto = random.randint(1, 3)
intentos = 0

# pasamos la fecha al formato europeo solo con dia / mes / año
fecha = datetime.date.today()
hoy = fecha.strftime('%d-%b-%Y')


# creamos lista de resultados desde el archivo de texto
with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())


# ordenamos la lista de resultados por intentos pero solo guardamos los tres mejores resultados
new_score_list = sorted(score_list, key=lambda k: k['Intentos'])
del new_score_list[3:]

# generamos el dicionario desde la lista para mostrar los resultados en un listado ordenado
for score_dict in new_score_list:
    score_text = "{0} encontro en {1} intentos el {2}.".format(score_dict.get("Nombre"), str(score_dict.get("Intentos")), score_dict.get("Fecha"))
    print(score_text)

nombre = input("\n Empezemos. Cómo te llamas ")


while True:
    guess = int(input(" Pon un número del 1 al 30: "))
    intentos += 1

    if guess == secreto:
        score_list.append({"Intentos": intentos, "Fecha": hoy, "Nombre": nombre })

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Bingo efectivamente es " + str(secreto) + ". Lo encontraste en " + str(intentos) + " intentos \n")
        break

    elif guess > secreto:
        print("No, menos")

    elif guess < secreto:
        print("No, más")
