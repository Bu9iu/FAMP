from fastapi import FastAPI 
from fastapi import Response
from fastapi import HTTPException
from fastapi import status

from models import Curso

app = FastAPI()

cursos = {
    1:{
        "titulo": "Python",
        "aulas": 12,
        "horas": 60     
    },
    2:{
        "titulo": "Python",
        "aulas": 12,
        "horas": 60
    },
    3:{
        "titulo": "Python",
        "aulas": 12,
        "horas": 60
    },
    4:{
        "titulo": "Python",
        "aulas": 12,
        "horas": 60
    }
}

@app.get("/cursos")
async def get_cursos():
    return cursos

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso nao encontrado")
    
@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    if curso.id in cursos:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Curso ja existe")
    cursos[curso.id] = curso
    return curso

@app.put("/cursos/{curso_id}", status_code=status.HTTP_200_OK)
async def put_curso(curso_id: int, curso: Curso):
    if curso.id not in cursos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso nao encontrado")
    cursos[curso.id] = curso
    return curso

@app.delete("/cursos/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int):
    if curso_id not in cursos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso nao encontrado")
    del cursos[curso_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)