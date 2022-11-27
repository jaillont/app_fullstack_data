from django import forms


#### Form to create a New Playlist ####

class NewPlaylistForm(forms.Form):
    title = forms.CharField(
        label='Playlist title',
        max_length=100
    )
    description = forms.CharField(
        label='Playlist description',
        max_length=100,
        required=False
    )
    tracks = forms.CharField(
        label = "Add Tracks",
        max_length=1000
    )
    image = forms.CharField(
        label="Image",
        max_length=200,
        required=False
    )


class CustomNewPlaylistForm(NewPlaylistForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['title'].widget.attrs.update(
        {
            'class': 'form-control',
            'placeholder': 'Title'
        }
    )
    self.fields['description'].widget.attrs.update(
        {
            'class': 'form-control',
            'placeholder': 'Description (optional)'
        }
    )
    self.fields['tracks'].widget.attrs.update(
        {
            'class': 'form-control',
            'placeholder': 'Add tracks - ex : "(artist_name,song)-(artist_name2,song2)"'
        }
    )
    self.fields['image'].widget.attrs.update(
        {
            'class': 'form-control selected-image',
            'placeholder': 'Image path (optional)'
        }
    )


#### Form to create a New Cover Image ####

class ImageForm(forms.Form):
    image_description = forms.CharField(
        label = "Image Description",
        max_length = 1000
    )
    image_type = forms.CharField(
        label = "Image Type",
        max_length = 1000,
        required=False
    )
    image_aspect = forms.CharField(
        label = "Image Aspect",
        max_length = 1000,
        required=False
    )
    image_name = forms.CharField(
        label = "Name",
        max_length = 30
    )


class CustomImageForm(ImageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_description'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Image Description - Ex : A red dog'
            }
        )
        self.fields['image_type'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Image Type - Ex : A photo (optional)'
            }
        )
        self.fields['image_aspect'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Image Aspect - Ex : Black and White (optional)'
            }
        )
        self.fields['image_name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Image Name (No space permitted)'
            }
        )


#### Form to choose images generated to keep ####

class ImagesChosenForm(forms.Form):
    images = forms.CharField(
        label = "Images",
        max_length = 300
    )


class CustomImagesChosenForm(ImagesChosenForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Images chosen'
            }
        )


#### Form to send an Email ####

class ContactForm(forms.Form):
    subject = forms.CharField(
        label = "Subject",
        max_length = 200
    )
    message = forms.CharField(
        label = "Message",
        max_length = 1000,
        widget=forms.Textarea
    )


class CustomContactForm(ContactForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Subject'
            }
        )
        self.fields['message'].widget.attrs.update(
            {
                'class': 'form-control textarea',
                'placeholder': 'Message'
            }
        )
