# gkpodcasts

Un simple rôle Ansible permettant de créer des flux RSS pour les podcasts de Gamekult (entre autres, fonctionne avec n'importe quoi d'autre qui proposerait des podcasts avec l'idée saugrenue de ne pas les associer à un flux RSS)

Nécessite d'avoir sous la main un serveur HTTP et une connaissance même restreinte d'Ansible. Si vous n'y connaissez rien à Ansible, bon courage parce que je me vois mal expliquer comment tout ça fonctionne dans ce README. 

Pas grand chose n'est automatisé à part la génération du flux RSS, il faut donc dans le fichier de configuration host_vars/ indiquer manuellement:

- le titre du Podcast
- l'auteur
- le site web
- un résumé du concept
- un copyright
- une image d'illustration

Et ensuite par épisode:

- un titre
- un lien vers la page web où l'épisode est publié
- la date de publi
- la durée
- le résumé
- et enfin et surtout l'URL Soundcloud vers votre épisode

Le fichier host_vars/localhost présent dans ce répo a déjà deux podcasts pré-remplis pour un total de 3 épisodes, seules manquent les URLs Soundcloud parce qu'il y a mon token dedans...

Ça reste donc maxi casse-couilles même si je peux peut-être scripter un peu pour au moins extraire quelques métadonnées de la page web mais pour l'instant j'ai pas eu le courage.

J'ai perdu 3h de ma vie à coder ça un samedi, merci les branlos !
