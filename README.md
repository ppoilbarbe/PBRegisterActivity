# PBRegisterActivity

Programme pour enregistrer son activité afin de pouvoir remplir le CRA
(Compte-Rendu d'Activité) ou un autre type de justificatif.

## Prérequis

### Exécution

  - Python 3.5 standard (ou supérieur) doit être installé
  - PyQt5 (Python Bindings for Qt 5) doit être accessible
  - matplotlib (tracés graphiques)

### Compilation

  - zip

### Développement

  Les prérequis d'exécution, de compilation et:

  - Designer 5 (modification de l'interface)
  - les outils de conversion vers Python des fichiers ui et qrc doivent
    être installés (pyuic5 et pyrcc5, paquet debian `pyqt5-dev-tools`)

## Compilation

Le programme est écrit en Python mais est conçu pour être autonome en
un seul fichier.

### Livraison

Pour créer l'exécutable, taper la commande «`make`», le fichier
`PBRegisterActivity` est alors utilisable tel que comme commande.

On peut aussi le lancer en préfixant le nom par `python3` (ou python si
c'est la version 3 qui est votre version par défaut)

    python3 PBRegisterActivity

### Pendant le développement

Lors de chaque modification d'interface graphique (fichiers .ui et .uic),
il faut lancer «make» dans le répertoire ui ou lancer «make ui» dans le
réperoire racine.

La commande «python3 src» dans le répertoire racine permet le lancement
de l'application sans créer le fichier qui embarque tout.

## Fichiers

### Configuration

La configuration du programme est dans
`$HOME/.pbregisteractivity/config.ini`

### Données

Les données saisies sont enregistrées dans
`$HOME/.pbregisteractivity/activity.txt`

### Verrou

Pour que l'application ne s'exécute pas 2 fois en même temps
sur le même compte, un fichier verrou est mis en place:
`$HOME/.pbregisteractivity/pbregisteractivity_running_once.lock`.

Ceci est nécessaire car le fichier de données est entièrement récrit
par l'application et on ne saurait pas qui écrirait la bonne
valeur, si tant est qu'il y en ait une, lorsque deux programmes,
voire plus, s'exécutent en même temps.

Le fichier est présent durant toute l'exécution du programme puis
est supprimé.
