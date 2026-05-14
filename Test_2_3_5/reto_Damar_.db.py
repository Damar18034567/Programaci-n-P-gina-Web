import sqlite3

DB_PATH = "/home/dviltru1803/Programación Projec./Test_2_3_5/reto_Damar_.db"

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Crear tabla LOGS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS LOGS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        evento TEXT NOT NULL
    )
    """)

    # 30 eventos inventados
    eventos = [
        "Usuario 'ana' inició sesión",
        "Usuario 'juan' cerró sesión",
        "Error: tiempo de espera en /api/data",
        "Archivo subido: imagen_123.png",
        "Backup automático completado",
        "Restauración iniciada",
        "Permiso denegado para usuario 'luis'",
        "Conexión a la base de datos establecida",
        "Conexión a la base de datos perdida",
        "Usuario 'maria' cambió contraseña",
        "Evento programado: limpieza de temporales",
        "Servicio de correo enviado a cliente_45",
        "Advertencia: espacio en disco bajo",
        "Actualización de configuración aplicada",
        "Nueva cuenta creada: usuario_78",
        "Eliminación de registro id=256",
        "Error 500 en /login",
        "Cache invalidado para ruta /home",
        "Cron job ejecutado: sincronizar",
        "Solicitud IP 192.0.2.5 bloqueada",
        "Sesión expirada para usuario 'ana'",
        "Token refrescado para api_client_3",
        "Migración de esquema completada",
        "Lectura de archivo config.yml fallida",
        "Generación de reporte mensual finalizada",
        "Notificación push enviada a usuario_12",
        "Reconexión automática realizada",
        "Prueba de correo fallida: smtp.timeout",
        "Límite de intentos de login excedido para 'pablo'",
        "Modo mantenimiento activado"
    ]

    # Insertar eventos
    cur.executemany("INSERT INTO LOGS (evento) VALUES (?)", [(e,) for e in eventos])

    conn.commit()
    conn.close()
    print(f"Base de datos creada en: {DB_PATH} con {len(eventos)} registros en LOGS")

if __name__ == "__main__":
    main()