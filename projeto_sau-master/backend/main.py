from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
tutorias = [

        {
    "id": 1,
    "titulo": "Erro Siafi",
    "categoria": "SIGADAER",
    "descricao": "Tutorial de acesso ao sistema",
    "pdf": "pdfs/Tutorial_Siafi_erro_no_Download.pdf"
},
{
    "id": 2,
    "titulo": "Mapeamento de Pasta (Win 11)",
    "categoria": "Pasta de Rede",
    "descricao": "Como mapear pasta no Windows 11",
    "pdf": "pdfs/mapeamento_win11.pdf"
},
{
    "id": 3,
    "titulo": "Mapeamento de Pasta (Win 10)",
    "categoria": "Pasta de Rede",
    "descricao": "Como mapear pasta no Windows 10",
    "pdf": "pdfs/mapeamento_win10.pdf"
},
{
    "id": 4,
    "titulo": "Configurar Java",
    "categoria": "Java",
    "descricao": "Como configurar Java",
    "pdf": "pdfs/tutorial_java_excecoes.pdf"
},
{
    "id": 5,
    "titulo": "Windows Update",
    "categoria": "Windows",
    "descricao": "Corrigir erro de download",
    "pdf": "pdfs/erro_download_software.pdf"
},
{
    "id": 6,
    "titulo": "Token GDS",
    "categoria": "Token",
    "descricao": "Configuração do Token",
    "pdf": "pdfs/token_gds.pdf"
},
{
    "id": 7,
    "titulo": "Token GD",
    "categoria": "Token",
    "descricao": "Configuração do Token",
    "pdf": "pdfs/token_gd.pdf"
},
{
    "id": 8,
    "titulo": "Token Dexon",
    "categoria": "Token",
    "descricao": "Configurar token Dexon",
    "pdf": "pdfs/token_dexon.pdf"
},
{
    "id": 9,
    "titulo": "Erro Extensão Assinador",
    "categoria": "SIGADAER",
    "descricao": "Corrigir extensão",
    "pdf": "pdfs/erro_extensao_assinador.pdf"
},
{
    "id": 10,
    "titulo": "Erro Assinador Serpro",
    "categoria": "SIGADAER",
    "descricao": "Corrigir assinador",
    "pdf": "pdfs/erro_assinador_serpro.pdf"
},
{
    "id": 11,
    "titulo": "Facilidades VOIP",
    "categoria": "VOIP",
    "descricao": "Tutorial VOIP",
    "pdf": "pdfs/facilidades_voip.pdf"
},
{
    "id": 12,
    "titulo": "Solicitação de Login",
    "categoria": "Login",
    "descricao": "Solicitar login",
    "pdf": "pdfs/solicitacao_login.pdf"
}
   
    
]

@app.get("/")
def inicio():
    return {"mensagem": "Portal TI FAB funcionando"}

@app.get("/tutoriais")
def listar_tutorias():
    return tutorias

@app.get("/tutoriais/{tutorial_id}")
def buscar_tutorial (tutorial_id:int):

    for tutorial in tutorias:
        if tutorial["id"] == tutorial_id:
            return tutorial
    return {"erro":"Tutorial não encontrado"}

