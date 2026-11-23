# Foro de publicaciones con login y registro

Aplicación web hecha con **Flask + MySQL** donde los usuarios se registran, inician sesión y publican mensajes. Cada usuario puede editar y eliminar solo sus propias publicaciones.

## Características

- Registro e inicio de sesión con sesiones de Flask
- Contraseñas cifradas con **Bcrypt**
- Validación de formularios en el servidor (nombre, email, contraseña)
- Consultas parametrizadas (prevención de inyección SQL)
- Relación 1:N entre `users` y `posts`
- Arquitectura **MVC** con Blueprints (modelos, controladores, vistas)
- Pruebas unitarias de validaciones

## Tecnologías

Python · Flask · MySQL · PyMySQL · Flask-Bcrypt · python-dotenv · HTML/CSS

## Estructura

```
├── app.py
├── extensions.py
├── config/mysqlconnection.py
├── models/        (user.py, post.py)
├── controllers/   (auth_controller.py, posts_controller.py)
├── utils/validators.py
├── templates/
├── static/css/
├── tests/
└── schema.sql
```

## Instalación

```bash
git clone https://github.com/jesusbravo777/foro-flask-mysql.git
cd foro-flask-mysql
python -m venv venv
venv\Scripts\activate          # Windows  (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
```

1. Crea la base de datos ejecutando `schema.sql` en MySQL Workbench.
2. Copia `.env.example` a `.env` y completa tus datos de MySQL.
3. Ejecuta la app:

```bash
python app.py
```

Abre http://127.0.0.1:5000

## Pruebas

```bash
python -m unittest discover tests
```

## Despliegue

Incluye `Procfile` (`gunicorn app:app`) para desplegar en Railway con una base MySQL.

## Autor

Cristopher Orellana · [GitHub](https://github.com/jesusbravo777)
