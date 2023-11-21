#!/usr/bin/python3
"""  """
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from os import getenv


class DBStorage:
    """
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """
        """
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Amenity).all())
            objs.extend(self.__session.query(Review).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            query = self.__session.query(cls)
            return {'{}.{}'.format(type(o).__name__, o.id): o for o in query}

    def new(self, obj):
        """
        """
        self.__session.add(obj)

    def save(self):
        """This method permit to commit all change in the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
