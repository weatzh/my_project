# 간단한 홈페이지 제공
# 1. 모듈 가져오기
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles # 정적 데이터 처리 모듈

# 2. Fastapi 객체 생성, 전역변수 생성
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static") # 정적데이터 경로설정


# 3. 라우팅 구성/정의
@app.get("/")
def home(req:Request):
    # 홈페이지("/") get 방식 요청 -> 매칭되는 함수 home() 호출됨
    # 홈페이지 요청 -> index.html을 읽어서 req 데이터를 전달하여 동적 html 구성 
    # -> 응답(return) -> 클라이언트 브라우저에게 전달 -> 랜더링, Dom tree
    # -> 브라우저 해석 화면에 그리기 -> 클라이언트는 응답된 결과를 화면에서 볼수있다
    return templates.TemplateResponse(req,"index.html")


@app.get("/auth/login")
def login(req:Request):
    return templates.TemplateResponse(req,"login.html")