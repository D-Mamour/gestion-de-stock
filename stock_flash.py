import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "",
    database = "inventaire"
)

if connection.is_connected():
    print("vous etes connecte dans la base de donnees challenge")

def ajouter_produit():
    """permet d'ajouter des produits"""

    with connection.cursor() as curseur:

        while True :
            designation = input("Designation : ").strip()
            if designation.isalpha():
                break
            print("designation invalide, veuillez entrer un desigation valide")
        
        categorie = input("Categorie : ").strip()

        while True : 
            prix_unitaire = input("Prix Unitaire : ")
            if prix_unitaire.isnumeric():
                break
            print("prix unitaire invalide, veuillez entrer un prix unitaire valide")

        while True : 
            quantite = input("Quantite : ")
            if quantite.isnumeric():
                break
            print("quantite invalide, veuillez entrer un quantite valide")
        
        sql = """
            insert into produits (designation, categorie, prix_unitaire, quantite)
            values (%s, %s, %s, %s)
            """
        curseur.execute(sql, (designation, categorie, prix_unitaire, quantite))
        connection.commit()

def liste_des_produits():
    """permet de lister toutes les produits"""

    with connection.cursor(dictionary=True) as curseur:
        sql = "select * from produits"
        curseur.execute(sql)

# [(1, 'pomme', 'alimentaire', 10, Decimal('350.00'), 1),]
# 1: pomme - alimentaire - 10 - 350.00 - 1
# lister[1]

        for lister in curseur.fetchall():
            # print(f"{lister[0]} : {lister[1]} - {lister[2]} - {lister[3]} - {lister[4]} - {lister[5]}")
            print(f"{lister["id"]} : {lister["designation"]} - {lister["categorie"]} - {lister["quantite"]} - {lister["prix_unitaire"]} - {lister["disponibilite"]}")
            # print(lister)

def mise_a_jour():
    """Mettre a jour la quantite d'un produit"""
    global trouve
    with connection.cursor() as curseur:
        liste_des_produits()
        id = "select id from produits "
        curseur.execute(id)
        resultat = curseur.fetchall()
        
        while True:
            trouve = False
            produit = int(input("ID produit : "))
            for e in resultat:
                if produit == e[0]:
                    trouve = True
            if trouve == True:
                print ("ID valide")
                break
     
            
        while True:
            qte = input("Nouvelle quantite : ")
            if qte.isnumeric():
                break

        sql = "update produits set quantite = %s WHERE id = %s"
        curseur.execute(sql, (qte, produit))
        connection.commit()

        print("Stock mis a jour")


def recherche_produit():
    """Permet de rechercher un produit"""

    with connection.cursor() as curseur:

        mot = input("Mot a rechercher : ").strip()

        sql = """
            select id, designation, categorie, quantite, prix_unitaire
            from produits
            where designation like %s
            or categorie like %s
        """

        s = f"%{mot}%"
        curseur.execute(sql, (s, s))

        resultats = curseur.fetchall()

        if not resultats:
            print("Aucun produit trouve")
            return

        for pdt in resultats:
            print(f"Resultat recherche : {pdt}")

def supprimer_un_produit():
    """permet la suppression d'un produit"""

    with connection.cursor() as curseur:
        liste_des_produits()

        while True:
            produit_id = input("veuillez entrer le numero du produit a supprimer : ")
            if produit_id.isnumeric():
                break
            print("veuillez saisir un nombre")
        
        sql = "delete from produits where id = %s"
        curseur.execute(sql,(produit_id,))
        connection.commit()

        print("Produit supprime") 

def visualisation():

    with connection.cursor() as curseur:

        print("""
        1. Produit le plus cher
        2. Valeur totale du stock
        3. Nombre de produits par categorie
        """)

        choix = input("Choix : ")

        if choix == "1":
            sql = """
                SELECT designation, prix_unitaire
                FROM produits
                ORDER BY prix_unitaire DESC
                LIMIT 1
            """

            curseur.execute(sql)
            resultat = curseur.fetchone()

            if resultat:
                designation, prix = resultat
                print(f"Produit le plus cher : {designation} — {prix}")
            else:
                print("Aucun produit trouvé")


        elif choix == "2":
            sql = ("""
                select SUM(prix_unitaire * quantite)
                from produits
            """)
            curseur.execute(sql)
            total = curseur.fetchone()[0]
            print(f"Valeur totale : {total} FCFA")


        elif choix == "3":
            sql = ("""
                select categorie, count(*)
                from produits
                group by categorie
            """)
            curseur.execute(sql)

            for nombre_produits in curseur.fetchall():
                print(nombre_produits)


def menu():    
    while True:
        print("\n-------------------- MENU --------------------")
        
        print("""
            1. Ajouter un produit
            2. Lister l'inventaire
            3. Mettre a jour le stock
            4. Rechercher un produit
            5. Supprimer un produit 
            6. Visualisation 
            7. Quitter
            """)
        
        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_produit()

        elif choix == "2":
            liste_des_produits()

        elif choix == "3":
            mise_a_jour()

        elif choix == "4":
            recherche_produit()

        elif choix == "5":
            supprimer_un_produit()

        elif choix == "6":
            visualisation()

        elif choix == "7":
            print("Fin du programme")
            break

        else:
            print("Choix invalide veuillez reessayer")   

menu() 
connection.close()