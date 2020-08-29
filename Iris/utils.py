from .models import Species

# helper function to get species name
def specie_name(key):
    specie = Species.objects.get(id=key)
    return specie

