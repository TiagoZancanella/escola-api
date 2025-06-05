from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from src.escola_api.app import router
from src.escola_api.database.banco_dados import SessionLocal
from src.escola_api.database.modelos import CursoEntidade
from src.escola_api.schemas.curso_schemas import CursoEditar, CursoCadastro

# from src.escola_api.database.schemas.curso_schemas import CursoCadastro, Curso, CursoEditar
# from src.escola_api.main import app, alunos


alunos = [
    # instanciando um objeto da classer Curso
    CursoEditar(id=1, nome="Python Web", sigla="PY1"),
    CursoEditar(id=2, nome="Git e GitHub", sigla="GH")
]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/api/cursos")
def listar_todos_cursos(db: Session = Depends(get_db)):
    cursos = db.query(CursoEntidade).all()
    # return (alunos)
    return cursos


@router.get("/api/cursos/{id}")
def obter_por_id_cursos(id: int ,db:Session =Depends(get_db)):
    curso = db.query(CursoEntidade).filter(CursoEntidade.id == id).first()
    if curso:
            return curso

        # lançado uma exceção com o status code de 404( Não encontrado )
    raise HTTPException(status_code=404, detail=F"Curso não encotrado com id: {id}")


@router.post("/api/cursos")
def cadastrar_curso(form: CursoCadastro, db:Session =Depends(get_db)):
    curso = CursoEntidade(nome=form.nome, sigla=form.sigla)
    db.add(curso)
    db.commit()
    db.refresh(curso)

    return curso


@router.put("/api/cursos/{id}", status_code=200)
def editar_curso(id: int, form: CursoEditar, db: Session = Depends((get_db))):
    curso = db.query(CursoEntidade).filter(CursoEntidade.id == id).first()
    if curso:
            curso.nome = form.nome
            curso.sigla = form.sigla
            db.commit()
            db.refresh(curso)
            return curso
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


@router.delete("/api/cursos/{id}", status_code=204)
def apagar_curso(id: int, db:Session =Depends(get_db)):
    curso = db.query(CursoEntidade).filter(CursoEntidade.id == id).first()
    if curso:
            db.delete(curso)
            db.commit()
            return
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")
