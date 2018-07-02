import os
from django.conf import settings

if not settings.configured:
    # TODO: Production 레벨에서 Production 세팅으로 전환
    settings.configure('Caffein2.settings.dev', DEBUG=True)

from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from .category import (
    DEPARTMENT_CHOICES,
    COLLEGE_CHOICES
)
from .validator import (
    snumail_validator,
    student_no_validator,
    phone_validator,
    year_validator
)
from django.utils.timezone import now
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


def get_profile_path(instance, filename):
    user_id = instance.pk
    return 'accounts/profile/{}/{:%Y/%m/%d}/{}'.format(user_id, now(), filename)


def get_default_semester():
    """If today is between August(8) and September(9) return 2(Fall) else 1(Spring)"""
    if now().month in range(8, 10):
        return 2
    elif now().month in range(2, 4):
        return 1


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError(_('An user must have a SNU email'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    UNDERGRADUATE, GRADUATE, EXCHANGE, PROFESSOR = 'u', 'g', 'e', 'p'

    STUDENT_CATEGORY = (
        (UNDERGRADUATE, '학부생'),
        (GRADUATE, '대학원생'),
        (EXCHANGE, '교환학생'),
        (PROFESSOR, '교직원'),
    )
    SEMESTER_CHOICE = (
        (1, '1학기'),
        (2, '2학기'),
    )

    email = models.EmailField(_('이메일'), unique=True,
                              validators=[snumail_validator],
                              help_text=_('snu.ac.kr 계정 이메일을 입력해주세요'))
    name = models.CharField(_('이름'), max_length=30)
    phone = models.CharField(_('전화번호'), max_length=14,
                             validators=[phone_validator],
                             help_text=_('01x-xxxx-xxxx 형식으로 입력해주세요'))
    student_no = models.CharField(_('학번'), max_length=12, unique=True,
                                  validators=[student_no_validator],
                                  help_text=_('20xx-xxxxx 형식으로 입력해주세요'))

    college = models.CharField(_('단과대'), choices=COLLEGE_CHOICES, max_length=3)
    department = models.CharField(_('학과'), choices=DEPARTMENT_CHOICES, max_length=2)

    category = models.CharField(_('분류'), max_length=1, choices=STUDENT_CATEGORY)
    profile_pic = ProcessedImageField(upload_to=get_profile_path,
                                      processors=[Thumbnail(100, 100)],
                                      format='JPEG',
                                      options={'quality': 60},
                                      null=True, blank=True)

    join_year = models.PositiveSmallIntegerField(_('가입 년도'), validators=[year_validator], default=now().year)
    join_semester = models.PositiveSmallIntegerField(_('가입 학기'), choices=SEMESTER_CHOICE, default=get_default_semester)
    date_joined = models.DateTimeField(_('가입일'), auto_now_add=True)

    rule_confirm = models.BooleanField(_('약관 동의'), default=False)

    is_active = models.BooleanField(_('활동 상태'), default=True)
    is_staff = models.BooleanField(_('운영진 여부'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('회원')
        verbose_name_plural = _('회원')

    def __str__(self):
        return "{} {} {}".format(self.get_college_display(), self.get_department_display(), self.name)

    def get_user_name(self):
        """Returns the short name for the user.
        """
        return self.name

    def get_join_year_semester(self):
        return self.join_year, self.join_semester

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class ActiveUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    active_year = models.PositiveSmallIntegerField(_('활동 년도'), default=now().year, validators=[year_validator])
    active_semester = models.PositiveSmallIntegerField(_('활동 학기'), choices=User.SEMESTER_CHOICE)
    is_paid = models.BooleanField(_('입금 확인'), default=False)

    class Meta:
        verbose_name = _('활동 회원')
        verbose_name_plural = _('활동 회원')

    def __str__(self):
        return self.user.__str__()

    def is_paid(self):
        """Make bastards who didn't pay pay"""
        return self.is_paid

    @property
    def is_new(self):
        """Return whether this active user is a newbie or not"""
        return self.user.get_join_year_semester == (self.active_year, self.active_semester)
