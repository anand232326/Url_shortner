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