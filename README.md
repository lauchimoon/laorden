# La Orden scripts

## Clonar
```
$ git clone https://github.com/laurenL12/laorden.git
$ cd laorden/
$ mkdir out/
```
El directorio `out/` es requerido ya que es allí donde se generan los clips e imagenes.

## Generar tabla de precios
Los precios dependen del excel `data.xlsx`. Las imagenes generadas saldrán como resultado en el directorio `out/`
```
$ python3 gen-prices-1.py
$ python3 gen-prices-2.py
```

## Generar clips
Los clips se generan en `out/` bajo el nombre `clip.mp4`. Se requiere la tabla de precios generada de antemano.
```
$ python3 gen-video.py
```
