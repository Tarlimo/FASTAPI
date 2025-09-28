from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import select

app = FastAPI()

engine = create_async_engine('sqlite+aiosqlite:///humans.db')
new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

class Base(DeclarativeBase):
    pass

class HumanModel(Base):
    __tablename__ = "humans"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    gender: Mapped[str]

@app.post("/setup_db")
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"status": "ok"}

class HumanAddSchema(BaseModel):
    name: str
    age: int
    gender: str

class HumanSchema(HumanAddSchema):
    id: int

@app.post("/humans")
async def add_human(data: HumanAddSchema, session: AsyncSession = Depends(get_session)):
    new_human = HumanModel(
        name=data.name,
        age=data.age,
        gender=data.gender
    )
    session.add(new_human)
    await session.commit()
    return {"status": "human added"}

@app.get("/humans")
async def list_humans(session: AsyncSession = Depends(get_session)):
    query = select(HumanModel)
    result = await session.execute(query)
    return result.scalars().all()

@app.put("/humans")
async def update_human(data: HumanSchema, session: AsyncSession = Depends(get_session)):
    query = select(HumanModel).where(HumanModel.id == data.id)
    result = await session.execute(query)
    human = result.scalar_one_or_none()
    if human is None:
        return {"error": "human not found"}
    human.name = data.name
    human.age = data.age
    human.gender = data.gender
    await session.commit()
    return {"status": "human updated"}

@app.delete("/humans")
async def delete_human(human_id: int, session: AsyncSession = Depends(get_session)):
    query = select(HumanModel).where(HumanModel.id == human_id)
    result = await session.execute(query)
    human = result.scalar_one_or_none()
    if human is None:
        return {"error": "human not found"}
    await session.delete(human)
    await session.commit()
    return {"status": "human deleted"}