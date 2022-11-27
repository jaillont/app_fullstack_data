# Trackground

:bulb: Idée du projet:  
Construire une application permettant de gérer, créer, enrichir et customiser ses playlists spotify.

 :computer: Technologies utilisées:
  - Frontend: Django
  - API: Django
  - Conteneur: Docker
  - Database: PostgreSQL
  - Music: Spotify API using spotipy librairy
  - Image Generation : stable diffusion from keras-CV
  

:musical_note: Trackground:  
Sur trackground vous pouvez connecter votre compte spotify et ainsi accéder à l'ensemble de vos playlists.
Trackground permet de visualiser et créer vos playlists. Vous aurez également la possibilité de découvrir certaines statistiques de vos playlists comme les artistes les plus présents. Trackground implémente également le modèle IA "stable diffusion" de KerasCV. Ce modèle vous permet de générer des illustrations pour vos playlists à partir d'une simple description textuelle comme par exemple: "electro album cover" ou "photograph of a dog on the moon" 
<p>
     <img src="https://github.com/jaillont/app_fullstack_data/blob/main/images/electro.png" width="320" height="320" />
     <img src="https://github.com/jaillont/app_fullstack_data/blob/main/images/metal.png" width="320" height="320" />
     <img src="https://github.com/jaillont/app_fullstack_data/blob/main/images/sunset.png" width="320" height="320" />

</p>

:nut_and_bolt: Lancement de l'application :  
Connectez vous sur Trackground avec les identifiants tests:  
Email : trackgrounduser@gmail.com  
Mot de passe : MyPassword123&  
Ou bien inscrivez vous, puis connectez votre compte spotify en récupérant votre l'identifiant et l'email de votre compte sur le lien suivant:  
https://www.spotify.com/fr/account/overview/?utm_source=spotify&utm_medium=menu&utm_campaign=your_account  
Avec à ces identifiants, trackground se connecte à l'API de spotify en utilisant la librairie spotipy.  

Sur trackground on retrouve:  

🌓 Light / Dark mode :  
En effet il est possible d'utiliser un mode sombre et même de changer le code couleur de l'application.  

🏠 La page home :  
Une fois connecté, vous arriverez sur cette page de présentation de l'application.  

📂 La page service :  
La page service renvoi vers les différents outils comme la création de playlists ou la génération d'images.  

📫 La page contact :  
Cette page permet de nous contacter par mail depuis l'application. L'envoi des emails est assuré par l'API email de Mailtrap.  

🖼️ La génération d'images :  
Cette page vous permet de générer des images grâce à de simples descriptions d'images, de contexte et de style. Pour chaque prompt, le modèle retourne trois propositions que vous pouvez ou non sauvegarder. Seul bémol la génération peut prendre plusieurs minutes selon les ressources de votre machine.  

🎶 La page playlist :  
Cette page contient l'ensemble de vos playlists, il ne vous reste plus qu'à en sélectioner une pour accéder à l'ensemble de ses musiques. Dans chaque playlist on retrouve les informations importantes comme la durée de la playlist et de chaque musique mais aussi les artistes et la possibilité d'écouter la musique.  

Voici une vue d'ensemble de l'application :   




