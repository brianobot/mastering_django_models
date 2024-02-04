from django.db import models


class Person(models.Model):
    # fields translate to database table columns
    # when naming fields avoid names that conflict with the model api (clean, delete, save etc)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        # db_table: overwrite the default database tabel name for a model
        #    - use lower case names to ensure compatabilty with all database (MySQL, Mariadb)
        #    - to prevent database name length limitation on oracle, use < 30 chars for the database name
        #    - 
        # db_table_comment: this is useful for the direct database users who might not access through your django orm
        # 
        pass


class Asset(models.Model):
    data = models.FileField(upload_to="assets/")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name