import os
from django.conf import settings
from django.core.files import File
from biblioteca.models import Autor   # adaptar ao modelo

for obj in Autor.objects.all():
    if obj.retrato and obj.retrato.name:   # adaptar o nome do campo (neste caso é "retrato")
        nome = obj.retrato.name.lstrip("/")
        if nome.startswith("media/"):
            nome = nome[6:]

        base = os.path.splitext(nome)[0]
        local_path = os.path.join(settings.MEDIA_ROOT, f"{base}.jpeg")
        if not os.path.exists(local_path) and "_" in base:
            local_path = os.path.join(settings.MEDIA_ROOT, f"{base.rsplit('_', 1)[0]}.jpeg")

        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.retrato.save(                         # adequar
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )
            print(f"Migrado: {obj}")