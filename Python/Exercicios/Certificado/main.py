from models.tratamentoDados import TratamentoDados
from models.criarCertificado import CriarCertificado
from datetime import date
def main():
    print(f"Informe o DIRETÓRIO do arquivo .CSV \nEx. de Teste: ../Certificado/molde/Dados_Alunos.csv")
    caminho_csv = str(input("-> "))
    print(f"Informe o DIRETÓRIO do arquivo .jpg \nEx. de Teste: ../Certificado/molde/certificado_molde.jpg")
    caminho_img = str(input("-> "))

    print("Gerando certificados...")

    dados = TratamentoDados(caminho_csv)   
    dados.lendoCsv()
    
    certificado = CriarCertificado(caminho_img, dados)
    
    print("Certificados gerados com sucesso!") if certificado.gerarCertificado() else print("Erro ao gerar certificados!")


if __name__ == "__main__":
    main()