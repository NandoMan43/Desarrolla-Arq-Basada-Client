# Sistema de Chat en Tiempo Real

## Descripción

Este proyecto implementa un sistema de chat en tiempo real que permite la comunicación instantánea entre múltiples usuarios utilizando una arquitectura distribuida. La aplicación incluye funcionalidades para establecer conexiones P2P (peer-to-peer), un balanceador de carga y servidores backend que manejan las solicitudes de los clientes. Este sistema es ideal para entornos donde la colaboración y la interacción rápida son esenciales.

## Montaje

### Estructura del Proyecto

La estructura básica del proyecto es la siguiente:

### Herramientas Utilizadas

- **Python 3**: Lenguaje de programación utilizado para desarrollar el sistema. Python se eligió por su simplicidad y la riqueza de sus bibliotecas para el manejo de sockets y la programación de redes.
- **Sockets**: Se utilizaron sockets de Python para establecer conexiones TCP entre los diferentes componentes del sistema, permitiendo la comunicación entre los clientes y los servidores.
- **Threading**: La biblioteca `threading` se empleó para manejar múltiples conexiones simultáneamente, asegurando que el sistema pueda servir a varios usuarios al mismo tiempo sin bloqueos.
- **Visual Studio Code**: Editor de código utilizado para desarrollar y probar el sistema.

## Explicación de su Operación

1. **Servidor Backend**:
   - Cada servidor backend está diseñado para escuchar en un puerto específico. Cuando un cliente se conecta, el servidor acepta la conexión, recibe solicitudes y envía respuestas de vuelta al cliente. 
   - Los servidores se ejecutan en puertos diferentes (por ejemplo, 8001, 8002, 8003) para permitir la escalabilidad y balanceo de carga.

2. **Balanceador de Carga**:
   - El balanceador de carga escucha en un puerto designado (por ejemplo, 8000) y acepta conexiones de los clientes. Utiliza un algoritmo de Round-Robin para distribuir las solicitudes entre los servidores backend disponibles. 
   - Esto permite que el sistema maneje un número elevado de conexiones simultáneas y mejora la eficiencia al prevenir la sobrecarga de un solo servidor.

3. **Clientes**:
   - Los clientes se conectan al balanceador de carga y envían mensajes que son redirigidos a uno de los servidores backend. 
   - En la variante P2P del cliente, se permite a los usuarios conectarse directamente entre sí para intercambiar mensajes, facilitando una comunicación más rápida y privada.

4. **Comunicación P2P**:
   - Cuando un cliente decide iniciar un modo P2P, puede conectarse a otro cliente en la red y enviar mensajes directamente, lo que reduce la latencia en la comunicación. 
   - El sistema está diseñado para permitir que varios clientes se conecten y se comuniquen sin la necesidad de un servidor centralizado.

## Instalación

Para ejecutar este sistema de chat, sigue estos pasos:

1. **Ejecuta los servidores backend: Abre varias terminales y ejecuta el siguiente comando en cada una**:
   ```bash
   python servidor.py O python Servidores.py
2. **Inicia el balanceador de carga: En una nueva terminal, ejecuta**:
   ```bash
   python distribucion.py
3. **Inicia los clientes: En diferentes terminales, ejecuta el cliente utilizando**:
   ```bash
   python cliente.py
4. **Para la funcionalidad P2P, ejecuta**:
   ```bash
   python cliente_2.py

## Conclusión

Este proyecto ha implementado con éxito un sistema de chat en tiempo real utilizando una arquitectura distribuida y conexiones P2P (peer-to-peer). La estructura del código permite la escalabilidad, el balanceo de carga, y una comunicación eficiente entre los clientes. 

Gracias a la flexibilidad que ofrece la combinación de Python, sockets y threading, el sistema es capaz de manejar múltiples conexiones simultáneas, lo que lo convierte en una solución ideal para aplicaciones de mensajería en tiempo real. Además, la opción de comunicación P2P ofrece un canal directo entre clientes, mejorando la privacidad y reduciendo la latencia.

Con esta aplicación, los desarrolladores pueden expandir la funcionalidad o adaptarla a entornos más complejos, permitiendo un fácil crecimiento y optimización en futuros desarrollos.
