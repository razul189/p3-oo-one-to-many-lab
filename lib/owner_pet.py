# class Pet:

#     PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
#     all = []

#     def __init__(self, name, pet_type, owner="None"):
#         self.name = name
#         self.pet_type = pet_type
#         self.owner = owner
#         Pet.all.append(self)
        
#         if pet_type not in Pet.PET_TYPES:
#             raise Exception(f"Inavlid pet type: {pet_type}. Must be one of {Pet.PET_TYPES} .")
#         self.pet_type = pet_type

# class Owner:
#     def __init__(self, name): 
#         self.name = name
#         self.pets = []

#     def add_pet(self, pet):
#         if not isinstance(pet, Pet):
#             raise TypeError('add_pet method only accepts a pet instance.')
#         pet.owner = self
#         self.pets.append(pet)

#     def pets(self):
#         return self.pets

#     def sort_pets_by_name(self):
#         return sorted(self.pets, key=lambda pet: pet.name)

class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Direct validation in __init__
        if pet_type not in Pet.PET_TYPES:
            raise Exception('Not a valid pet type.')
        self.name = name
        self._pet_type = pet_type  # Directly setting the internal variable
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise Exception('Not a valid pet type.')
        self._pet_type = pet_type

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if not (isinstance(owner, Owner) or owner is None):
            raise Exception("Object is not of type Owner")
        self._owner = owner



class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Input object is not of type Pet")
        pet.owner = self            

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    
