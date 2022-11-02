class TratamentoDados():
    def __init__(self, caminho_csv: str) -> None:
        self.caminho_csv = caminho_csv
        self.dados_alunos = []

    def lendoCsv(self) -> None:
        with open(self.caminho_csv, 'r') as arquivo_csv:
            for linha in arquivo_csv:
                nome, cpf, curso, data_inicio, data_fim, ch_total = linha.split(",")
                molde = {
                    "nome": nome,
                    "cpf": cpf,
                    "curso": curso,
                    "data_inicio": data_inicio,
                    "data_fim": data_fim,
                    "ch_total": ch_total.replace('\n', '')
                }
                self.dados_alunos.append(molde)