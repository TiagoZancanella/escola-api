from dataclasses import dataclass, field
from dataclasses import dataclass, field
from datetime import datetime, date


import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import status_code_ranges

app = FastAPI()

@app.get("/")
def index():
    return {"mensagem": "Olá mundo"}

@app.get("/calculadora")
def calculadora(numero1 : int, numero2 : int):
    soma = numero1 + numero2
    return {"soma" : soma}

@app.get("/processar-cliente")
def processar_dados_cliente(nome:str, idade:int, sobrenome:str):
    nome_completo = nome + "" + sobrenome
    ano_nascimento = datetime.now().year - idade

    if ano_nascimento >= 1990 and ano_nascimento < 2000:
        decada = "decada de 90"
    elif ano_nascimento >= 1980 and ano_nascimento < 1990:
        decada = "decada de 90"
    elif ano_nascimento >= 1970 and ano_nascimento < 1970:
        decada = "decada de 70"
    else:
        decada = "Decada abaixo de 70 ou acima de 90"

    return {"nome_completo": nome_completo,
            "ano_nascimento": ano_nascimento,
            "decada": decada,}

@dataclass
class Curso:
    id: int = field()
    nome: str = field()
    sigla: str = field()

@dataclass
class CursoCadastro:
    nome: str = field()
    sigla: str = field()
@dataclass
class CursoEditar:
    nome: str = field()
    sigla: str = field()

alunos = [
    #instanciando um objeto da classer Curso
    Curso(id = 1 , nome = "Python Web" , sigla = "PY1"),
    Curso(id = 2 , nome = "Git e GitHub" , sigla = "GT")
]
@app.get("/api/cursos")
def listar_todos_cursos():
    return alunos


@app.get("/api/cursos/{id}")
def obter_por_id_curos(id:int ):
    for curso in alunos:
        if curso.id == id:
            return curso

        #lançado uma exceção com o status code de 404( Não encontrado )
    raise HTTPException(status_code=404, detail=F"Curso não encotrado com id: {id}")

@app.post("/api/cursos")
def cadastrar_curso(form: CursoCadastro):

    ultimo_id = max([curso.id for curso in alunos], default=0)

    curso = Curso(id = ultimo_id + 1, nome=form.nome , sigla=form.sigla )
    alunos.append(curso)

    return curso
@app.put("/api/cursos/{id}", status_code=200)
def editar_curso(id:int, form: CursoEditar):
    for curso in alunos:
        if curso.id == id:
            curso.nome = form.nome
            curso.sigla = form.sigla
            return  curso
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


@app.delete("/api/cursos/{id}", status_code=204)
def apagar_curso(id: int):
    for curso in alunos:
        if curso.id == id:
            alunos.remove(curso)
            return
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")





############################################################################################

                            #      EXERCICIO     #

############################################################################################


@dataclass
class Aluno:
    id: str = field()
    nome: str = field()
    sobrenome: str = field()
    cpf: str = field()
    data_nascimento: date = field()


@dataclass
class AlunoCadastro:
    nome: str = field()
    sobrenome: str = field()
    cpf: str = field()
    data_nascimento: date = field()


@dataclass
class AlunoEditar:
    nome: str = field()
    sobrenome: str = field()
    cpf: str = field()
    data_nascimento: date = field()


alunos_matriculado = [
    #instanciando um objeto da classer Curso
    Aluno(id = 1 , nome = "Tiago", sobrenome = "Zancanella", cpf = "12345678909", data_nascimento = "17/12/1992"),
    Aluno(id = 2 , nome = "Anthony", sobrenome = "Zancanella", cpf = "12345678900",data_nascimento= "09-08-2023"),
]

@app.get("/api/alunos")
def listar_todos_alunos():
    return alunos_matriculado


@app.get("/api/alunos/{id}")
def obter_por_id_alunos(id:int ):
    for aluno in alunos_matriculado:
        if aluno.id == id:
            return aluno

        #lançado uma exceção com o status code de 404( Não encontrado )
    raise HTTPException(status_code=404, detail=F"Aluno não encotrado com id: {id}")


@app.post("/api/alunos")
def cadastrar_aluno(form: AlunoCadastro):

    ultimo_id = max([aluno.id for aluno in alunos_matriculado], default=0)

    aluno = Aluno(id = ultimo_id + 1, nome=form.nome, sobrenome=form.sobrenome, cpf=form.cpf, data_nascimento=form.data_nascimento)

    alunos_matriculado.append(aluno)

    return aluno


@app.put("/api/alunos/{id}", status_code=200)
def editar_aluno(id:int, form: AlunoEditar):

    for aluno in alunos_matriculado:
        if aluno.id == id:
            aluno.nome = form.nome
            aluno.sobrenome = form.sobrenome
            aluno.cpf = form.cpf
            aluno.data_nascimento = form.data_nascimento
            return  aluno
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")


@app.delete("/api/alunos/{id}", status_code=204)
def apagar_aluno(id: int):
    for aluno in alunos_matriculado:
        if aluno.id == id:
            alunos_matriculado.remove(aluno)
            return
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")

















































if __name__ == "__main__":
    uvicorn.run("main:app")