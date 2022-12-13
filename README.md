# pymigration-bookwyrm (ESP)

(English version below)

Este script de python está diseñado para favorecer la migración desde una instancia de Bookwyrm a otra.

---

## Requisitos

- Python
- Pandas (si tienes python instalado se puede instalar con 'pip install pandas')


## Instrucciones

Tras descargar este script, lo primero que hay que hacer es exportar los datos de Bookwyrm de la instancia desde la que se quiere migrar (en configuración -> exportación en csv -> descargar archivo). Se renombra este archivo csv como BW.csv. Se ejecuta el script y se generará un nuevo archivo con el nombre BWnew.csv.

En el archivo csv que exporta bookwyrm falta información que es necesaria para que se pueda importar toda la información correctamente. Los campos que faltan son la estanteria y la fecha de lectura. Este script incluye todos los libros que han sido puntuados en la estantería de libros leídos (read) y les añade una fecha de lectura. Los libros sin valoraciones se incluyen en la estantería de libros por leer (to-read).

Si se quiere incluir la fecha exacta de lectura habría que modificar a mano el archivo csv, indicando para cada libro la fecha en la columna 'Date Read' y con formato yyyy/mm/dd (p.ej. 2022/12/13).

Tras realizar estas modificaciones en el archivo BWnew.csv ya estaría listo para ser importado en la nueva instancia de bookwyrm a la que se quiere migrar. La importación se hace en configuración -> importar, como fuente de datos hay que seleccionar Goodreads (csv).


## Agradecimientos

Este script ha sido escrito para facilitar la migración a https://lectura.social/, instancia que ha soportado numerosas pruebas para comprobar el correcto funcionamiento del archivo csv generado.

---

# pymigration-bookwyrm (EN)

This python script is designed to support migration from one instance of Bookwyrm to another.

---

## Requirements

- Python
- Pandas (if you have python installed it can be installed with 'pip install pandas')


## Instructions

After downloading this script, the first thing to do is to export the Bookwyrm data of the instance you want to migrate from (in configuration -> csv export -> download file). Rename this csv file as BW.csv. Run the script and a new file will be generated with the name BWnew.csv.

The csv file exported by bookwyrm is missing information that is necessary to be able to import all the information correctly. The missing fields are the shelf and the date of reading. This script includes all books that have been rated in the read shelf and adds a read date to them. Books without ratings are included in the to-read shelf.

If you want to include the exact date of reading, you would have to modify the csv file by hand, indicating the date in the 'Date Read' column for each book in the format yyyy/mm/dd (e.g. 2022/12/13).

After making these modifications to the BWnew.csv file, it is ready to be imported into the new instance of bookwyrm to which you want to migrate. The import is done in configuration -> import, as data source you have to select Goodreads (csv).

## Acknowledgements

This script has been written to facilitate the migration to https://lectura.social/, which has supported numerous tests to check the correct functioning of the generated csv file.
