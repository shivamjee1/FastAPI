from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy import create_engine, text
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import mapped_column, Mapped

app=FastAPI()


#this is the database connection url getting from .env file throgh this seetting class with given object
class Settings(BaseSettings):
    DATABASE_URL : str
    SECRET_KEY : str
    model_config = SettingsConfigDict(
        env_file= ".env",
        extra="ignore"
    )

settings = Settings()

#creating engine by this we create sessions 
engine = create_engine(settings.DATABASE_URL)


#datas=[] #used to test the endpoints basics using list

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

#function definition for the getting a session with the specified url(database)
def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()

Base = declarative_base()#used in the table creation phase

#Model difinition for the table 
class Data(Base):
    __tablename__= "Datas"
    id : Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    name : Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )
    password : Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )


#used to create the new model/table if not created
Base.metadata.create_all(bind=engine)


#request body used for client/user what data have to given by user 
class request_body(BaseModel):
    id:int
    name: str
    password: str

#responce what have to change in get to the user

#===============================================

#endpoints api
@app.get("/home")
def home():
    return {
        "details": "its home of test"
    }
#========================================================================
#used that list data for storage
# @app.get("/datas")
# def home():
#     return datas

# @app.post("/add_info")
# def put_data(data: request_body):
#     datas.append(data)
#     return {
#         "details": "data added",
#         "data": data
#     }
#========================================================================

#using database as storage
@app.get("/db_data")
def get_db_data(db:Session=Depends(get_db)):
    datas=db.query(Data).all()
    return datas

@app.get("/db-test")
def db_test(db:Session=Depends(get_db)):
    result= db.execute(text("SELECT 1"))

    return {
        "database" :result.scalar()
    }

@app.post("/create_data")
def create_data(data:request_body, db:Session=Depends(get_db)):
    newdata=Data(
        id=data.id,
        name=data.name,
        password=data.password
    )
    db.add(newdata)
    db.commit()
    db.refresh(newdata)
    return {
        "details": "dta added",
        "data": newdata
    }