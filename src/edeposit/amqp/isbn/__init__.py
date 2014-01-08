# This package may contain traces of nuts
from collections import namedtuple

class Result(namedtuple("Result",['valid','producent','publication'])):
    """
    valid: [True | False]
    producent: type Producent
    publication: MARCXML xml format
    """
    pass

class Producent(namedtuple("Producent",['title','phone','fax','email','url','identificator','ico'])):
    pass

class Publication(namedtuple("Publication",['stream',])):
    pass

def process_isbn(isbn):
    return Result(valid=True, 
                  producent=None,
                  publication=Publication(stream=""))

def producent_info(result):
    return result.producent

def publication_info(result):
    return result.publication
