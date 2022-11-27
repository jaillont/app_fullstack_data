from user.models import User


class CreateTrackgroundExample:

    def __init__(self):
        pass

    def create_user(self):
        try:
            User.objects.get(email = 'quentin.barthelemy@edu.esiee.fr')
        except:
            user = User.objects.create_user(
                email = 'quentin.barthelemy@edu.esiee.fr',
                password = "MyPassword123&"
            )
            user.set_password = "MyPassword123&"
            user.first_name = "Quentin"
            user.last_name = "Barthélémy"
            user.spotify_username = "31tzzkjdwe32nspi4chb6gvz7qhm"
            user.save()


    def create_user_example(self):
        self.create_user()
