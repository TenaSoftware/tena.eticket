"""
`ausers` backends for tena project.

Generated Manually from Linux terminal
 * NAME: Wendirad Demelash
 * DATE: April 3, 2021
"""
from django.contrib.auth.backends import ModelBackend
from django.db.models import Exists, OuterRef, Q

from ausers.models import Customer
from ausers.utils import twilio_verify

class CustomerBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(Customer.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            username = twilio_verify._formated_number(username)
            user = Customer._default_manager.get_by_natural_key(username)
        except Customer.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            Customer().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def with_perm(self, perm, is_active=True, include_superusers=True, obj=None):
        """
        Return users that have permission "perm". By default, filter out
        inactive users and include superusers.
        """
        if isinstance(perm, str):
            try:
                app_label, codename = perm.split('.')
            except ValueError:
                raise ValueError(
                    'Permission name should be in the form '
                    'app_label.permission_codename.'
                )
        elif not isinstance(perm, Permission):
            raise TypeError(
                'The `perm` argument must be a string or a permission instance.'
            )

        UserModel = Customer
        if obj is not None:
            return UserModel._default_manager.none()

        permission_q = Q(group__user=OuterRef('pk')) | Q(user=OuterRef('pk'))
        if isinstance(perm, Permission):
            permission_q &= Q(pk=perm.pk)
        else:
            permission_q &= Q(codename=codename, content_type__app_label=app_label)

        user_q = Exists(Permission.objects.filter(permission_q))
        if include_superusers:
            user_q |= Q(is_superuser=True)
        if is_active is not None:
            user_q &= Q(is_active=is_active)

        return UserModel._default_manager.filter(user_q)

    def get_user(self, user_id):
        try:
            user = Customer._default_manager.get(pk=user_id)
        except Customer.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
