from sqlalchemy import create_engine, URL, Column, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declared_attr

from backend.conf import settings

SQLALCHEMY_DATABASE_URL = URL(
    drivername=settings.DATABASE.DRIVER,
    username=settings.DATABASE.get('USERNAME', None),
    password=settings.DATABASE.get('PASSWORD', None),
    host=settings.DATABASE.get('HOST', None),
    port=settings.DATABASE.get('PORT', None),
    database=settings.DATABASE.get('NAME', None),
    query=settings.DATABASE.get('QUERY', None),
)

# echo=True表示引擎将用repr()函数记录所有语句及其参数列表到日志
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,  echo=True
)

# SQLAlchemy中，CRUD是通过会话进行管理的，所以需要先创建会话，
# 每一个SessionLocal实例就是一个数据库session
# flush指发送到数据库语句到数据库，但数据库不一定执行写入磁盘
# commit是指提交事务，将变更保存到数据库文件中
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


class CustomBase:
    """https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html"""

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_collate': 'utf8mb4_general_ci'
    }
    id = Column(BigInteger, primary_key=True, autoincrement=True)

# 创建基本映射类
Base = declarative_base()