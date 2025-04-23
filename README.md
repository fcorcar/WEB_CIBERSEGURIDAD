# 🔐 WEB_CIBERSEGURIDAD

Bienvenido a **WEB_CIBERSEGURIDAD**, un proyecto web desarrollado con **HTML**, **CSS** y **Python Flask**. El objetivo de esta aplicación es explorar principios básicos y avanzados de ciberseguridad web, creando una base para experimentar con buenas prácticas, autenticación, y más.

> 📌 *Desarrollado por [Fran Cortés](https://github.com/fcorcar)*

---

## 🚀 Tecnologías utilizadas

- HTML5
- CSS3
- Python 3.x
- Sqlite3
- Flask 🔥
- Jinja2 (para plantillas)
- Entorno virtual `.venv`

---

## 📁 Estructura del proyecto

```bash
WEB_CIBERSEGURIDAD/
├── static/           
├── templates/          
├── app.py     
├── base_datos.py   
├── enviar_correo.py  
├── settings.py   
├── noticias_semalanes.db        
├── .venv/              
├── .env                
├── .gitignore
└── README.md
```

---

## ⚙️ Cómo ejecutar este proyecto

1. Clona el repo:
   ```bash
   git clone https://github.com/fcorcar/WEB_CIBERSEGURIDAD.git
   cd WEB_CIBERSEGURIDAD
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la app Flask:
   ```bash
   flask run
   ```

5. Abrir el navegador en `http://127.0.0.1:5000`

---

## 📌 Variables de entorno

Crea un archivo `.env` en la raíz con contenido como:

```env
DB=nombreBaseDatos
MJ_API_KEY=key
MJ_API_SECRET=apiSecret
EMAIL=emailQueEnviaLosCorreos
```

> Asegurate de que `.env` esté listado en `.gitignore`.

---

## 🌟 Sobre el autor

Soy **Fran Cortés**, apasionado del desarrollo web y la ciberseguridad. Este proyecto es parte de mi camino de aprendizaje para construir aplicaciones seguras y eficientes con Python.

- 🧑‍💻 GitHub: [fcorcar](https://github.com/fcorcar)

---

> “La seguridad no es un producto, es un proceso.” – Bruce Schneier
