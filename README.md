# prueba-enviexpress
Prueba tecnica con Python, PHP, MySQL

## Se crea un directorio sql
- Este contiene un script que permitira crear la base de datos y agregar las tabla de TB_PEDIDOS_ELIMINADOS

## Se crea un workflow
- Este sirve para poder ejecutar mysql desde github y todas sus variables y configuraciones estan en mysql.yml

### Archivo Gitignore
Se agrega un archivo gitignore que sea capaz mantener el repositorio limpio de las opciones que se agreguen el entorno virtual y demas compilaciones

### Archivo Requirements
El archivo requirements.txt tiene como objetivo listar todas las librerias usadas en el entorno virtual que se usa de forma local

## Creacion y ejecucion del proyecto
- Luego de clonado el repositorio. Abrir una terminal y navegar hasta el directorio back
``` 
cd back 
```
- Crear un entorno virtual 
```
python -m venv env
```
- Ejecutar el entorno virtual
    - si es Linux o MacOS
    ``` 
    source env/bin/activate 
    ```
    -si es Windows
    ``` 
    env\Scripts\activate 
    ```
- Una vez activado el entorno virtual ejecutar el siguiente comando
``` 
pip install -r requirements.txt
```
- Poner en marcha el servidor
```
uvicorn main:app --reload
```
- Abrir el archivo index.html en un navegador este se encuentra en el directorio front

## .env.example

El archivo ``` .env.example ``` sirve como ejemplo de las variables de entorno usadas asi que si se copia y se renombra quitando ``` .example ``` y cambiando las variables en su interior por las propias, crea un enlace con el entorno local y las funciones del puestas en ``` back/src/database.py ```