from dataclasses import Field
from datetime import date

from pydantic import BaseModel


class Matricula(BaseModel):
    data_matricula: date = Field(alias="dataMatricula")

class MatriculaBase(BaseModel):
    aluno_id: int = Field()
    curso_id: int =Field()

class MatriculaCadastro(MatriculaBase):
    pass


class MatriculaCadastro(BaseModel):
    curso_id: int = Field()