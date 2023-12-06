from typing import Optional

from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título tem que ter pelo menos 3 palavras')
        return value


cursos = [
    Curso(id=1, titulo='Curso 1 teste', aulas=112, horas=58),
    Curso(id=2, titulo='Curso 2 teste', aulas=112, horas=58),
    Curso(id=3, titulo='Curso 3 teste', aulas=112, horas=58),
]
