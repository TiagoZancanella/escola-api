from datetime import date
from fastapi import HTTPException
from src.escola_api.schemas.aluno_schemas import Aluno, Aluno, AlunoCadastro
from src.escola_api.app import router

alunos_matriculado = [
    Aluno(id=1, nome="Tiago", sobrenome="Zancanella", cpf="12345678909", dataNascimento=date(1992, 12, 17)),
    Aluno(id=2, nome="Anthony", sobrenome="Zancanella", cpf="12345678900", dataNascimento=date(2023, 8, 9)),
    ]


@router.get("/api/alunos")
def listar_todos_alunos():
    return alunos_matriculado


@router.get("/api/alunos/{id}")
def obter_por_id_alunos(id: int):
    for aluno in alunos_matriculado:
        if aluno.id == id:
            return aluno

        # lançado uma exceção com o status code de 404( Não encontrado )
    raise HTTPException(status_code=404, detail=F"Aluno não encotrado com id: {id}")


@router.post("/api/alunos")
def cadastrar_aluno(form: AlunoCadastro):
    ultimo_id = max([aluno.id for aluno in alunos_matriculado], default=0)

    aluno = Aluno(
        id=ultimo_id + 1,
        nome=form.nome,
        sobrenome=form.sobrenome,
        cpf=form.cpf,
        dataNascimento=form.data_nascimento)

    alunos_matriculado.append(aluno)

    return aluno


@router.put("/api/alunos/{id}", status_code=200)
def editar_aluno(id: int, form: Aluno):
    for aluno in alunos_matriculado:
        if aluno.id == id:
            aluno.nome = form.nome
            aluno.sobrenome = form.sobrenome
            aluno.cpf = form.cpf
            aluno.data_nascimento = form.data_nascimento
            return aluno
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")


@router.delete("/api/alunos/{id}", status_code=204)
def apagar_aluno(id: int):
    for aluno in alunos_matriculado:
        if aluno.id == id:
            alunos_matriculado.remove(aluno)
            return
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")



