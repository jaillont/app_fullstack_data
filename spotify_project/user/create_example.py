from user.models import User


class CreateTrackgroundExample:

    def __init__(self):
        pass

    def create_user_example(self):
        try:
            User.objects.get(email = 'trackgrounduser@gmail.com')
        except:
            user = User.objects.create_user(
                email = 'trackgrounduser@gmail.com',
                password = "MyPassword123&"
            )
            user.set_password = "MyPassword123&"
            user.first_name = "Jean"
            user.last_name = "Dupont"
            user.spotify_username = "31yct2zkcgfwd6txz2jtdsibztyy"
            user.save()
