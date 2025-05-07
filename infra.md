# Infrastructure utilisée (IaC simplifiée)

## Plateforme cloud
AWS (Amazon Web Services) – Instance EC2 (Ubuntu 24.04)

# Services utilisés
- EC2 : héberge l'application Dockerisée
- Sécurité : Groupe avec ports 22 (SSH) et 80 (HTTP) ouverts
- Clé SSH : campagne-key.pem

## Déploiement
Déploiement effectué manuellement :
1. Création de l'instance EC2 via AWS Console
2. Connexion SSH à l’instance
3. Installation de Docker & Docker Compose
4. Envoi des fichiers avec `scp`
5. Démarrage des conteneurs avec `docker-compose`

## Configuration
Les variables de connexion à MySQL sont passées via `docker-compose.yml` :

```yaml
  environment:
    - DB_HOST=db
    - DB_USER=root
    - DB_PASSWORD=rootpass
    - DB_NAME=campagne
