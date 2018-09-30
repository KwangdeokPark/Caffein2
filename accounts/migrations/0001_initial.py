# Generated by Django 2.0.6 on 2018-09-30 10:20

import accounts.models
import accounts.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(help_text='snu.ac.kr 계정 이메일을 입력해주세요', max_length=254, unique=True, validators=[accounts.validators.snumail_validator], verbose_name='이메일')),
                ('name', models.CharField(max_length=30, verbose_name='이름')),
                ('phone', models.CharField(help_text='01x-xxxx-xxxx 형식으로 입력해주세요', max_length=14, validators=[accounts.validators.phone_validator], verbose_name='전화번호')),
                ('student_no', models.CharField(help_text='20xx-xxxxx 형식으로 입력해주세요', max_length=12, unique=True, validators=[accounts.validators.student_no_validator], verbose_name='학번')),
                ('college', models.CharField(choices=[('hum', '인문대학'), ('soc', '사회과학대학'), ('nat', '자연과학대학'), ('nur', '간호대학'), ('bus', '경영대학'), ('eng', '공과대학'), ('agr', '농업생명과학대학'), ('art', '미술대학'), ('law', '법과대학'), ('edu', '사범대학'), ('cbe', '생활과학대학'), ('vet', '수의과대학'), ('pha', '약학대학'), ('mus', '음악대학'), ('med', '의과대학'), ('cls', '자유전공학부'), ('uni', '연합전공'), ('cor', '연계전공')], max_length=3, verbose_name='단과대')),
                ('department', models.CharField(choices=[('00', '국어국문학과'), ('01', '중어중문학과'), ('02', '영어영문학과'), ('03', '독어독문학과'), ('04', '노어노문학과'), ('05', '서어서문학과'), ('06', '아시아언어문명학부'), ('07', '불어불문학과'), ('08', '언어학과'), ('09', '국사학과'), ('10', '동양사학과'), ('11', '서양사학과'), ('12', '철학과'), ('13', '종교학과'), ('14', '미학과'), ('15', '고고미술사학과'), ('16', '정치외교학부'), ('17', '경제학부'), ('18', '사회학과'), ('19', '인류학과'), ('20', '심리학과'), ('21', '지리학과'), ('22', '사회복지학과'), ('23', '언론정보학과'), ('24', '수리과학부'), ('25', '통계학과'), ('26', '물리천문학부'), ('27', '화학부'), ('28', '생명과학부'), ('29', '지구환경과학부'), ('30', '간호학과'), ('31', '경영학과'), ('32', '건설환경공학부'), ('33', '기계항공공학부'), ('34', '재료공학부'), ('35', '전기정보공학부'), ('36', '컴퓨터공학부'), ('37', '산업공학과'), ('38', '화학생물공학부'), ('39', '건축학과'), ('40', '건축공학과'), ('41', '조선해양공학과'), ('42', '에너지자원공학과'), ('43', '원자력공학과'), ('44', '식물생산과학부'), ('45', '산림과학부'), ('46', '응용생물화학부'), ('47', '식품동물생명공학부'), ('48', '바비오시스템소재학부'), ('49', '조경지역시스템공학부'), ('50', '농경제사회학부'), ('51', '동양화과'), ('52', '서양화과'), ('53', '조소과'), ('54', '공예과'), ('55', '디자인과'), ('56', '법학부'), ('56', '교육학과'), ('57', '국어교육과'), ('58', '영어교육과'), ('59', '불어교육과'), ('60', '독어교육과'), ('61', '사회교육과'), ('62', '역사교육과'), ('63', '지리교육과'), ('64', '윤리교육과'), ('65', '수학교육과'), ('66', '물리교육과'), ('67', '화학교육과'), ('68', '생물교육과'), ('69', '지구과학교육과'), ('70', '체육교육과'), ('71', '소비자아동학부'), ('72', '식품영양학과'), ('73', '의류학과'), ('74', '수의예과'), ('75', '수의학과'), ('76', '약학과'), ('77', '제약학과'), ('78', '성악과'), ('79', '작곡과(이론)'), ('80', '작곡과(작곡)'), ('81', '기악과'), ('82', '국악과'), ('83', '의예과'), ('84', '의학과'), ('85', '자유전공학부'), ('u0', '계산과학'), ('u1', '글로벌환경경영학'), ('u2', '기술경영'), ('u3', '영상매체예술'), ('u4', '정보문화학'), ('u5', '벤처경영학'), ('u6', '동아시아비교인문학'), ('c0', '중국학'), ('c1', '미국학'), ('c2', '러시아학'), ('c3', '라틴아메리카학'), ('c4', '유럽지역학'), ('c5', '뇌마음행동'), ('c6', '금융경제'), ('c7', '금융수학'), ('c8', '과학기술학'), ('c9', '공학바이오'), ('ca', '통합창의디자인'), ('cb', '고전문헌학'), ('cc', '인문데이터과학'), ('cd', '정치경제철학')], max_length=2, verbose_name='학과')),
                ('category', models.CharField(choices=[('u', '학부'), ('g', '대학원'), ('e', '교환'), ('p', '교직원')], max_length=1, verbose_name='분류')),
                ('profile_pic', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=accounts.models.get_profile_path, verbose_name='프로필 사진')),
                ('join_year', models.PositiveSmallIntegerField(default=2018, validators=[accounts.validators.year_validator], verbose_name='가입 년도')),
                ('join_semester', models.PositiveSmallIntegerField(choices=[(1, '1학기'), (2, '2학기')], default=accounts.models.get_default_semester, verbose_name='가입 학기')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('rule_confirm', models.BooleanField(default=False, validators=[accounts.validators.confirmation_validator], verbose_name='약관 동의')),
                ('survey_done', models.BooleanField(default=False, verbose_name='설문 완료 여부')),
                ('is_active', models.BooleanField(default=False, verbose_name='활동 상태')),
                ('is_staff', models.BooleanField(default=False, verbose_name='운영진 여부')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '회원',
                'verbose_name_plural': '회원',
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ActiveUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_year', models.PositiveSmallIntegerField(default=2018, validators=[accounts.validators.year_validator], verbose_name='활동 년도')),
                ('active_semester', models.PositiveSmallIntegerField(choices=[(1, '1학기'), (2, '2학기')], verbose_name='활동 학기')),
                ('is_paid', models.BooleanField(default=False, verbose_name='입금 확인')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '활동 회원',
                'verbose_name_plural': '활동 회원',
                'get_latest_by': ['-active_year', 'active_semester'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='activeuser',
            unique_together={('user', 'active_year', 'active_semester')},
        ),
    ]
