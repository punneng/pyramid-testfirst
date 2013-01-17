from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    DateTime,
    Integer
    )

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import text
from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    validates,
    )

from zope.sqlalchemy import ZopeTransactionExtension

from formencode import validators, Invalid

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
#DBSession = scoped_session(sessionmaker())

class AppBase(object):
    _errors = None
    
    def save(self):
        if self.is_valid:
            try:
                DBSession.add(self)
                DBSession.flush()
                return True
            except IntegrityError:
                return False
        return False
        
    def update(self):
        if self.is_valid:
            try:
                DBSession.merge(self)
                DBSession.flush()
                return True
            except IntegrityError:
                return False
        return False
        
    def delete(self):
        try:
            DBSession.delete(self)
            DBSession.flush()
        except IntegrityError:
            return False
        return True
        
    @property
    def errors(self):
        return self._errors
        
    @property    
    def is_valid(self):
        return not bool(self._errors)
        
    def validate(self, validator, key, value):
        if not self._errors:
            self._errors = {}
        try:
            validator.to_python(value)
        except Invalid as e:
            if not self._errors.get(key):
                self._errors[key] = []
            self._errors[key].append(str(e))
            
Base = declarative_base(cls=AppBase)
      
class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(String(512), nullable=False)
    created_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    done_at = Column(DateTime)
    priority = Column(Integer, default=5) # 1 => the most priority, 10 => not important now 

    def __init__(self, task, done_at=None, priority=1):
        super(Todo, self).__init__()
        self.task = task
        self.done_at = done_at
        self.priority = priority
        
        
    @validates('task')
    def validate_task(self, key, value):
        self.validate(validators.String(not_empty=True), key, value)
        return value
        
    @validates('priority')
    def validate_priority(self, key, value):
        self.validate(validators.Int(), key, value)
        return value

