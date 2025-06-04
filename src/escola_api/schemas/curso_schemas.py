from pydantic import BaseModel, Field
#from typing_extensions

class Curso(BaseModel):
    id: int = Field()
    nome: str = Field()
    sigla: str = Field()


class CursoCadastro(BaseModel):
    nome: str = Field()
    sigla: str = Field()


class CursoEditar(BaseModel):
    nome: str = Field()
    sigla: str = Field()

