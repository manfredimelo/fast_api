from typing import Optional, Any, Dict, List

from fastapi import FastAPI, HTTPException, status, Response, Path, Query, Header, Depends
from time import sleep
# from starlette.responses import JSONResponse

from models import Curso, cursos


def fake_deb():
    try:
        print('Abrindo conexão do banco de daods...')
        sleep(1)
    finally:
        print('Fechando conexão com banco de dados...')
        sleep(1)


app = FastAPI(
    title='API FAST',
    version='0.0.1',
    description='Estudando Fast'
)



@app.get('/cursos',
         description='Retorna todos os cursos',
         summary='Retorna todod os cusros',
         response_model=List[Curso],
         response_description='Cursos encontrados'
         )
async def get_cursos(db: Any = Depends(fake_deb)):
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(default=None,
                                         title='ID do curso',
                                         description='Deve ser entre 1 e 2',
                                         gt=0,
                                         lt=3,
                                         ), db: Any = Depends(fake_deb)
                    ):
    try:
        return cursos[curso_id]
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    # curso.update({"id": curso_id})


@app.post('/cursos', status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    curso.id =next_id
    cursos.append(cursos)
    return curso



@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_deb)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        curso.id = curso_id
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT) # Etto na implementação na versão do fast
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe um curso com id {curso_id}')


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fake_deb)):
    if curso_id in cursos:
        del cursos[curso_id]
        return
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe um curso com id {curso_id}')


@app.get('/calculadora')
async def calcular(a: int = Query(default=0, gt=5), b: int = Query(default=0, gt=10),
                   x_geek: str = Header(default=None), c: Optional[int] = 0
                   ):
    soma = a + b + c
    print(f'X_GEEG :{x_geek}')
    return {"resultado": soma}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, debug=True, log_level="info", reload=True)
    # unicorn main:app -w 4 -k uvicorn.workers.Uvicornworker
