
from imap_tools import MailBox, AND

usuario = "seu_email"
senha = "sua_senha"

meu_email = MailBox("imap.gmail.com").login(usuario, senha)

#Pegar email que foram enviados por um remetente específico
lista_emails = meu_email.fetch(AND(from_="seu_email"))
for email in lista_emails:
    if len(email.attachments) > 0:
        for anexo in email.attachments:
            if "fatura" in anexo.filename:
                print(anexo.content_type)
                print(anexo.payload)
                with open("Teste.doc", 'wb') as arquivo_docx:
                    arquivo_docx.write(anexo.payload)
