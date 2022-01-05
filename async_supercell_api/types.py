from typing import Any, Dict, Generic, List, Optional, Type, TypeVar


class SupercellApiResponse:
    """
    Superclass of all API responses.
    
    :param success: wether the response was successful. Useful to spot errors
    :type success: bool
    """
    
    def __init__(self, success: bool = True, **kwargs):
        self.__success = success
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_string(self, *, level: int = 0, sep = '    ', nl: str = '\n'):
        """
        Returns a prettified string representation of the object.

        :param level: starting level of indentation. Default: 0
        :param sep: character sequence for indentation. Default: 4 spaces
        :param nl: new line sequence. Default '\\n'
        :type level: int
        :type sep: str
        :type nl: str
        """
        
        def recursion(obj, level: int = level, sep = sep) -> str:
            if isinstance(obj, SupercellApiResponse):
                return obj.to_string(level = level + 1, sep = sep)
            if isinstance(obj, list):
                return f'[{nl}{sep * (level + 2)}' + (
                    f',{nl}{sep * (level + 2)}'.join(
                        map(lambda x: recursion(x, level + 1, sep), obj)
                    )) + f'\n{sep * (level + 1)}]'
            return str(obj)
        
        to_skip = ['_SupercellApiResponse__success']
        return '{}({}{}{}{}{})'.format(
            type(self).__name__,
            nl,
            sep * (level + 1),
            f',{nl}{sep * (level + 1)}'.join(
                '{} = {}'.format(*item) for item in map(
                    lambda x: (x[0], recursion(x[1])),
                    filter(lambda x: x[0] not in to_skip and x[1] is not None, vars(self).items())
                )
            ),
            nl,
            sep * level,
        )
    
    def __repr__(self):
        return self.to_string()
    
    def __bool__(self):
        return self.__success


T = TypeVar('T')


class Page(SupercellApiResponse, Generic[T]):
    def __init__(self, items: Optional[List[T]] = None, paging: Optional[Dict[str, Any]] = None,
                 _page_generic_type: Optional[Type[SupercellApiResponse]] = None, **kwargs):
        """
        Object representing a list of items. It's returned by all the methods that have the 'limit', 'after' and 'before' parameters.
        
        :param items: list of items
        :param paging: info about the current, next and previous pages
        :param _page_generic_type: private type, only used for generalization
        :type items: Optional[List[:class:`SupercellApiResponse`]]
        :type paging: Optional[Dict[str, Any]]
        :type _page_generic_type:
        """
        
        super().__init__(**kwargs)
        self.items: List[T] = None if items is None else list(map(lambda x: _page_generic_type(**x), items))
        self.paging = paging
