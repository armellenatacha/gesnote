from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

# Register your models here.
# from gestionNote.models import User
from . import models

# admin.site.register(models.User)
admin.site.register(models.Parent)
admin.site.register(models.Eleve)
admin.site.register(models.Principal)
admin.site.register(models.Professeur)
admin.site.register(models.ChefInformatique)
admin.site.register(models.Matiere)
admin.site.register(models.Modules)
admin.site.register(models.Resultat)
admin.site.register(models.Classe)
admin.site.register(models.Specialite)
admin.site.register(models.Trimestre)
admin.site.register(models.Sequences)
admin.site.register(models.Note)


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('email', 'nom', 'telephone')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = models.User
        fields = ('email', 'password', 'parent', 'principal', 'chefInformatique', 'professeur', 'is_active', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'nom', 'telephone', 'is_superuser', 'is_active')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('nom', 'prenom', 'telephone',)}),
        ('Permissions', {'fields': ('parent', 'principal', 'chefInformatique', 'professeur', 'is_superuser', 'is_active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nom', 'telephone', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'telephone',)
    ordering = ('email', 'telephone',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(models.User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)