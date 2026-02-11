
# Projet — Application Console de Gestion d’Inventaire (Python + MySQL)

## Description

Cette application est un programme Python en ligne de commande permettant de gérer un inventaire de produits stockés dans une base de données MySQL.  
Elle propose les opérations essentielles : ajout, consultation, mise à jour, recherche, suppression et visualisation statistique des produits.

Le projet est basé sur **Python** et le connecteur **mysql-connector-python**.

---

## Fonctionnalités

- Ajout de produits avec validation des entrées
- Liste complète de l’inventaire
- Mise à jour de la quantité en stock
- Recherche de produits par désignation ou catégorie
- Suppression d’un produit
- Visualisations :
  - Produit le plus cher
  - Valeur totale du stock
  - Nombre de produits par catégorie
- Menu interactif en boucle

---

## Structure des Données

Base de données utilisée : `inventaire`

Table principale : `produits`

Exemple de structure compatible :

CREATE TABLE produits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    designation VARCHAR(100) NOT NULL,
    categorie VARCHAR(100) NOT NULL,
    prix_unitaire DECIMAL(10,2) NOT NULL,
    quantite INT NOT NULL,
    disponibilite BOOLEAN DEFAULT TRUE
);

---

## Prérequis

- Python 
- MySQL Server
- mysql-connector-python

Installation du connecteur :

pip install mysql-connector-python

---

## Configuration

Modifier les paramètres de connexion si nécessaire dans le script :

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventaire"
)

Vérifier que :

- le serveur MySQL est actif
- la base `inventaire` existe
- la table `produits` est créée

---

## Lancement du Programme

Exécuter le script :

python nom_du_fichier.py

Le menu interactif s’affiche automatiquement.

---

## Menu Principal

1. Ajouter un produit  
2. Lister l'inventaire  
3. Mettre a jour le stock  
4. Rechercher un produit  
5. Supprimer un produit  
6. Visualisation  
7. Quitter

---

## Règles de Validation Implémentées

- La désignation doit être alphabétique
- Le prix unitaire doit être numérique
- La quantité doit être numérique
- Les identifiants produits doivent être numériques
- Les requêtes SQL utilisent des paramètres pour limiter les risques d’injection SQL

---

## Améliorations Possibles

- Interface graphique (Tkinter / Web)
- Gestion des utilisateurs
- Historique des mouvements de stock
- Export CSV / Excel
- Gestion des alertes de stock faible
- Tests unitaires

---

## Objectif Pédagogique

Ce projet illustre :

- Connexion Python ↔ MySQL
- Requêtes SQL paramétrées
- Organisation d’un programme procédural
- Validation des entrées utilisateur
- Menu interactif en ligne de commande

---

## Auteur

Projet de gestion d’inventaire — Python & MySQL
