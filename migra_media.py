import os
from django.core.files import File
from biblioteca.models import Autor

for obj in Autor.objects.all():
    if obj.retrato and obj.retrato.name:
        nome = obj.retrato.name.lstrip("/")
        if nome.startswith("media/"):
            nome = nome[6:]

        base = os.path.splitext(nome)[0]
        local_path = os.path.join("media", f"{base}.jpeg")
        if not os.path.exists(local_path) and "_" in base:
            local_path = os.path.join("media", f"{base.rsplit('_', 1)[0]}.jpeg")

        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.retrato.save(
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )
            print(f"Migrado: {obj}")