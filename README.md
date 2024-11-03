# Application de Gestion des Tâches

## Table des Matières

1. [Introduction](#introduction)
2. [Conception](#Conception) 
3. [Fonctionnalités](#fonctionnalités)
4. [Technologies Utilisées](#technologies-utilisées)
5. [Configuration du Projet](#configuration-du-projet)
6. [Utilisation](#utilisation)
7. [Points de Terminaison de l'API](#points-de-terminaison-de-lapi)
8. [Aperçu des Composants](#aperçu-des-composants)
9. [Style et Design](#style-et-design)
10. [Gestion des Erreurs](#gestion-des-erreurs)
11. [Démonstration](#Démonstration)
12. [Améliorations Futures](#améliorations-futures)

## 1. Introduction

Cette application de gestion des tâches est un outil web conçu pour aider les utilisateurs à gérer efficacement leurs tâches. Les utilisateurs peuvent créer, modifier, supprimer et mettre à jour le statut de leurs tâches. L'application fournit une interface claire et conviviale construite avec React et intégrée à une API RESTful.
## 2. Conception 
lien de conception avec Figma :`https://www.figma.com/design/HPLZuMGFWywBh2XGxpObPy/Untitled?node-id=0-1&t=bGfUahAe74FtYy4m-1`

## 3. Fonctionnalités

- **Création de Tâches** : Les utilisateurs peuvent créer de nouvelles tâches en fournissant les détails nécessaires.
- **Modification de Tâches** : Les utilisateurs peuvent modifier des tâches existantes pour mettre à jour leurs informations.
- **Suppression de Tâches** : Les utilisateurs peuvent supprimer des tâches avec une demande de confirmation.
- **Mise à Jour du Statut des Tâches** : Les utilisateurs peuvent mettre à jour le statut des tâches (À faire, En cours, Fait).
- **Notifications Toast** : Les utilisateurs reçoivent des notifications pour les actions effectuées (messages de succès ou d'erreur).

## 4. Technologies Utilisées

- **Frontend** : 
  - React
  - Axios (pour les requêtes HTTP)
  - React Toastify (pour les notifications)

- **Backend** : 
  - Django
  - API RESTful

## 5. Configuration du Projet

### Prérequis

Assurez-vous d'avoir installé les dépendances nécessaires avant de commencer. 

### Installation

1. Clonez le dépôt :</br>
`git clone https://github.com/RACHADDOUlFIKAR/TasksManager`</br>
`git clone https://github.com/RACHADDOUlFIKAR/Tasks-Manager-front`
  
3. Accédez au répertoire du projet :
`cd TaskManagerBack`
`cd taskmanager-frontend`
4. Installez les dépendances :
`  npm install (pour le front) `
`  activer l'environnement pour le back `


## 6. Utilisation 

`npm start  (pour le front)`
python manage.py runserver (pour le back) `
Pour démarrer l'application, exécutez la commande suivante :

Accédez à l'application via `http://localhost:3000`.

## 7. Points de Terminaison de l'API

- **GET** `/api/taches` : Récupérer toutes les tâches.
- **POST** `/api/taches` : Créer une nouvelle tâche.
- **PUT** `/api/taches/:id` : Mettre à jour une tâche existante.
- **DELETE** `/api/taches/:id` : Supprimer une tâche.
![Capture d'écran 2024-11-03 181225](https://github.com/user-attachments/assets/d18fd8ab-357f-42e6-a53f-58ae608a1ae4)

## 8. Aperçu des Composants

- `TaskList` : Composant pour afficher la liste des tâches.
- `TaskForm` : Composant pour ajouter ou modifier une tâche.

## 9. Style et Design

L'application utilise des styles modernes avec une mise en page réactive pour une meilleure expérience utilisateur. Vous pouvez personnaliser les styles dans le fichier `App.css`.

## 10. Gestion des Erreurs

Les erreurs sont gérées avec des messages de notification clairs pour guider l'utilisateur sur les actions nécessaires. Assurez-vous de gérer les erreurs côté serveur également pour fournir des retours appropriés.

## 11. Démonstration


https://github.com/user-attachments/assets/c7f9d5fc-467e-44d6-9861-62306c86f0f8



## 12. Améliorations Futures

- Ajouter une fonctionnalité de filtrage des tâches.
- Intégrer l'authentification des utilisateurs.
- Améliorer le style et la réactivité de l'interface utilisateur.
