from typing import Type

from django.db import models

import slothql
from slothql.utils.singleton import Singleton


class TypeRegistry(metaclass=Singleton):
    _type_mapping = {}

    def register(self, django_field: Type[models.Field], field: slothql.Field):
        self._type_mapping[django_field] = field

    def unregister(self, django_field: Type[models.Field]):
        del self._type_mapping[django_field]

    def clear(self):
        self._type_mapping.clear()

    def get(self, django_field: models.Field):
        if type(django_field) not in self._type_mapping:
            raise NotImplementedError(f'{type(django_field)} field conversion is not implemented')
        return self._type_mapping[type(django_field)]
