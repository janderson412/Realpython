
class Entity:
    """Base class for S3 entity objects."""
    def __init__(self, fullname):
        """Initializer.

        Parameters
        ----------
            name: str
                Full pathname of entity
        """
        self._fullname = fullname
        parts = fullname.split('/')
        self._name = parts[len(parts) - 1]

    @property
    def FullPathname(self):
        """Full pathname of entity.

        Returns
        -------
        str
            Full pathname of entity
        """
        return self._name

    @property
    def Name(self):
        """Name of entity.

        Returns
        -------
        str
            Name of entity (without path)
        """
        return self._name

class File(Entity):

    def __init__(self, fullname):
        """File initializer.

        Parameters
        ----------
            fullname: str
                Full pathname of file
        """
        super().__init__(self, fullname)

class Directory(Entity):

    def __init__(self, fullname):
        """Directory initializer.

        Parameters
        ----------
            fullname: str
                Full pathname of directory
        """
        super().__init__(self, fullname)
        self._subentities = []

    @property
    def SubEntities(self):
        """Sub-entities.

        Returns
        -------
        list
            List of sub-entities (Directory and File objects)
        """
        return self._subentities;

    def Add(self, entity):
        """Add an entity.

        Parameters
        ----------
        entity : Entity
            Directory or File entity to add

        """
        if (entity is Directory) or (entity is File):
            self._subentities.append(entity)
        else:
            raise Exception('Attempt to add invalid type of object, must be File or Directory')

    @property
    def SubDirectories(self):
        """Get list of sub diretories

        Returns
        -------
        iterable
            List of sub-directories
        """
        for entity in self._subentities:
            if entity is Directory:
                yield entity

    @property
    def Files(self):
        """Get list of files in this directory

        Returns
        -------
        iterable
            List of files
        """
        for entity in self._subentities:
            if entity is File:
                yield entity


