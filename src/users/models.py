from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from stdimage.models import StdImageField


# from onemosh.stdimage import resize_and_autorotate


# Custom User
class User(AbstractUser):  # Inherit Default User
    profile_pic = StdImageField(_('Profile Picture'),
                                help_text=_('Picture:JPG/JPEG.'),
                                upload_to='users/profile_pics',
                                # render_variations=resize_and_autorotate,
                                variations={
                                    'thumbnail': (100, 100, True), },
                                blank=True,
                                null=True, )

    class Meta:
        db_table = 'users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return '{username}'.format(username=self.username)
