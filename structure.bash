auth-service
│
├── app
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── services.py
│   ├── auth.py
│   ├── dependencies.py
│   └── routers
│        └── auth.py
│
├── tests
├── requirements.txt
└── README.md




## ✅ Separation of Concerns

| File              | Responsibility |
| ----------------- | -------------- |
| `security.py`     | hashing + JWT  |
| `services.py`     | business logic |
| `routers/auth.py` | API endpoints  |


Step1 - Create database.py write code in it.
Step2 - Create user Model/models.py write code in it.
Step3 — Create Schemas.py, write code in it.
Step4 — Password Hashing, Create security.py, write code in it. 
Step5 - JWT Tokens/ Create in routers/auth.py, write code in it.
Step6 — User Logic/ services.py, write code in it.
Step7 - Create routers in routers/auth.py, write code in it.
Step8 — Main App, write code in it.