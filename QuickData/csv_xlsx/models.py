from django.db import models

# Create your models here.
class archivo(models.Model):
    nombre = models.CharField(max_length=30)
    subir_archivo = models.FileField(upload_to='./csv_xlsx/archivos_csv/')
    def save(self, *args, **kwargs):
        # Verificar si el archivo fue subido
        if self.subir_archivo:
            # Obtener la extensión del archivo
            ext = self.subir_archivo.name.split('.')[-1]
            # Construir el nuevo nombre del archivo utilizando el campo `name`
            new_filename = f"{self.nombre}.{ext}"
            self.subir_archivo.name = new_filename
        super(archivo, self).save(*args, **kwargs)