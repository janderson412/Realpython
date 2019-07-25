
class Entity:
    """Base class for S3 entity objects."""
    def __init__(self, fullname):
        """Initializer.

        :param name: Full pathname of entity
        :type name: str
        """
        self._fullname = fullname
        parts = fullname.split('/')
        self._name = parts[len(parts) - 1]

    @property
    def FullPathname(self):
        """Full pathname of entity.

        :returns: (str) Full pathname of entity
        """
        return self._name

    @property
    def Name(self):
        """Name of entity.

        :returns: (str) Name of entity (without path)
        """
        return self._name

class File(Entity):

    def __init__(self, fullname):
        """File initializer.

        :param fullname: Full pathname of file
        :type fullname: str
        """
        super().__init__(self, fullname)

class Directory(Entity):

    def __init__(self, fullname):
        """Directory initializer.

        :param fullname: Full pathname of directory
        :type fullname: str
        """
        super().__init__(self, fullname)
        self._subentities = []

    @property
    def SubEntities(self):
        """Sub-entities.

        :returns: (list) List of sub-entities (Directory and File objects)
        """
        return self._subentities

    def Add(self, entity):
        """Add an entity.

        :param entity: Entity to add to this entity
        :type entity: Directory or File entity
        :raises: Exception: attempt to add invalid type
        """
        if entity is Entity:
            self._subentities.append(entity)
        else:
            raise Exception('Attempt to add invalid type of object, must be File or Directory entity')

    @property
    def SubDirectories(self):
        """Get list of sub directories

        :returns: (iterable) List of sub-directories
        """
        for entity in self._subentities:
            if entity is Directory:
                yield entity

    @property
    def Files(self):
        """Get list of files in this directory

        :returns: (iterable) List of files
        """
        for entity in self._subentities:
            if entity is File:
                yield entity


