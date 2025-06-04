
from src.escola_api.schemas.curso_schemas import Curso, CursoEditar, CursoCadastro
from src.escola_api.app import  router
from fastapi import HTTPException

#from src.escola_api.database.schemas.curso_schemas import CursoCadastro, Curso, CursoEditar
#from src.escola_api.main import app, alunos


alunos = [
    # instanciando um objeto da classer Curso
    CursoEditar(id=1, nome="Python Web", sigla="PY1"),
    CursoEditar(id=2, nome="Git e GitHub", sigla="GH")
]


@router.get("/api/cursos")
def listar_todos_cursos():
    return (alunos)


@router.get("/api/cursos/{id}")
def obter_por_id_cursos(id: int):
    for curso in alunos:
        if curso.id == id:
            return curso

        # lançado uma exceção com o status code de 404( Não encontrado )
    raise HTTPException(status_code=404, detail=F"Curso não encotrado com id: {id}")


@router.post("/api/cursos")
def cadastrar_curso(form: CursoCadastro):
    ultimo_id = max([curso.id for curso in alunos], default=0)

    curso = CursoEditar(id=ultimo_id + 1, nome=form.nome, sigla=form.sigla)
    alunos.append(curso)

    return curso


@router.put("/api/cursos/{id}", status_code=200)
def editar_curso(id: int, form: CursoEditar):
    for curso in alunos:
        if curso.id == id:
            curso.nome = form.nome
            curso.sigla = form.sigla
            return curso
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


@router.delete("/api/cursos/{id}", status_code=204)
def apagar_curso(id: int):
    for curso in alunos:
        if curso.id == id:
            alunos.remove(curso)
            return
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")
