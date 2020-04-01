import factory
from faker import Factory

from .models import GrievanceTypes, Grievances, GrievanceDetails

facker = Factory.create()


class GrievanceTypesFactory(factory.DjangoModelFactory):
    class Meta:
        model = GrievanceTypes
        # griev_type = factory.LazyAttribute(facker.word())
        # griev_type = facker.word()


class GrievancesFactory(factory.DjangoModelFactory):
    class Meta:
        model = Grievances
        # griev_type_id = factory.SubFactory(GrievanceTypesFactory)
        # griev_title = factory.LazyAttribute(facker.word())
        # griev_desc = facker.text()


class GrievanceDetailsFactory(factory.DjangoModelFactory):
    class Meta:
        model = GrievanceDetails

        # griev_id = factory.SubFactory(GrievancesFactory)
        # griev_status = factory.LazyAttribute(facker.word())
        # griev_status_desc = facker.text()
