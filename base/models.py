from django.db import models


class CustomBaseManager(models.Manager):
    def get_queryset(self) -> models.query.QuerySet:
        return super(CustomBaseManager, self).get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, null=False, db_index=True)
    objects = models.Manager()
    custom_objects = CustomBaseManager()

    def delete(self, *args, soft_delete: bool = True, **kwargs) -> tuple[int, dict[str, int]]:
        if soft_delete:
            self.is_deleted = True
            self.save()
        else:
            return super().delete(*args, **kwargs)

    class Meta:
        abstract = True
