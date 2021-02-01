# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsInterests(models.Model):
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'accounts_interests'


class AccountsUserpersona(models.Model):
    name = models.CharField(unique=True, max_length=64)
    normalized_name = models.CharField(unique=True, max_length=64)
    description = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'accounts_userpersona'


class AccountsUserprofile(models.Model):
    is_full_name_displayed = models.BooleanField()
    persona = models.ForeignKey(AccountsUserpersona, models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_userprofile'


class AccountsUserprofileInterests(models.Model):
    userprofile = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)
    interests = models.ForeignKey(AccountsInterests, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_userprofile_interests'
        unique_together = (('userprofile', 'interests'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DataStructureAccount(models.Model):
    name = models.CharField(unique=True, max_length=200)
    account_number = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'data_structure_account'


class DataStructureBalance(models.Model):
    date_time = models.DateTimeField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'data_structure_balance'


class DataStructureCashflow(models.Model):
    date_time = models.DateTimeField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    comments = models.CharField(max_length=500, blank=True, null=True)
    account = models.OneToOneField(DataStructureAccount, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_structure_cashflow'


class DataStructureExternallink(models.Model):
    add_datetime = models.DateTimeField()
    title = models.CharField(max_length=100)
    link = models.TextField()

    class Meta:
        managed = False
        db_table = 'data_structure_externallink'


class DataStructureIns(models.Model):
    name = models.CharField(unique=True, max_length=200)
    location = models.CharField(max_length=50)
    alias = models.ForeignKey('DataStructureInsalias', models.DO_NOTHING, blank=True, null=True)
    ins_type = models.ForeignKey('DataStructureInstype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_structure_ins'


class DataStructureInsalias(models.Model):
    alias = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'data_structure_insalias'


class DataStructureInstype(models.Model):
    name = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'data_structure_instype'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PagesDatawidget(models.Model):
    title = models.CharField(unique=True, max_length=50, blank=True, null=True)
    js_name = models.CharField(unique=True, max_length=1000)
    comments = models.TextField()
    python_script = models.TextField()
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages_datawidget'


class PagesPage(models.Model):
    title = models.CharField(max_length=100)
    permalink = models.CharField(unique=True, max_length=12)
    update_date = models.DateTimeField()
    bodytext = models.TextField()

    class Meta:
        managed = False
        db_table = 'pages_page'


class PagesPageWidgets(models.Model):
    page = models.ForeignKey(PagesPage, models.DO_NOTHING)
    datawidget = models.ForeignKey(PagesDatawidget, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pages_page_widgets'
        unique_together = (('page', 'datawidget'),)
