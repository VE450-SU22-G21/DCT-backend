from django.db import models


# A diagnosed user uploads all keys it has advertised in the past 14 days.
# A Report object contains a single key.
class Report(models.Model):
    key = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
    