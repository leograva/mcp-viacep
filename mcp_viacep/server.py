from fastmcp import FastMCP
import requests

app = FastMCP("ViaCEP")

@app.tool()
def buscar_cep(cep: str) -> dict:
    """Busca endereço pelo CEP."""
    cep = cep.replace("-", "").replace(".", "").strip()
    
    if len(cep) != 8 or not cep.isdigit():
        return {"erro": "CEP inválido"}
    
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        data = response.json()
        return {"erro": "CEP não encontrado"} if "erro" in data else data
    except:
        return {"erro": "Erro na consulta"}

def main():
    app.run()

if __name__ == "__main__":
    main()