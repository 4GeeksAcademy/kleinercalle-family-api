
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list.
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # Lista de miembros inicializada
        self._members = []

    # Método para generar IDs aleatorios
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        """
        Agrega un nuevo miembro a la lista de miembros. Si no se proporciona un ID, se genera automáticamente.
        """
        if 'id' not in member:
            member['id'] = self._generateId()
        if 'last_name' not in member:
            member['last_name'] = self.last_name  # Asignar automáticamente el apellido
        self._members.append(member)
        return member

    def delete_member(self, id):
        """
        Elimina un miembro de la lista de miembros por ID.
        """
        for member in self._members:
            if member['id'] == id:
                self._members.remove(member)
                return True
        return False

    def update_member(self, id, updates):
        """
        Actualiza la información de un miembro por ID.
        """
        for member in self._members:
            if member['id'] == id:
                member.update(updates)
                return member
        return None

    def get_member(self, id):
        """
        Devuelve un miembro específico por ID.
        """
        for member in self._members:
            if member['id'] == id:
                return member
        return None

    def get_all_members(self):
        """
        Devuelve la lista completa de miembros de la familia.
        """
        return self._members