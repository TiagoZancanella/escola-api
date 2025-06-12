#from dataclasses import Field
from datetime import date

from pydantic import BaseModel, Field


class MatriculaAluno(BaseModel):
    nome: str = Field()
    sobrenome: str = Field()
    id: int = Field()


class Matricula(BaseModel):
    data_matricula: date = Field(alias="dataMatricula")
    aluno: MatriculaAluno = Field()
    id: int = Field()

    class Config:
        populate_by_name = True
      #  allow_popullation_by_field_name = True



class MatriculaBase(BaseModel):
    aluno_id: int = Field()
    curso_id: int =Field()

class MatriculaCadastro(MatriculaBase):
    pass


class MatriculaEditar(BaseModel):
    curso_id: int = Field()