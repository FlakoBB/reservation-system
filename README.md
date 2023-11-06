<h1 align='center'>Sistema de Reservas para Espacios de Coworking</h1>

<p>
   Sistema de reservas para un espacio de coworking que permita a los usuarios reservar escritorios y salas de reuniones. El sistema debe ser capaz de gestionar múltiples usuarios, espacios y reservas simultáneas.
</p>

**Requisitos Funcionales:**

1. **Autenticación y Permisos:**
    - Los usuarios deben poder registrarse e iniciar sesión.
    - Los usuarios deben tener diferentes roles (administrador y usuario regular).
    - Solo los administradores pueden agregar nuevos espacios de coworking.
2. **Espacios de Coworking:**
    - Los administradores pueden agregar, editar y eliminar espacios de coworking.
    - Cada espacio debe tener información como nombre, ubicación y capacidad.
3. **Reservas de Escritorios:**
    - Los usuarios pueden ver la disponibilidad de escritorios en un espacio de coworking.
    - Los usuarios pueden reservar un escritorio para un día específico.
4. **Reservas de Salas de Reuniones:**
    - Las salas de reuniones deben tener una capacidad definida.
    - Los usuarios pueden ver la disponibilidad de salas de reuniones.
    - Los usuarios pueden reservar una sala de reuniones para un día y hora específicos.
5. **Calendario y Recordatorios:**
    - Los usuarios deben tener un calendario que muestre sus reservas.
    - Se deben enviar recordatorios por correo electrónico a los usuarios antes de sus reservas.
6. **Historial de Reservas:**
    - Los usuarios pueden ver su historial de reservas pasadas y futuras.
    - Los administradores pueden ver el historial de reservas de todos los usuarios.

**Requisitos Técnicos:**

1. **Django API:**
    - Utiliza Django para construir una API RESTful.
2. **Base de Datos:**
    - Utiliza una base de datos para almacenar información sobre usuarios, espacios, y reservas.
3. **Autenticación JWT:**
    - Implementa la autenticación usando tokens JWT.
4. **Documentación API:**
    - Crea documentación clara para la API utilizando herramientas como Swagger o ReDoc.
5. **Pruebas Unitarias:**
    - Escribe pruebas unitarias para al menos el 80% del código.