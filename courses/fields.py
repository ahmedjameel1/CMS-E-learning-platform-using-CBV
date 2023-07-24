from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            # no current value
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    # filter by objects with the same field values
                    # for the fields in "for_fields"
                    query = {
                        field.attname: getattr(model_instance, field.attname)
                        for field in self.model._meta.fields
                        if field.attname in self.for_fields
                    }
                    qs = qs.filter(**query)
                    for i in self.model._meta.fields:
                        print(i, i.attname)
                    print(qs)
                    # get the order of the last item
                    last_item = qs.latest(self.attname)
                    value = getattr(last_item, self.attname) + 1
                else:
                    value = 0
                setattr(model_instance, self.attname, value)
                return value
            except ObjectDoesNotExist:
                value = 0
                setattr(model_instance, self.attname, value)
                return value
        else:
            return super().pre_save(model_instance, add)
