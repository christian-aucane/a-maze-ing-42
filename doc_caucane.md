# 🌳 Growing Tree — Synthèse du choix (AMazeIng / 42)

---

## 🧠 Pourquoi choisir Growing Tree

Growing Tree est un algorithme de génération de labyrinthe basé sur une idée simple mais puissante :

> On maintient une liste de cellules actives et on étend progressivement le labyrinthe en choisissant une cellule selon une stratégie.

C’est un algorithme **hybride** qui peut se comporter comme DFS, Prim, ou un mélange des deux selon l’heuristique choisie.

---

## ⚙️ Fonctionnement

1. On commence avec une cellule initiale
2. On ajoute cette cellule dans une liste active
3. Tant que la liste n’est pas vide :
   - on sélectionne une cellule dans la liste (selon une règle)
   - on choisit un voisin NON VISITÉ aléatoirement
   - on casse le mur entre les deux
   - on ajoute le voisin à la liste active
   - si aucune extension possible → on retire la cellule

---

## 🧱 Propriété importante

✔ Growing Tree produit un **labyrinthe parfait** si :
- on ne connecte jamais deux cellules déjà visitées
- chaque nouvelle connexion ajoute exactement une cellule

👉 Donc :
- pas de cycles
- un seul chemin entre deux points
- structure = arbre couvrant

---

## 🔥 Pourquoi c’est un très bon choix pour 42

### ✔ Différenciation
- Ton binôme fait DFS (backtracking)
- Growing Tree est conceptuellement différent (frontière active vs profondeur)

### ✔ Intelligence algorithmique
- Tu choisis la stratégie de sélection
- Tu contrôles la forme du labyrinthe

### ✔ Flexibilité
Tu peux reproduire plusieurs comportements :
- DFS-like → pile (dernière cellule)
- Prim-like → aléatoire
- hybride → mix contrôlé

### ✔ Niveau attendu 42
- structures simples (liste / stack)
- logique claire
- facile à défendre à l’oral

---

## ⚖️ Avantages / Inconvénients

### 👍 Avantages
- Produit des labyrinthes parfaits
- Très flexible (comportement configurable)
- Plus intéressant que DFS classique
- Bonne valeur pédagogique et technique
- Facile à adapter et expliquer

### 👎 Inconvénients
- Un peu plus complexe que DFS
- Nécessite réflexion sur la stratégie de sélection
- Moins standard que BFS/DFS (mais c’est un avantage en soutenance)

---

## 🎯 Conclusion

Growing Tree est un excellent choix car :

- il garantit un labyrinthe parfait
- il est plus riche qu’un DFS classique
- il permet de justifier des choix algorithmiques
- il montre une vraie compréhension des structures de génération

👉 C’est un algorithme simple en base, mais puissant dans son comportement.

---

## 🚀 Recommandation finale

Pour AMazeIng :

- Ton binôme → DFS (backtracking)
- Toi → Growing Tree

👉 Résultat :
- deux approches différentes
- même objectif (labyrinthe parfait)
- meilleure défense de projet
