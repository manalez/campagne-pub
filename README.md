# 🚀 Campagne Publicitaire – Déploiement Flask + MySQL

Ce projet est une application web simple développée avec Flask et connectée à une base de données MySQL.  
Elle est containerisée avec Docker, déployée sur une instance EC2 (AWS), et automatisée avec un pipeline CI/CD via GitHub Actions.

---

## 🛠️ Technologies utilisées

- Python 3.10
- Flask
- MySQL 8
- Docker / Docker Compose
- GitHub Actions (CI/CD)
- AWS EC2 (déploiement cloud)

---

## 📁 Structure du projet

campagne-pub/
├── app.py
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
├── templates/
│ └── index.html
├── static/
│ └── style.css
└── .github/
└── workflows/
└── deploy.yml


---

## ⚙️ Déploiement

### 1. Lancer l'infrastructure localement (optionnel)

```bash
docker-compose up --build
