# Disfrazate 🎃
Venta y Alquiler de disfraces

## Estructura de carpetas (editar luego)
```bash
disfrazate/
├── server/                   # Código y configuración del servidor backend
│   ├── app/                  # Aplicación principal
│   │   ├── controllers/      # Lógica para las rutas (controladores)
│   │   ├── models/           # Modelos de base de datos
│   │   ├── routes/           # Definición de rutas (endpoints)
│   │   ├── services/         # Servicios o lógica de negocio
│   │   ├── utils/            # Utilidades o helpers
│   │   └── __init__.py       # Archivo de inicialización de la aplicación
│   ├── config/               # Configuración de entorno
│   │   ├── database.py       # Conexión a la base de datos
│   │   └── .env              # Variables de entorno
│   ├── tests/                # Pruebas de backend
│   ├── requirements.txt      # Dependencias del backend
│   └── README.md             # Documentación del backend
│
├── client/                   # Código de la aplicación frontend (cliente)
│   ├── src/                  # Código fuente de la app frontend
│   │   ├── components/       # Componentes reutilizables
│   │   ├── pages/            # Vistas o páginas
│   │   ├── services/         # Servicios para llamar a la API
│   │   ├── styles/           # Estilos de la app (CSS, Sass, etc.)
│   │   ├── assets/           # Archivos estáticos (imágenes, fuentes, etc.)
│   │   ├── App.js            # Archivo principal de la app
│   │   └── index.js          # Punto de entrada de la app
│   ├── public/               # Archivos públicos de la app
│   ├── tests/                # Pruebas de frontend
│   ├── package.json          # Dependencias y scripts del frontend
│   └── README.md             # Documentación del frontend
│
├── mysql/                    # Configuración y datos de MySQL
│   ├── data/                 # Volumen de datos de MySQL
│   ├── init.sql              # Script de inicialización de MySQL (opcional)
│   └── my.cnf                # Configuración personalizada de MySQL (opcional)
│
├── docs/                     # Documentación general del proyecto
│   ├── api_documentation.md  # Documentación de la API
│   ├── architecture.md       # Documentación de arquitectura
│   └── design_guide.md       # Guía de diseño y estándares
│
├── .gitignore                # Archivos y carpetas a ignorar por Git
└── README.md                 # Documentación principal del proyecto
```
