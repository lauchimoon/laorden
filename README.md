# La Orden scripts

## Clonar
```
$ git clone https://github.com/laurenL12/laorden.git
$ cd laorden/
$ pip install -r requirements.txt # Descarga los paquetes necesarios
```

## Generar imagenes y videos
```
$ python3 gen.py
```
El script `gen.py` depende de los directorios `burger/`, `banners/` y `sandwich/`.

El contenido generado pertenece al directorio `out/`, que se crea durante el proceso de generación de media.

## Modificar la información generada
La hoja de cálculo `data.xlsx` provee los precios e información de cada producto para generar las imagenes y videos.

Lo importante está en cambiar el precio; los otros campos no deberían ser alterados.
