from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from src.escola_api.app import router
from src.escola_api.database.modelos import CursoEntidade
from src.escola_api.dependencias import get_db
from src.escola_api.schemas.curso_schemas import CursoEditar, CursoCadastro


@router.get("/api/cursos", tags=["cursos"])
def listar_todos_cursos(db: Session = Depends(get_db)):
    cursos = db.query(CursoEntidade).all()
    # return (alunos)
    return cursos


@router.get("/api/cursos/{id}", tags=["cursos"])
def obter_por_id_cursos(id: int, db: Session = Depends(get_db)):
    curso = db.query(CursoEntidade).filter(CursoEntidade.id == id).first()
    if curso:
        return curso

    # lançado uma exceção com o status code de 404( Não encontrado )
    raise HTTPException(status_code=404, detail=F"Curso não encotrado com id: {id}")


@router.post("/api/cursos", tags=["cursos"])
def cadastrar_curso(form: CursoCadastro, db: Session = Depends(get_db)):
    curso = CursoEntidade(nome=form.nome, sigla=form.sigla)
    db.add(curso)
    db.commit()
    db.refresh(curso)

    return curso


@router.put("/api/cursos/{id}", status_code=200, tags=["cursos"])
def editar_curso(id: int, form: CursoEditar, db: Session = Depends((get_db))):
    curso = db.query(CursoEntidade).filter(CursoEntidade.id == id).first()
    if curso:
        curso.nome = form.nome
        curso.sigla = form.sigla
        db.commit()
        db.refresh(curso)
        return curso
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


@router.delete("/api/cursos/{id}", status_code=204, tags=["cursos"])
def apagar_curso(id: int, db: Session = Depends(get_db)):
    curso = db.query(CursoEntidade).filter(CursoEntidade.id == id).first()
    if curso:
        db.delete(curso)
        db.commit()
        return
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")
