# 📌 TAS - Telegram Automation Script 📌
 - Clonagem de Mensagens & Upload de Arquivos - 

🤖 Script por: Messias6 

### Disclaimer: 
 - Este script é apenas para fins educacionais. 
 - O uso para copiar conteúdos sem autorização pode violar os Termos do Telegram e leis locais. 
 - Use por sua conta e risco.
 - Não me responsabilizo pelo uso indevido deste script.
 - Se gostou, não esqueça de deixar uma ⭐ no repositório.
 - Se tiver dúvidas, sugestões ou relatar bugs, sinta-se à vontade para enviar e-mail ou pix para messias6@gmail.com.

 ## 🔹 O que este script faz?
 - Clona mensagens de um canal para outro.
 - Faz upload de arquivos ou pastas para o Telegram.
 - Gera e envia um sumário automático dos arquivos enviados.
 - Mostra progresso do upload em tempo real.
 - Permite pausar e continuar uploads interrompidos.

 ## 🔹 Passo a Passo para Usar o Script:
 - Você vai precisar de: Um computador com Windows (funciona em Linux e Mac também, mas vamos focar no Windows). Conexão com a internet para baixar os programas necessários. Nenhum conhecimento em programação – eu explico tudo do zero.
 
1️⃣ Baixar e Instalar o Python - Python é a linguagem que usaremos para rodar o script.
Passo a passo:
 - Acesse o site oficial do Python: 👉 https://www.python.org/downloads/
 - Clique no botão "Download Python" (a versão mais recente aparecerá automaticamente).
 - Durante a instalação, marque a opção "Add Python to PATH" (isso facilita a execução no CMD).
 - Clique em "Install Now" e aguarde a instalação.
 
2️⃣ Baixar e Instalar o VS Code (Opcional, mas Recomendado) - O Visual Studio Code (VS Code) é um programa que facilita a edição e execução do script.
Passo a passo:
 - Baixe o VS Code no site oficial: 👉 https://code.visualstudio.com/
 - Abra o instalador e clique em "Next" até concluir a instalação.
 - Na tela de seleção de componentes, marque a opção "Add to PATH" (isso facilita a execução).
 - Conclua a instalação e abra o VS Code.
   
3️⃣ Baixar o Script do GitHub - Agora precisamos baixar o script que será executado.
Passo a passo:
 - Acesse o repositório do projeto no GitHub pelo https://github.com/messias519/TAS---Telegram-Automation-Script
 - Clique no botão "Code" (botão verde).
 - Escolha a opção "Download ZIP" e aguarde o download.
 - Extraia a pasta do ZIP para um local fácil de encontrar (por exemplo, Área de Trabalho).
   
4️⃣ Instalar a Biblioteca Necessária - O script usa a biblioteca Telethon, então precisamos instalá-la.

Se você baixou o VS Code, siga este passo:
 - Abra o VS Code.
 - Clique em "File" → "Open Folder" e selecione a pasta onde salvou o script.
 - No VS Code, clique em "Terminal" → "New Terminal" (ou pressione Ctrl + J).
 - Digite o seguinte comando e pressione Enter:
   pip install telethon

Se você preferir usar o CMD/PowerShell:
 - Abra o CMD (Prompt de Comando) ou PowerShell.
 - Navegue até a pasta do script com este comando:
   cd "C:\Caminho\Para\A\PastadoScript"         # Exemplo: Se a pasta do script estiver na Área de Trabalho, digite: cd "C:\Users\SeuNome\Desktop\NomeDaPastaDoScript"
 - Instale a biblioteca Telethon:
   pip install telethon

5️⃣ Configurar o Script - Agora precisamos configurar o script para funcionar corretamente (abaixo um tutorial mais explicado sobre cada um dos itens a serem editados.
Passo a passo:
 - Abra a pasta do script no VS Code.
 - Abra o arquivo config.py (ou a classe Config dentro do script).
 - Substitua os valores necessários:
   API_ID = "0000000"  # Seu ID do Telegram
   API_HASH = "xxxaaa222"  # Seu Hash do Telegram
   PHONE_NUMBER = "+55DDNúmero"  # Seu número de telefone com código do país
   SRC_CHAT_ID = -1000000000000  # ID do canal de onde as mensagens serão clonadas
   DEST_CHAT_ID = -1000000000000  # ID do canal para onde as mensagens serão enviadas
   UPLOAD_PATH = r"C:\Users\User\Downloads\Arquivos"  # Caminho da pasta/arquivo a ser enviado
 - Salve as alterações (Ctrl + S).

6️⃣ Executar o Script - Agora vamos rodar o script.
Se você está usando o VS Code:
 - No VS Code, clique em "Terminal" → "New Terminal" (Ctrl + J). E digite:
   python script.py
 - Pressione Enter.

Se você está usando o CMD/PowerShell:
 - Abra o CMD (Prompt de Comando) ou PowerShell (pelo próprio executar ou a tecla win + r).
 - Navegue até a pasta do script com o comando:
  cd "C:\Caminho\Para\A\PastadoScript"
 - Execute o script:
  python script.py

🔹 Se tudo estiver correto, o menu do script aparecerá, e você poderá escolher entre clonar mensagens ou enviar arquivos! ✅

 ## 🔹 Como configurar?
 
     # API_ID = "0000000" 
         - Substitua pelo seu ID, ele pode ser  encontrado em https://my.telegram.org/apps
         - Crie um novo aplicativo e pegue o ID e o HASH. Coloque qualquer nome em: APP TITLE e SHORT NAME
    
     # API_HASH = "xxxaaa222"
         - Substitua pelo seu HASH gerado no site https://my.telegram.org/apps
    
     # PHONE_NUMBER = "+55DDNúmero"  
         - Substitua pelo seu número no telegram, incluindo o código do país e DD.
     # NAME = "User"
         - Nome do cliente, pode ser qualquer um.
    
     # SRC_CHAT_ID = -00000000000
         - ID do canal de origem, onde as mensagens serão clonadas. 
         - Pode ser encontrando com utilizado clientes de telegram como o 64Gram (https://github.com/TDesktop-x64/tdesktop), basta clicar no canal e copiar ID.
    
     # DEST_CHAT_ID = -00000000000
         - ID do canal de destino, onde as mensagens serão enviadas.
         - Pode ser encontrando com utilizado clientes de telegram como o 64Gram (https://github.com/TDesktop-x64/tdesktop), basta clicar no canal e copiar ID.
    
     # UPLOAD_PATH = r"LocalDoArquivoOuPasta"  
         - Pode ser arquivo ou pasta
         - Exemplo: r"C:\Users\User\Downloads\Arquivos" ou r"C:\Users\User\Downloads\Arquivos\Arquivo.pdf"
    
     # UPLOAD_STATE_FILE = os.path.join(os.path.dirname(__file__), "upload_state.json")
         - Caminho para o arquivo de estado do upload. Não altere a menos que necessário.
    
     # SUMMARY_FILE = os.path.join(os.path.dirname(__file__), "upload_summary.txt")
         - Caminho para o arquivo de sumário do upload. Não altere a menos que necessário.
    
     # START_CODE_NUMBER = 1  
         - Número inicial do código das legendas, utilizado para criar um código único para cada arquivo enviado e facilitar o sumário.
    
     # CODE_PREFIX = "F"  
         - Prefixo para o código (#F001, #G001, #Aula001, etc.)
         - Utilizado para facilitar a identificação dos arquivos enviados. 
