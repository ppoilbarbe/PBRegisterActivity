# PBRegisterActivity

Programme pour enregistrer son activité afin de pouvoir remplir le CRA
(Compte-Rendu d'Activité) ou un autre type de justificatif.

## Installation

Télécharger l'exécutable correspondant à votre plateforme depuis la page
des releases, puis le rendre exécutable (Linux/macOS) :

```bash
chmod +x pbregisteractivity-*-linux-x86_64
./pbregisteractivity-*-linux-x86_64
```

Aucune installation Python ni de dépendances supplémentaires n'est requise :
l'exécutable est autonome.

## Utilisation

Au lancement, la fenêtre principale permet de :

- saisir le nom de l'activité en cours (avec auto-complétion sur l'historique)
- ajuster l'heure de début si nécessaire
- enregistrer la plage avec **Enregistrer**

La barre de statut affiche le cumul de temps sur la journée. La fenêtre
peut être réduite dans la zone de notification système.

Le menu **Extraire** ouvre un dialogue d'analyse avec trois vues
(chronologie, camembert, texte) et permet d'exporter en HTML ou CSV.

## Fichiers de données

| Fichier | Rôle |
|---|---|
| `~/.pbregisteractivity/config.ini` | Configuration de l'application |
| `~/.pbregisteractivity/activity.txt` | Activités enregistrées |

## Licence

GNU General Public License v3 — voir le fichier [LICENSE](LICENSE).

---

*Pour la compilation et le développement, voir [CODING.md](CODING.md).*
