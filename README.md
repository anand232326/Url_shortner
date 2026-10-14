                Client / Web Browser 
                          │
                          ▼ (GET /{short-url})
               [ Load Balancer (Orange Block) ]
                          │
                          ▼
               [ Web Servers Cluster (Green Blocks) ]
                     │                       │
      (Step 2: Check Cache)        (Step 3: Query DB on Miss)
                     ▼                       ▼
       [ Distributed Cache (Red) ]   [ Relational Database (Blue) ]
       (Redis / Memcached)           (PostgreSQL / MySQL)
                     │                       │
                     └───────────┬───────────┘
                                 │
                                 ▼ (Step 4: 301 Permanent Redirect)
                           [ Client Browser ]




D:\django\
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── nginx\
│   └── nginx.conf
├── url_shortner\
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── polls\
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations\
    │   └── 0001_initial.py
    └── templates\
        └── polls\
            └── index.html