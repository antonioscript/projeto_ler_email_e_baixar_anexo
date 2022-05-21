from imap_tools import MailBox, AND

usuario = "antoniojunior159@gmail.com"
senha = "simboloperdido852"

meu_email = MailBox("imap.gmail.com").login(usuario, senha)

#Pegar email que foram enviados por um remetente específico
# pegar emails com um anexo específico
lista_emails = meu_email.fetch(AND(from_="antoniojunior159@gmail.com"))
for email in lista_emails:
    if len(email.attachments) > 0:
        for anexo in email.attachments:
            if "fatura" in anexo.filename:
                print(anexo.content_type)
                print(anexo.payload)
                with open("Teste.doc", 'wb') as arquivo_docx:
                    arquivo_docx.write(anexo.payload)
#Pegar anexo de um emal
