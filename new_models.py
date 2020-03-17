# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agentie(models.Model):
    id_agentie = models.AutoField(primary_key=True)
    nume_agentie = models.CharField(max_length=30)
    tara_agentie = models.CharField(max_length=20, blank=True, null=True)
    oras_agentie = models.CharField(max_length=20, blank=True, null=True)
    email_agentie = models.CharField(max_length=30, blank=True, null=True)
    telefon_agentie = models.CharField(max_length=20, blank=True, null=True)
    adresa = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'agentie'


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class Autocar(models.Model):
    id_autocar = models.AutoField(primary_key=True)
    nume_autocar = models.CharField(max_length=20)
    locuri_totale = models.IntegerField()
    locuri_disponibile = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autocar'


class CamereHotel(models.Model):
    id_hotel = models.ForeignKey('Hotel', models.DO_NOTHING, db_column='id_hotel', blank=True, null=True)
    id_tip_camera_hotel = models.ForeignKey('TipCameraHotel', models.DO_NOTHING, db_column='id_tip_camera_hotel', blank=True, null=True)
    numar_total_camere = models.IntegerField()
    numar_camere_disponibile = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camere_hotel'


class Discount(models.Model):
    id_discount = models.AutoField(primary_key=True)
    nume_discount = models.CharField(unique=True, max_length=20)
    procent_discount = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'discount'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Hotel(models.Model):
    id_hotel = models.AutoField(primary_key=True)
    nume_hotel = models.CharField(max_length=20)
    tara = models.CharField(max_length=30, blank=True, null=True)
    oras = models.CharField(max_length=30, blank=True, null=True)
    adresa = models.CharField(max_length=40)
    pret = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hotel'


class Imagini(models.Model):
    tara = models.CharField(max_length=30, blank=True, null=True)
    oras = models.CharField(max_length=30)
    descriere = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'imagini'


class LocatiiAutocar(models.Model):
    id_locatii_autocar = models.AutoField(primary_key=True)
    id_autocar = models.ForeignKey(Autocar, models.DO_NOTHING, db_column='id_autocar', blank=True, null=True)
    tara = models.CharField(max_length=20)
    oras = models.CharField(max_length=20)
    pret_autocar = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locatii_autocar'


class LocatiiZbor(models.Model):
    id_locatii_zbor = models.AutoField(primary_key=True)
    id_zbor = models.ForeignKey('Zbor', models.DO_NOTHING, db_column='id_zbor', blank=True, null=True)
    tara = models.CharField(max_length=30)
    oras = models.CharField(max_length=30)
    pret_zbor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locatii_zbor'


class Masa(models.Model):
    id_masa = models.AutoField(primary_key=True)
    nume_masa = models.CharField(max_length=20)
    pret_masa = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'masa'


class MasaServicii(models.Model):
    id_servicii = models.ForeignKey('Servicii', models.DO_NOTHING, db_column='id_servicii', blank=True, null=True)
    id_masa = models.ForeignKey(Masa, models.DO_NOTHING, db_column='id_masa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'masa_servicii'


class ModalitatePlata(models.Model):
    id_modalitate_plata = models.AutoField(primary_key=True)
    nume_modalitate_plata = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'modalitate_plata'


class Orase(models.Model):
    id_oras = models.AutoField(primary_key=True)
    nume_oras = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orase'


class PersoaneRezervare(models.Model):
    id_persoane_rezervare = models.AutoField(primary_key=True)
    id_rezervare = models.ForeignKey('Rezervare', models.DO_NOTHING, db_column='id_rezervare', blank=True, null=True)
    id_discount = models.ForeignKey(Discount, models.DO_NOTHING, db_column='id_discount', blank=True, null=True)
    numar_persoane = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'persoane_rezervare'


class Plati(models.Model):
    id_plata = models.AutoField(primary_key=True)
    id_rezervare = models.ForeignKey('Rezervare', models.DO_NOTHING, db_column='id_rezervare', blank=True, null=True)
    total_plata = models.IntegerField()
    data_efectuare_plata = models.DateField()
    id_modalitate_plata = models.ForeignKey(ModalitatePlata, models.DO_NOTHING, db_column='id_modalitate_plata', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plati'


class Rezervare(models.Model):
    id_rezervare = models.AutoField(primary_key=True)
    id_utilizator = models.ForeignKey('Utilizator', models.DO_NOTHING, db_column='id_utilizator', blank=True, null=True)
    id_agentie = models.ForeignKey(Agentie, models.DO_NOTHING, db_column='id_agentie', blank=True, null=True)
    id_status_rezervare = models.ForeignKey('StatusRezervare', models.DO_NOTHING, db_column='id_status_rezervare', blank=True, null=True)
    data_rezervare = models.DateField()
    descriere_rezervare = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rezervare'


class RezervareTot(models.Model):
    nume = models.CharField(max_length=30, blank=True, null=True)
    prenume = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    oras = models.CharField(max_length=40, blank=True, null=True)
    telefon = models.CharField(max_length=40, blank=True, null=True)
    statut = models.CharField(max_length=40, blank=True, null=True)
    id_transport = models.IntegerField(blank=True, null=True)
    id_masa = models.IntegerField(blank=True, null=True)
    id_servicii = models.IntegerField(blank=True, null=True)
    numar_persoane = models.IntegerField(blank=True, null=True)
    id_agentie = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rezervare_tot'


class Servicii(models.Model):
    id_servicii = models.AutoField(primary_key=True)
    id_zbor = models.ForeignKey('Zbor', models.DO_NOTHING, db_column='id_zbor', blank=True, null=True)
    id_autocar = models.ForeignKey(Autocar, models.DO_NOTHING, db_column='id_autocar', blank=True, null=True)
    id_hotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='id_hotel', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicii'


class ServiciiRezervare(models.Model):
    id_servicii = models.ForeignKey(Servicii, models.DO_NOTHING, db_column='id_servicii', blank=True, null=True)
    id_rezervare = models.ForeignKey(Rezervare, models.DO_NOTHING, db_column='id_rezervare', blank=True, null=True)
    data_inceput = models.DateField()
    data_sfarsit = models.DateField(blank=True, null=True)
    numar_nopti = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'servicii_rezervare'


class StatusRezervare(models.Model):
    id_status_rezervare = models.AutoField(primary_key=True)
    nume_status = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'status_rezervare'


class TipCameraHotel(models.Model):
    id_tip_camera_hotel = models.AutoField(primary_key=True)
    nume_tip_camera_hotel = models.CharField(unique=True, max_length=20)
    numar_locuri = models.IntegerField(blank=True, null=True)
    pret_noapte = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tip_camera_hotel'


class Utilizator(models.Model):
    id_utilizator = models.AutoField(primary_key=True)
    nume_utilizator = models.CharField(max_length=20)
    prenume_utilizator = models.CharField(max_length=20)
    tara_utilizator = models.CharField(max_length=20, blank=True, null=True)
    oras_utilizator = models.CharField(max_length=20, blank=True, null=True)
    email_utilizator = models.CharField(max_length=30, blank=True, null=True)
    telefon_utilizator = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizator'


class Zbor(models.Model):
    id_zbor = models.AutoField(primary_key=True)
    nume_zbor = models.CharField(max_length=30)
    locuri_totale = models.IntegerField()
    locuri_disponibile = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zbor'
