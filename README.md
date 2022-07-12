# Utilisation de l'API GPT-3 pour améliorer un texte :

**Préalable :**

Convertir un fichier "document" (.doc, .odt, etc.) en fichiers ".txt" dans le logitiel de traitement de texte adapté. 


Donner à Playground : 
```bash
#input
Améliore : 
"Dans un monde où le chômage augmente par le remplacement progressif du travail par les machines et la concurrence déloyale, on arrive à un moment où il faut repenser notre système de redistribution."
```

```bash
#output
"Le chômage augmente en raison du remplacement progressif du travail par les machines. La concurrence déloyale est également un problème. Il est donc temps de repenser notre système de redistribution."
```

Faire un script qui extrait tous le texte d'un mémoire, puis donner en entrée chaque phrase dans l'API :

(https://beta.openai.com/docs/quickstart/build-your-application)

Requirement :

```bash
sudo apt install python3.10-venv
```

API installation :
```bash
pip3 install openai
```

Create "OPENAI_API_KEY" environement variable :

```bash
pip install python-decouple
# create .env file in directory with openai key
touch .env
OPENAI_API_KEY=key_value
```

100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 270/270 [1:12:57<00:00, 16.21s/it]

## Texte Bonus 

Mérite "naturel" selon moi :

```
Pour illustrer, supposons une équipe de 5 chasseurs de lapin, le meilleur va capturer 6 lapins, 3 vont capturer 3 lapins et le moins bon, même en donnant toute son énergie, ne va pas réussir à récolter de lapin. Pourtant, il n'est pas possible de laisser ce dernier sans nourriture, et il est absurde que 6 lapins revienne uniquement dans la bouche du meilleur. Une façon équitable et bien vu par le groupe serait de repartir la nourriture de façon proportionnelle sans laisser son collègue mourir de faim : 4 pour le meilleur, les 3 pour les autres et 2 pour le dernier. De cette manière, le groupe est soudé et le mérite est psychologique (reconnaissance) et en même temps, il y a une forme de partage, car seul le meilleur donne. Dans les faits, ce n'est pas quantitatif, le groupe chasse la même chose, mais naturellement celui qui fait le plus d'effort va avoir le plus de butin de chasse, mais le dernier ne mourra pas de faim.
```
Mérite "naturel" selon gpt-3 :

```
Dans le cas du travail, le salaire est un argument de motivation pour le salarié, mais le salaire doit être proportionnel aux efforts fournis. Il est important de bien répartir l'argent dans la société pour motiver les salariés qui font des efforts au lieu de leur donner 100 % à ceux qui font le moins d'effort.

Dans la société, il est important de répartir équitablement les richesses pour éviter une émeute.

L'équité est importante dans la société, car elle permet de répartir équitablement les richesses entre les différents membres de la société. Lorsqu'une personne est mal rémunérée, elle peut devenir jalouse de ses voisins ou collègues, ce qui peut créer des tensions et des conflits. L'équité permet donc d'éviter les conflits sociaux et de maintenir la paix et l'harmonie entre les membres de la société.
```