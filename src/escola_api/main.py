from dataclasses import field
from datetime import datetime, date
import uvicorn
from fastapi import HTTPException
from pydantic import Field, BaseModel
from src.escola_api.api.v1 import curso_controller, aluno_controller
from src.escola_api.app import app, router
from src.escola_api.database.banco_dados import engine, Base


Base.metadata.create_all(bind=engine)

app.include_router(curso_controller.router)
app.include_router(aluno_controller.router)







############################################################################################

#      EXERCICIO     #

############################################################################################
class FormacaoCadastro(BaseModel):
    nome: str = field()
    descricao: str = field()
    duracao: int = field()


class ProfessoresEditar(BaseModel):
    nome: str = field()



class FormacaoEditar(BaseModel):
    descricao: str =field()


class Formacao(BaseModel):
    id: int =field()
    nome: str =field()
    descricao: str =field()
    duracao: int =field()


formacao_cadastrada = [Formacao(id=1, nome="SuperDev", descricao="completo" , duracao=90)]

@router.post("/api/formacao")
def cadastrar_formacao(form: FormacaoCadastro):
    ultimo_id = max([nome.id for nome in formacao_cadastrada], default=0)

    formacao = Formacao(
        id=ultimo_id + 1,
        nome=form.nome,
        descricao=form.descricao,
        duracao=form.duracao,
    )

    formacao_cadastrada.append(formacao)
    return formacao


@router.get("/api/formacao")
def listar_todas_formacoes():
    return formacao_cadastrada


@router.get("/api/formacao/{id}")
def obter_por_id_formacao(id: int):
    for nome in formacao_cadastrada:
        if nome.id == id:
            return nome

        # lançado uma exceção com o status code de 404( Não encontrado )
    raise HTTPException(status_code=404, detail=F"Formacao não encotrado com id: {id}")

@router.delete("/api/formacao/{id}", status_code=204)
def apagar_formacao(id: int):
    for nome in formacao_cadastrada:
        if nome.id == id:
            formacao_cadastrada.remove(nome)
            return
    raise HTTPException(status_code=404, detail=f"formacao não encontrada com id: {id}")



@router.put("/api/formacao/{id}", status_code=200)
def editar_formacao(id: int, form: FormacaoEditar):
    for formacao in formacao_cadastrada:
        if formacao.id == id:
            formacao.descricao = form.descricao

            return formacao
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")


class Professores(BaseModel):
    id: int = field()
    nome: str = field()
    cnpj: str = field()
    nomeFantasia: str = field()
    chavePix: str = field()
    formacao: str = field()
    dataAniversario: datetime = field()
    signo: str = field()



professores_cadastrado = [Professores(id=1,
                                      nome="Tiago",
                                      cnpj="91919191919",
                                      nomeFantasia="tiagoo",
                                      chavePix="20392093",
                                      formacao="engenheiro",
                                      dataAniversario="1992-12-17",
                                      signo="aries")]

class ProfessoresCadastro(BaseModel):
    nome: str = field()
    cnpj: str = field()
    nomeFantasia: str = field()
    chavePix: str = field()
    formacao: str = field()
    dataAniversario: datetime = field()
    signo: str = field()




@router.post("/api/professores")
def cadastrar_professores(form: ProfessoresCadastro):
    ultimo_id = max([nome.id for nome in professores_cadastrado], default=0)

    professores = Professores(
        id=ultimo_id + 1,
        nome=form.nome,
        cnpj=form.cnpj,
        nomeFantasia=form.nomeFantasia,
        chavePix=form.chavePix,
        formacao=form.formacao,
        dataAniversario=form.dataAniversario,
        signo=form.signo
    )

    formacao_cadastrada.append(professores)
    return professores







#class ProfessoresEditar(BaseModel):
    #pass




















if __name__ == "__main__":
    uvicorn.run("main:app")
