import lexical_uuid
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.types import TypeDecorator


class LexicalUUID(TypeDecorator):
  impl = BYTEA

  def __init__(self):
    self.impl.length = 16
    super(LexicalUUID, self).__init__(length=self.impl.length)

  def process_bind_param(self, value, dialect=None):
    if value and isinstance(value, lexical_uuid.LexicalUUID):
      return value.bytes
    elif value and not isinstance(value, lexical_uuid.LexicalUUID):
      raise TypeError("Value {} is not a valid LexicalUUID (must be an "
                      "instance of lexical_uuid.LexicalUUID).".format(value))
    else:
      return None

  def process_result_value(self, value, dialect=None):
    if value:
      return lexical_uuid.LexicalUUID(value=value)
    else:
      return None

  def is_mutable(self):
    return False

__doc__ = """
Usage::
  class Entity(db.Model):
    id = db.Column('id', LexicalUUID(), primary_key=True, default=lexical_uuid.LexicalUUID)
"""
