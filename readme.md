Este repositorio muestra un proyecto en el que se busca obtener un ranking de una partida de un juego shooter donde se tiene en cuenta unn sistema de puntuacion 
basado en kill = 3 puntos, death = -1 punto y assist = 1 punto. se muestran las diferentes rondas simuladas y se obtiene el ranking de los jugadores al final de la partida.

el analisis y resultado final del proyecto se encuentra en la carpeta Notebooks donde se encunetra el codigo main que procesa las rondas y genera el ranking final
en una funcion que se encuentra en la carpeta src/funciones.py 


ENTORNO VIRTUAL VENV=

este proyecto incluye un entorno virtual para su ejecucion el cual se encuentra en la carpeta venv,venv es una herramienta que sirve para crear entornos virtuales,
la cual se puede crear introduciendo en la terminal el siguiente comando: 

                                                 python -m venv venv

esto crea una carpeta con diferentes elementos, el venv viene incluido en python por defecto. una vez creada esta carpeta se debe activar el entorno virtual
para ello se debe ejecutar el siguiente comando en la terminal:

                                                 venv\Scripts\activate

en el caso de windows se usa ../Scripts/.. la cual esta puede cambiar de nombre depende en cual SO se encuentre, en el caso de linux o mac se usa venv/bin/activate.
este entorno virtual permite instalar las librerias necesarias para el correcto funcionamiento del proyecto sin afectar a otras aplicaciones o proyectos existentes


si este se quiere desactivar se debe ejecutar el siguiente comando en la terminal:

                                                 deactivate


una vez activado el entorno virtual se deben instalar las librerias necesarias para el correcto funcionamiento del proyecto
para ello se debe ejecutar el siguiente comando en la terminal:

                                                 pip install -r requirements.txt


JUPYTER NETBOOK= 

este repositorio incluye tambien un jupyter notebook el cual permite ejecutar el codigo de una manera mas interactuable y visual
para ello se debe instalar la libreria jupyter, la cual en la terminal se debe ejecutar el siguiente comando:

                                                 pip install jupyter

una vez instalada la libreria se debe ejecutar el siguiente comando en la terminal:

                                                    jupyter notebook

para abrirlo en la web si se quiere abrir en el navegador, o se puede abrir directamente desde la carpeta donde se encuentra el archivo .ipynb


una vez abierto el jupyter notebook se puede ejecutar el codigo de una manera mas visual y interactuable
ademas de poder ver los resultados de cada celda de manera mas clara

el proyecto se puede ejecutar sobre el archivo "main.py" en la carpeta src que contiene sus respectivas funciones y en el archivo "main.ipynb"
que contiene el mismo codigo pero en un jupyter notebook(para esto se tienen las intrucciones anteriormente dichas).

##REPASANDO##
las instrucciones para la ejecucion del proyecto:
crear el entorno virtual:
                                                 python -m venv venv

activar el entorno virtual:
                                                    venv\Scripts\activate  


instalar las librerias necesarias:
                                                    pip install -r requirements.txt 


si se quiere ejecutar el proyecto desde la terminal:
                                                    python src/main.py

si se quiere ejecutar el proyecto desde el jupyter notebook:
instalar jupyter notebook:

                                                    pip install notebook

abrir el jupyter notebook:

                                                    jupyter notebook
                                                    
una vez abierto el jupyter notebook se puede ejecutar el codigo de una manera mas visual y interactuable



