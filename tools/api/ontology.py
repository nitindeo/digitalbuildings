import sys
from typing import List

sys.path.insert(1, '../validators/ontology_validator/')

from yamlformat.validator.entity_type_lib import EntityType
from yamlformat.validator.presubmit_validate_types_lib import ConfigUniverse
from yamlformat import constants

from model import StandardField
from model import EntityTypeField

class Ontology(object):
    """Class defining an implementation of Google's ConfigUniverse as an ontology

       Args:
            universe: an instantiated ConfigUniverse Object

       Attributes:
            universe: A ConfigUniverse object detailing the various universes in the ontology

       Returns:
            An instance of Ontology class
    """

    def __init__(self, universe: ConfigUniverse):
        super().__init__()
        self.universe = universe

    def GetFieldsForTypeName(self, namespace: str, entity_type_name: str, required_only: bool = False) -> List[EntityTypeField]:
        """gets a list of fields for a given typename within a namespace

           Args:
                namespace: the name of the namespace as a string
                entity_type_name: name of the entity type as a string
                required_only: when true will return only required fields for a given type

           Returns:
                result_fields: a list of StandardField tuples
        """
        pass
     
    def GetEntityTypesFromFields(self, field_list: List[StandardField], general_type: str = None) -> List[EntityType]:
        """gets a list of EntityType objects matching a given a list of StandardField tuples

           Args:
                field_list: a list of StandardField tuples to match to an entity
                general_type: a string indicating a general type name to narrow return results

            Returns:
                entities: a list of EntityType objects matching the provided list of fields
        """
        pass

    def IsFieldValid(self, field: StandardField) -> bool:
        """A method to validate a field name against the ontology"""
        pass

