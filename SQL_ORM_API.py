import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2



Base = declarative_base()
#Data class for SQL base
class UserData(Base):
    __tablename__ = "UserData"

    id_requestion = sa.Column(sa.Integer, primary_key=True)
    gender = sa.Column(sa.Text)
    age = sa.Column(sa.Integer)
    FIO = sa.Column(sa.Text)
    address = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    login = sa.Column(sa.Text)

#Creating SQL Base
engine = sa.create_engine("postgresql+psycopg2://postgres:postgres@DB",
                            echo=True, pool_pre_ping=True)
#Creating tables
Base.metadata.create_all(engine)

DBSession = sessionmaker(
    binds={Base: engine},
    expire_on_commit=False,
)
session = DBSession()

async def last_id_requestion() -> int:
    """  This function realised find last request number in SQL base.   """
    return session.query(sa.func.coalesce(sa.func.max(Table.column), 0)).scalar()

async def save_users_data(data_dict: dict):
    """   This is saving function, in cycle parsing data from dictionary.
    id_requestion is variable for identityfy data others requests.
    """
    id_requestion = last_id_requestion() + 1
    for item in data_dict.get('users'):
        data = UserData(
        id_requestion=id_requestion,
        gender=item['gender'],
        age=item['age'],
        FIO=item['f_i_o'],
        address=item['adress'],
        email=item['email'],
        login=item['login']
        )
        session.add(data)#Preordering data
        session.commit()#Save data in SQL
