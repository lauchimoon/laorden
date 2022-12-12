import os
import pandas as pd

import burger.gen as burger
import sandwich.gen as sandwich
import banners.gen as banners

if not os.path.exists('out/'):
    os.mkdir('out/')

excel = pd.ExcelFile('data.xlsx')
data_burger = pd.read_excel(excel, 'Burger')
data_sandwich = pd.read_excel(excel, 'Sandwich')
data_banners = pd.read_excel(excel, 'Banners')

BURGER = '1'
SANDWICH = '2'
BANNERS = '3'

def burger_all():
    burger.tv1(data_burger)
    burger.tv2()
    burger.tv3(data_burger)

def sandwich_all():
    sandwich.sandwich1(data_sandwich)
    sandwich.sandwich2(data_sandwich)
    sandwich.sandwich3(data_sandwich)
    sandwich.sandwich4(data_sandwich)
    sandwich.sandwich_video()

def banners_all():
    banners.banner1(data_banners)
    banners.banner2(data_banners)
    banners.banner3(data_banners)
    banners.banner4(data_banners)
    banners.banner5(data_banners)
    banners.banner6(data_banners)

print("¿Qué deseas generar?")
print("1. burger\n2. sandwich\n3. banners")
generate = input(">> ")
if generate == BURGER:
    print("¿Qué deseas generar de burger?")
    print("1. Imagen 1\n2. TV 1\n3. TV 2\n4. TV 3\n5. Todo")
    print("Puedes seleccionar varias opciones separando por comas. ej: 1,3,5")

    valid = ['1', '2', '3', '4', '5']
    opt = input(">> ")
    split = opt.split(',')
    if not opt:
        print("No has hecho nada. Adios")

    for elem in split:
        if elem not in valid:
            print(f"{elem} no se encuentra dentro de las opciones.")
            break

        match elem:
            case '1': burger.burger1(data_burger)
            case '2': burger.tv1(data_burger)
            case '3': burger.tv2(data_burger)
            case '4': burger.tv3(data_burger)
            case '5': burger_all()

elif generate == SANDWICH:
    print("¿Qué deseas generar de sandwich?")
    print("1. Imagen 1\n2. Imagen 2\n3. Imagen 3\n4. Imagen 4\n5. Video\n6. Imagenes\n7. Todo")
    print("Puedes seleccionar varias opciones separando por comas. ej: 1,3,5")

    valid = ['1', '2', '3', '4', '5', '6', '7']
    opt = input(">> ")
    split = opt.split(',')
    if not opt:
        print("No has hecho nada. Adios")

    for elem in split:
        if elem.strip() not in valid:
            print(f"{elem} no se encuentra dentro de las opciones.")
            break

        match elem:
            case '1': sandwich.sandwich1(data_sandwich)
            case '2': sandwich.sandwich2(data_sandwich)
            case '3': sandwich.sandwich3(data_sandwich)
            case '4': sandwich.sandwich4(data_sandwich)
            case '5': sandwich.sandwich_video(data_sandwich)
            case '6':
                sandwich.sandwich1(data_sandwich)
                sandwich.sandwich2(data_sandwich)
                sandwich.sandwich3(data_sandwich)
                sandwich.sandwich4(data_sandwich)
            case '7': sandwich_all()

elif generate == BANNERS:
    print("¿Qué deseas generar de banners?")
    print("1. Imagen 1\n2. Imagen 2\n3. Imagen 3\n4. Imagen 4\n5. Imagen 5\n6. Imagen 6\n7. Todo")
    print("Puedes seleccionar varias opciones separando por comas. ej: 1,3,5")

    valid = ['1', '2', '3', '4', '5', '6', '7']
    opt = input(">> ")
    split = opt.split(',')
    if not opt:
        print("No has hecho nada. Adios")

    for elem in split:
        if elem.strip() not in valid:
            print(f"{elem} no se encuentra dentro de las opciones.")
            break

        match elem:
            case '1': banners.banner1(data_sandwich)
            case '2': banners.banner2(data_sandwich)
            case '3': banners.banner3(data_sandwich)
            case '4': banners.banner4(data_sandwich)
            case '5': banners.banner5(data_sandwich)
            case '6': banners.banner6(data_sandwich)
            case '7': banners_all()

else:
    if not generate:
        print("No has hecho nada. Adios")
        exit(0)

    print(f"{generate} no se encuentra dentro de las opciones. Adios")

