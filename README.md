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

 ## 🔹 Como usar este script?
 
 1️⃣ Instale o Python (https://www.python.org/downloads/)
 
 2️⃣ Instale as dependências: pip install telethon
 
 3️⃣ Edite a classe Config.
 
 4️⃣ Execute o script: python script.py

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
