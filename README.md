# Trackground

:bulb: Idée du projet:  
Construire une application permettant de gérer, créer, enrichir et customisé ses playlist spotify.

 :computer: Technologies utilisées:
  - Frontend: Django
  - API: Django
  - Conteneur: Docker
  - Database: PostgreSQL
  - Music: Spotify API using spotipy
  - Image Generation : stable diffusion with keras
  

:musical_note: Trackground:  
Sur trackground vous pouvez connecter votre compte spotify et ainsi accéder à l'ensemble de vos playlists.
Trackground permet de visualiser vos playlists, d'en créer ou de les modifier. Vous aurez également la possibilité de découvrir certaines statistiques de vos playlist comme les artistes les plus présents. Trackground implémente également le modèle IA "stable diffusion" de KerasCV. Ce modèle vous permet de générer des illustrations pour vos playlists à partir d'une simple description textuelle comme par exemple: "electro album cover"
<p>
     <img src="https://github.com/jaillont/app_fullstack_data/blob/main/images/electro.png" width="320" height="320" />
     <img src="https://github.com/jaillont/app_fullstack_data/blob/main/images/metal.png" width="320" height="320" />
     <img src="https://github.com/jaillont/app_fullstack_data/blob/main/images/sunset.png" width="320" height="320" />

</p>

:nut_and_bolt: Fonctionnement de l'application :  
Grâce l'API de spotify, vous pouvez vous créer un compte développeur sur le lien suivant: https://developer.spotify.com/dashboard/applications  
Une fois votre compte créé, récupérez vos client_ID et client_secret et créer un utilisateur avec le mail de votre compte spotify. De retour sur trackground il ne vous reste plus alors qu'à vous connecter pour pouvoir accéder à vos playlists. Trackground utilise ensuite la librairie python spotipy qui gère la connexion à l'API de spotify.  

🌓 Light / Dark mode :  
En effet il est possible d'utiliser un mode sombre et même de changer le code couleur de l'application.  
🏠 la page home :  
Une fois connecté, vous arriverez sur cette page de présentation de l'application.

📂 La page service :  
La page service renvoi vers les différents outils comme la création de playlists ou la génération d'images.  

📫 La page contact :  
Cette page permet de nous contacter par mail depuis l'application. L'envoi des emails est assuré par l'API email de Mailtrap.  

🖼️ La génération d'images :  
Cette page vous permet de générer des images grâce à de simples descriptions d'images, de contexte et de style. Pour chaque prompt, le modèle retourne trois propositions que vous pouvez ou non sauvegarder. Seul bémol la génération peut prendre plusieurs minutes selon les ressources de votre machine.  

🎶 La page playlist:  
Cette page contient l'ensemble de vos playlists, il ne vous reste plus qu'à en sélectioner une pour accéder à l'ensemble de ses musiques. Dans chaque playlist on retrouve les informations immortantes comme la durée de la playlist et de chaque musique mais aussi les artistes et la possibilité d'écouter la musique.  






