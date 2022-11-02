from models.tratamentoDados import TratamentoDados
from PIL import Image, ImageDraw, ImageFont
import img2pdf 
import os 
from datetime import date

class CriarCertificado():
    def __init__(self, arquivo_img: str, dados: TratamentoDados) -> None:
        self.arquivo_img = arquivo_img
        self.dataemissao = self.dataAtual()
        self.dados = dados

    def dataAtual(self) -> list:
        mes_ext = {
            1: 'Janeiro',
            2: 'Fevereiro', 
            3: 'Março', 
            4: 'Abril', 
            5: 'Maio', 
            6: 'Junho', 
            7: 'Julho', 
            8: 'Agosto', 
            9: 'Setembro', 
            10: 'Outubro', 
            11: 'Novembro', 
            12: 'Dezembro'
            }
        hoje = str(date.today())
        aaa, mm, dd = hoje.split("-")
        return dd, mes_ext[int(mm)], aaa

    def modelarCertificadoPdf(self, nome_pasta: str) -> None:
        # Abri a imagem
        imagem_certificado = Image.open(nome_pasta+"/certificado.jpg")
        # convertendo para PDF
        pdf_bytes = img2pdf.convert(imagem_certificado.filename) 
        file = open(nome_pasta+"/certificado.pdf", "wb") 
        file.write(pdf_bytes) 
        # Fechando os arquivos
        imagem_certificado.close()
        file.close()

    def gerarCertificado(self) -> bool:
        for cont, dados in enumerate(self.dados.dados_alunos):
            # Abri a imagem
            imagem = Image.open(self.arquivo_img)
            texto_certificado = ["Certificamos que", f"{dados['nome']},", "CPF", f"{dados['cpf']},", "participou, como CURSISTA, do Projeto", "de  extensão  contínuo", f"{dados['curso']}, ", "coordenado por FELIPE  GONÇALVES  DOS  SANTOS, selecionado através do", "EDITAL  Nº  03/2020/PROEN/IFS -\n", "PROGRAMA   INSTITUCIONAL   DE  PESQUISA   MULTIDISCIPLINAR   DE  APOIO  AO   ENSINO,", "no  período", "de", f"{dados['data_inicio']} a {dados['data_fim']},", f" com uma carga horária total de {dados['ch_total']} horas.", f"Corrente - PI, {self.dataemissao[0]} de {self.dataemissao[1]} de {self.dataemissao[2]}.", "_"*30, "Felipe Gonçalvesdos Santos", "Coordenador do Curso", "IFPI - Campus Corrente", "_"*30, "Israel Lobato Rocha", "Diretor Geral", "IFPI - Campus Corrente"]
            # Abrir para sobreposição
            draw = ImageDraw.Draw(imagem)
            # Setar a fonte
            fonte = ImageFont.truetype('../Certificado/molde/Roboto/Roboto-Medium.ttf', 40)
            fonte_negrito = ImageFont.truetype('../Certificado/molde/Roboto/Roboto-Black.ttf', 40)
            # 1º Linha
            draw.text((250, 800), texto_certificado[0], (0, 0, 0), font=fonte)
            draw.text((570, 800), texto_certificado[1], (0, 0, 0), font=fonte_negrito)
            draw.text((1145, 800), texto_certificado[2], (0, 0, 0), font=fonte)
            draw.text((1230, 800), texto_certificado[3], (0, 0, 0), font=fonte_negrito)
            draw.text((1550, 800), texto_certificado[4], (0, 0, 0), font=fonte)
            # 2º Linha
            draw.text((250, 850), texto_certificado[5], (0, 0, 0), font=fonte)
            draw.text((670, 850), texto_certificado[6], (0, 0, 0), font=fonte_negrito)
            # 3º Linha
            draw.text((250, 900), texto_certificado[7], (0, 0, 0), font=fonte)
            draw.text((1635, 900), texto_certificado[8], (0, 0, 0), font=fonte_negrito)
            # 4º Linha
            draw.text((250, 950), texto_certificado[9], (0, 0, 0), font=fonte_negrito)
            draw.text((1980, 950), texto_certificado[10], (0, 0, 0), font=fonte)
            draw.text((2200, 950), texto_certificado[11], (0, 0, 0), font=fonte_negrito)
            # 5º Linha
            draw.text((250, 1000), texto_certificado[12], (0, 0, 0), font=fonte_negrito)
            draw.text((730, 1000), texto_certificado[13], (0, 0, 0), font=fonte)
            # Linha da data
            draw.text((940, 1150), texto_certificado[14], (0, 0, 0), font=fonte)
            # Linha Coordenador do Curso
            draw.text((450, 1300), texto_certificado[15], (0, 0, 0), font=fonte)
            draw.text((465, 1350), texto_certificado[16], (0, 0, 0), font=fonte_negrito)
            draw.text((520, 1400), texto_certificado[17], (0, 0, 0), font=fonte)
            draw.text((515, 1450), texto_certificado[18], (0, 0, 0), font=fonte)
            # Linha Coordenador do Curso
            draw.text((1450, 1300), texto_certificado[19], (0, 0, 0), font=fonte)
            draw.text((1550, 1350), texto_certificado[20], (0, 0, 0), font=fonte_negrito)
            draw.text((1620, 1400), texto_certificado[21], (0, 0, 0), font=fonte)
            draw.text((1520, 1450), texto_certificado[22], (0, 0, 0), font=fonte)
            # Salvar a imagem
            nome_pasta = f"../Certificado/out/{cont+1}_{'_'.join((dados['nome'].split())[0:2])}"
            os.mkdir(nome_pasta)
            imagem.save(nome_pasta+"/certificado.jpg")
            self.modelarCertificadoPdf(nome_pasta)
            # Fechando os arquivos
            imagem.close()
        return True