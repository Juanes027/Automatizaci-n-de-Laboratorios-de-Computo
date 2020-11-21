# Automatizaciòn de Laboratorios de Computo
En este repositorio se encuentra toda la implementaciòn de los scripts de automatizaciòn escritos en Python para la implementaciòn de laboratorio de computo

## Asegurar el usuario Root
Esto debería ser lo primero que debe hacer al configurar una instalación nueva del servidor Ubuntu. Normalmente, la configuración de una contraseña para el usuario root se realiza durante el proceso de instalación. Sin embargo, si alguna vez se encuentra en una posición en la que ha asumido la responsabilidad de un servidor Ubuntu, es mejor restablecer la contraseña teniendo en cuenta las mejores prácticas para contraseñas.

* No uses palabras en español
* Utilice una combinación de símbolos y caracteres alfanuméricos
* Longitud: según la probabilidad y las probabilidades de adivinar o descifrar una contraseña, puede proporcionar la mejor seguridad después de que una contraseña alcanza una cierta longitud. Más de diez caracteres es una buena práctica, pero incluso contraseñas más largas con caracteres complejos es una forma más segura de hacerlo.

También puede bloquear la contraseña del usuario root para evitar que nada se ejecute como root.

Dependiendo de su versión de Ubuntu, la cuenta de root puede estar deshabilitada, simplemente configurar o cambiar la contraseña de root la habilitará con lo siguiente.

`sudo passwd root`

Ahora podemos bloquear la cuenta de root bloqueando la contraseña con la bandera "-l" como se muestra a continuación. Esto evitará que se utilice al usuario root.

`sudo passwd -l root`

Para desbloquear la cuenta de root, nuevamente, simplemente cambie la contraseña de root para habilitarla.

`sudo passwd root`

## Mantener el sistema de archivos actualizado

Querrá asegurarse de que su servidor se mantenga actualizado con los últimos parches de seguridad. Si bien un servidor puede funcionar durante un tiempo sin mucho mantenimiento y las cosas “simplemente funcionarán”, querrá asegurarse de no adaptar una mentalidad de “configúrelo y olvídelo”.

Las actualizaciones periódicas en un servidor Ubuntu pueden garantizar que el sistema se mantenga seguro y actualizado. Puedes usar lo siguiente para hacer eso.

`sudo apt-get update`

## Agregar un usuario en el servidor usando el Script de Python

Para poder agregar usuarios al servidor Ubuntu creado se necesita tener instalado Python 3 en el servidor, sino se tiene instalado se puede usar la siguiente line de comando.

`sudo apt-get python3`

usa el siguiente comando para verificar si Python esta instalado.

`python3 --version`

Posterior a la instalaciòn se actualiza el sistema con la siguiente linea de comandos.

`sudo apt-get update`

¡Ya tenemos instalado Python 3 en nuestro servidor!, despues de esto puedes descargar el archivo `add_usuario.py` de este repositorio y ubicarte en la carpeta donde se encuentre guardado el archivo con el comando `cd (ubicaciòn)` y para ver todos los archivos de esta carpeta lo puedes hacer con el comando `ls`. Posteriormente a ya estar en la carpeta deseada se corre el Script con el siguiente comando. 

`sudo python3 add_usuario.py`


## Instalar un Firewall

De forma predeterminada, las versiones posteriores de Ubuntu deberían incluir un firewall sin complicaciones o UFW. Puede verificar si UFW está instalado con lo siguiente:

`sudo ufw status`

Eso devolverá un estado de activo o inactivo. Si no está instalado, puede instalarlo con:

`sudo ufw allow 80/tcp`

Eso será esencialmente lo mismo que permitir el servicio HTTP. Una vez que tenga los servicios que desea en la lista, puede habilitar el firewall con esto.


`sudo ufw enable`

Esto puede interrumpir la conexión SSH actual si así es como inició sesión, así que asegúrese de que su información sea correcta, para que no se desconecte.

Además, asegúrese de comprender bien quién realmente necesita acceso al servidor y solo agregue usuarios al sistema operativo Linux que realmente necesitan acceso.



`sudo apt-get install ufw`

Es una buena idea pensar en una lista de componentes que requerirán acceso a su servidor. ¿Se necesita acceso SSH? ¿Se necesita tráfico web? Deberá habilitar los servicios a través del firewall que se necesitan para que el tráfico entrante pueda acceder al servidor de la forma que desee.

En nuestro ejemplo, permitamos el acceso SSH y web.

`sudo ufw allow ssh`

`sudo ufw allow http`

Esos comandos también abrirán los puertos. Alternativamente, puede utilizar el método de puerto para permitir servicios a través de ese puerto específico.


