from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    
    def create_user(self,email,nom,prenom,password,telephone):

        user = self.model(email=self.normalize_email(email),nom=nom,prenom=prenom,telephone=telephone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_parent(self,email,nom,prenom,password,telephone):
        user = self.create_user(email=self.normalize_email(email),nom=nom,prenom=prenom,telephone=telephone)
        user.parent = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_principal(self,email,nom,prenom,password,telephone):
        user = self.create_user(email=self.normalize_email(email),nom=nom,prenom=prenom,telephone=telephone)
        user.principal = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_chefInformatique(self,email,nom,prenom,password,telephone):
        user = self.create_user(email=self.normalize_email(email),nom=nom,prenom=prenom,telephone=telephone)
        user.chefInformatique = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_professeur(self,email,nom,prenom,password,telephone):
        user = self.create_user(email=self.normalize_email(email),nom=nom,prenom=prenom,telephone=telephone)
        user.professeur = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password):        
        user = self.model(email=email,password=password)
        user.set_password(password)
        user.is_active = True
        user.is_superuser = True
        # user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = None
    nom = models.CharField(max_length=250,unique=True)
    email = models.EmailField(_('email address'), unique=True)
    prenom = models.CharField(max_length=255,blank=True, null=True)
    telephone = models.CharField(max_length=50,unique=True)
    parent= models.BooleanField(default=False)
    principal= models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    chefInformatique = models.BooleanField(default=False)
    professeur = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS  = []
    objects = UserManager()


    def __str__(self):
        if self.parent == True:
            return "{} -- is_parent".format(self.email)
        if self.principal == True:
            return "{} -- is_principal".format(self.email)
        if self.chefInformatique == True:
            return "{} -- is_chefInformatique".format(self.email)
        if self.professeur == True:
            return "{} -- is_professeur".format(self.email)
        return "{} --- {}".format(self.nom,self.email) 

    def get_full_name(self):
        return "{} --- {}".format(self.nom, self.prenom)

    def get_short_name(self):
        return "{}".format(self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_superuser

class Parent(models.Model):
    parentUser = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parentUser')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Principal(models.Model):
    principalUser = models.OneToOneField(User, on_delete=models.CASCADE, related_name='principalUser')
    is_principal = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Professeur(models.Model):
    professeurUser = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professeurUser')
    is_professeur = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ChefInformatique(models.Model):
    chef_informatique = models.OneToOneField(User, on_delete=models.CASCADE, related_name='chef_informatique')
    is_chef_informatique = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Modules(models.Model):
    """Model definition for Modules."""

    codeModule = models.CharField('codeModule', max_length=200)
    nom_module = models.CharField('nom_module', max_length=200)
    # coefficient_module = models.CharField('coefficient_module', max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Resultat."""

        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

class Classe(models.Model):
    """Model definition for Classe."""

    codeClasse  =models.CharField('codeClasse', max_length=200)
    libelle_classe = models.CharField('libelle_classe', max_length=200, default="libelle")
    niveau_classe = models.CharField('niveau_classe', max_length=200,blank=True, null=True)
    module = models.ManyToManyField(Modules, related_name='moduleClasse')
    prof_titulaire = models.ForeignKey(Professeur, on_delete=models.CASCADE, related_name='prof_titulaire',blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Classe."""

        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'


class Matiere(models.Model):
    """Model definition for Martiere."""

    codeMatiere = models.CharField('codeMatiere', max_length=200)
    nom_Matiere = models.CharField('nom_Matiere', max_length=200)
    professeur = models.ManyToManyField(Professeur, related_name='professeurMatiere')
    classeM = models.ManyToManyField(Classe, related_name='classeMatiere')
    module = models.ForeignKey(Modules, models.CASCADE, related_name='matiereModule',blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Martiere."""

        verbose_name = 'Matiere'
        verbose_name_plural = 'Matieres'

    # def __str__(self):
    #     """Unicode representation of Martiere."""
    #     pass

class Eleve(models.Model):
    nom= models.CharField(max_length=250,unique=True)
    prenom= models.CharField(max_length=255,blank=True, null=True)
    matricule = models.CharField('matricule', max_length=200, blank=True, null=True)
    parentEleve = models.ForeignKey(Parent, models.CASCADE, related_name='parentEleve')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='eleveClasse', blank=True, null=True)
    date_naissance = models.DateTimeField('date_naissance', blank=True, null=True)
    lieu_naissance = models.CharField('lieu_naissance', max_length=200, blank=True, null=True)
    sexe = models.CharField('sexe', max_length=200, blank=True, null=True)
    is_eleve = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Resultat(models.Model):
    """Model definition for Resultat."""

    codeResultat = models.CharField('codeResultat', max_length=200)
    eleveProfil = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='eleveResultat')
    module = models.ManyToManyField(Modules, related_name='module')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Specialite(models.Model):
    """Model definition for Specialite."""

    codeSpecialite = models.CharField('codeSpecialite', max_length=200)
    nom_Specialite = models.CharField('nom_Specialite', max_length=200)
    classe = models.ManyToManyField(Classe, related_name='classeSpec')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Specialite."""

        verbose_name = 'Specialite'
        verbose_name_plural = 'Specialites'

class Trimestre(models.Model):
    numero_trimestre = models.CharField(max_length=3)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Sequences(models.Model):
    numero_sequence = models.CharField(max_length=3)
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE,  related_name='trimestreSeq')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Note(models.Model):
    """Model definition for Note."""

    codeNote = models.CharField('codeNote', max_length=200)
    sequence = models.ForeignKey(Sequences, on_delete=models.CASCADE, related_name='sequenceNote', blank=True, null=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='matiereNote')
    eleve = models.ForeignKey(Eleve, models.CASCADE, related_name='eleveNote')
    classe_n = models.ForeignKey(Classe, models.CASCADE, related_name='classeNote', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Note."""

        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

class Classe_matiere(models.Model):
    classe_m = models.ForeignKey("Classe", verbose_name=_("classe_m"), on_delete=models.CASCADE)
    matiere_c = models.ForeignKey("Matiere", verbose_name=_("matiere_c"), on_delete=models.CASCADE)
    coefficient_Matiere = models.CharField('coefficient_Matiere', max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



