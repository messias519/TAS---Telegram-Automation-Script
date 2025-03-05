# # 📌 TAS - Telegram Automation Script 📌
#  - Clonagem de Mensagens & Upload de Arquivos - 

# 🤖 Script por: Messias6 

# ### Disclaimer: 
#  - Este script é apenas para fins educacionais. 
#  - O uso para copiar conteúdos sem autorização pode violar os Termos do Telegram e leis locais. 
#  - Use por sua conta e risco.
#  - Não me responsabilizo pelo uso indevido deste script.
#  - Se gostou, não esqueça de deixar uma ⭐ no repositório.
#  - Se tiver dúvidas, sugestões ou relatar bugs, sinta-se à vontade para enviar e-mail ou pix para messias6@gmail.com.

#  ## 🔹 O que este script faz?
#  - Clona mensagens de um canal para outro.
#  - Faz upload de arquivos ou pastas para o Telegram.
#  - Gera e envia um sumário automático dos arquivos enviados.
#  - Mostra progresso do upload em tempo real.
#  - Permite pausar e continuar uploads interrompidos.

#  ## 🔹 Passo a Passo para Usar o Script:
#  - Você vai precisar de: Um computador com Windows (funciona em Linux e Mac também, mas vamos focar no Windows). Conexão com a internet para baixar os programas necessários. Nenhum conhecimento em programação – eu explico tudo do zero.
 
# 1️⃣ Baixar e Instalar o Python - Python é a linguagem que usaremos para rodar o script.
# Passo a passo:
#  - Acesse o site oficial do Python: 👉 https://www.python.org/downloads/
#  - Clique no botão "Download Python" (a versão mais recente aparecerá automaticamente).
#  - Durante a instalação, marque a opção "Add Python to PATH" (isso facilita a execução no CMD).
#  - Clique em "Install Now" e aguarde a instalação.
 
# 2️⃣ Baixar e Instalar o VS Code (Opcional, mas Recomendado) - O Visual Studio Code (VS Code) é um programa que facilita a edição e execução do script.
# Passo a passo:
#  - Baixe o VS Code no site oficial: 👉 https://code.visualstudio.com/
#  - Abra o instalador e clique em "Next" até concluir a instalação.
#  - Na tela de seleção de componentes, marque a opção "Add to PATH" (isso facilita a execução).
#  - Conclua a instalação e abra o VS Code.
   
# 3️⃣ Baixar o Script do GitHub - Agora precisamos baixar o script que será executado.
# Passo a passo:
#  - Acesse o repositório do projeto no GitHub pelo https://github.com/messias519/TAS---Telegram-Automation-Script
#  - Clique no botão "Code" (botão verde).
#  - Escolha a opção "Download ZIP" e aguarde o download.
#  - Extraia a pasta do ZIP para um local fácil de encontrar (por exemplo, Área de Trabalho).
   
# 4️⃣ Instalar a Biblioteca Necessária - O script usa a biblioteca Telethon, então precisamos instalá-la.

# Se você baixou o VS Code, siga este passo:
#  - Abra o VS Code.
#  - Clique em "File" → "Open Folder" e selecione a pasta onde salvou o script.
#  - No VS Code, clique em "Terminal" → "New Terminal" (ou pressione Ctrl + J).
#  - Digite o seguinte comando e pressione Enter:
#    pip install telethon

# Se você preferir usar o CMD/PowerShell:
#  - Abra o CMD (Prompt de Comando) ou PowerShell.
#  - Navegue até a pasta do script com este comando:
#    cd "C:\Caminho\Para\A\PastadoScript"         # Exemplo: Se a pasta do script estiver na Área de Trabalho, digite: cd "C:\Users\SeuNome\Desktop\NomeDaPastaDoScript"
#  - Instale a biblioteca Telethon:
#    pip install telethon

# 5️⃣ Configurar o Script - Agora precisamos configurar o script para funcionar corretamente (abaixo um tutorial mais explicado sobre cada um dos itens a serem editados.
# Passo a passo:
#  - Abra a pasta do script no VS Code.
#  - Abra o arquivo config.py (ou a classe Config dentro do script).
#  - Substitua os valores necessários:
#    API_ID = "0000000"  # Seu ID do Telegram
#    API_HASH = "xxxaaa222"  # Seu Hash do Telegram
#    PHONE_NUMBER = "+55DDNúmero"  # Seu número de telefone com código do país
#    SRC_CHAT_ID = -1000000000000  # ID do canal de onde as mensagens serão clonadas
#    DEST_CHAT_ID = -1000000000000  # ID do canal para onde as mensagens serão enviadas
#    UPLOAD_PATH = r"C:\Users\User\Downloads\Arquivos"  # Caminho da pasta/arquivo a ser enviado
#  - Salve as alterações (Ctrl + S).

# 6️⃣ Executar o Script - Agora vamos rodar o script.
# Se você está usando o VS Code:
#  - No VS Code, clique em "Terminal" → "New Terminal" (Ctrl + J). E digite:
#    python script.py
#  - Pressione Enter.

# Se você está usando o CMD/PowerShell:
#  - Abra o CMD (Prompt de Comando) ou PowerShell (pelo próprio executar ou a tecla win + r).
#  - Navegue até a pasta do script com o comando:
#   cd "C:\Caminho\Para\A\PastadoScript"
#  - Execute o script:
#   python script.py

# 🔹 Se tudo estiver correto, o menu do script aparecerá, e você poderá escolher entre clonar mensagens ou enviar arquivos! ✅

#  ## 🔹 Como configurar?
 
#      # API_ID = "0000000" 
#          - Substitua pelo seu ID, ele pode ser  encontrado em https://my.telegram.org/apps
#          - Crie um novo aplicativo e pegue o ID e o HASH. Coloque qualquer nome em: APP TITLE e SHORT NAME
    
#      # API_HASH = "xxxaaa222"
#          - Substitua pelo seu HASH gerado no site https://my.telegram.org/apps
    
#      # PHONE_NUMBER = "+55DDNúmero"  
#          - Substitua pelo seu número no telegram, incluindo o código do país e DD.
#      # NAME = "User"
#          - Nome do cliente, pode ser qualquer um.
    
#      # SRC_CHAT_ID = -00000000000
#          - ID do canal de origem, onde as mensagens serão clonadas. 
#          - Pode ser encontrando com utilizado clientes de telegram como o 64Gram (https://github.com/TDesktop-x64/tdesktop), basta clicar no canal e copiar ID.
    
#      # DEST_CHAT_ID = -00000000000
#          - ID do canal de destino, onde as mensagens serão enviadas.
#          - Pode ser encontrando com utilizado clientes de telegram como o 64Gram (https://github.com/TDesktop-x64/tdesktop), basta clicar no canal e copiar ID.
    
#      # UPLOAD_PATH = r"LocalDoArquivoOuPasta"  
#          - Pode ser arquivo ou pasta
#          - Exemplo: r"C:\Users\User\Downloads\Arquivos" ou r"C:\Users\User\Downloads\Arquivos\Arquivo.pdf"
    
#      # UPLOAD_STATE_FILE = os.path.join(os.path.dirname(__file__), "upload_state.json")
#          - Caminho para o arquivo de estado do upload. Não altere a menos que necessário.
    
#      # SUMMARY_FILE = os.path.join(os.path.dirname(__file__), "upload_summary.txt")
#          - Caminho para o arquivo de sumário do upload. Não altere a menos que necessário.
    
#      # START_CODE_NUMBER = 1  
#          - Número inicial do código das legendas, utilizado para criar um código único para cada arquivo enviado e facilitar o sumário.
    
#      # CODE_PREFIX = "F"  
#          - Prefixo para o código (#F001, #G001, #Aula001, etc.)
#          - Utilizado para facilitar a identificação dos arquivos enviados. 

#### Código do Script:


import os
import time
import json
import logging
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError as FloodWait

# Configurações do bot
class Config:
    API_ID = "xx"  # Substitua pelo seu ID
    API_HASH = "xx"  # Substitua pelo seu HASH
    PHONE_NUMBER = "xx"  # Substitua pelo seu número
    NAME = "xx"  # Nome do cliente
    SRC_CHAT_ID = -0000000  # ID do canal de origem
    DEST_CHAT_ID = -0000000  # ID do canal de destino
    UPLOAD_PATH = r"C:\Users\User\Downloads\Arquivos"  # Pode ser arquivo ou pasta
    UPLOAD_STATE_FILE = os.path.join(os.path.dirname(__file__), "upload_state.json")
    SUMMARY_FILE = os.path.join(os.path.dirname(__file__), "upload_summary.txt")
    START_CODE_NUMBER = 1  # Número inicial do código das legendas
    CODE_PREFIX = "F"  # Prefixo para o código (#F001, #G001, #Aula001, etc.)

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from telethon.tl.types import MessageService

def clone_messages():
    """Clona mensagens de um canal para outro."""
    with TelegramClient(Config.NAME, Config.API_ID, Config.API_HASH) as client:
        logging.info("Iniciando clonagem de mensagens...")
        total_sent = 0
        for message in client.iter_messages(Config.SRC_CHAT_ID, reverse=True):
            if isinstance(message, MessageService):
                continue
            try:
                client.send_message(Config.DEST_CHAT_ID, message)
                total_sent += 1
                if total_sent % 50 == 0:
                    logging.info(f"{total_sent} mensagens clonadas. Pausando 5s para evitar spam...")
                    time.sleep(5)
            except FloodWait as e:
                logging.warning(f"Telegram impôs um limite. Aguardando {e.seconds} segundos...")
                time.sleep(e.seconds)
        logging.info(f"Clonagem concluída! Total de mensagens clonadas: {total_sent}")

def format_file_size(size_in_bytes):
    """Formata o tamanho do arquivo para KB ou MB."""
    size_in_kb = size_in_bytes / 1024
    if size_in_kb > 1024:
        return f"{size_in_kb / 1024:.2f}MB"
    return f"{size_in_kb:.2f}KB"

def save_upload_state(uploaded_files):
    """Salva o estado do upload para retomada posterior."""
    with open(Config.UPLOAD_STATE_FILE, "w") as f:
        json.dump(uploaded_files, f)

def load_upload_state():
    """Carrega o estado do upload para continuar de onde parou."""
    if os.path.exists(Config.UPLOAD_STATE_FILE):
        with open(Config.UPLOAD_STATE_FILE, "r") as f:
            return json.load(f)
    return []

def save_summary(summary):
    """Salva o sumário do upload para retomada posterior."""
    with open(Config.SUMMARY_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(summary))

def load_summary():
    """Carrega o sumário salvo para continuar de onde parou."""
    if os.path.exists(Config.SUMMARY_FILE):
        with open(Config.SUMMARY_FILE, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    return []

def upload_files():
    """Faz upload de arquivos ou pastas para o Telegram, gerando sumário com progresso."""
    choice = input("Deseja iniciar um novo upload? (S/N): ").strip().lower()
    if choice == 's':
        uploaded_files = []  # Inicia um novo upload
        sumario = []  # Reseta o sumário
        if os.path.exists(Config.UPLOAD_STATE_FILE):
            os.remove(Config.UPLOAD_STATE_FILE)  # Remove estado anterior
        if os.path.exists(Config.SUMMARY_FILE):
            os.remove(Config.SUMMARY_FILE)  # Remove sumário anterior
    else:
        uploaded_files = load_upload_state()
        sumario = load_summary()
    
    path = Config.UPLOAD_PATH
    
    if not os.path.exists(path):
        logging.error(f"Caminho não encontrado! Caminho recebido: {path}")
        return
    
    file_list = []
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                file_list.append(os.path.join(root, file))
    else:
        file_list.append(path)
    
    if not file_list:
        logging.warning("Nenhum arquivo encontrado para upload.")
        return
    
    with TelegramClient(Config.NAME, Config.API_ID, Config.API_HASH) as client:
        logging.info("Iniciando upload de arquivos...")
        code_number = Config.START_CODE_NUMBER
        
        for file_path in file_list:
            if file_path in uploaded_files:
                logging.info(f"Pulando arquivo já enviado: {file_path}")
                continue
            try:
                file_name = os.path.basename(file_path)
                file_size = format_file_size(os.path.getsize(file_path))
                caption = f"#{Config.CODE_PREFIX}{code_number:03} - {file_name} - Tamanho {file_size}"
                logging.info(f"Enviando: {caption}")
                
                start_time = time.time()  # Início do tempo de envio
                
                def progress_callback(sent_bytes, total_bytes):
                    # Atualiza a barra de progresso no terminal com % enviada, velocidade e tempo estimado restante.
                    elapsed_time = time.time() - start_time  # Tempo decorrido
                    percent = (sent_bytes / total_bytes) * 100  # Percentual enviado
                    
                    # Calcula velocidade de envio
                    speed = sent_bytes / elapsed_time if elapsed_time > 0 else 0
                    speed_formatted = f"{speed / 1024:.2f} KB/s" if speed < 1048576 else f"{speed / 1048576:.2f} MB/s"

                    # Estimativa de tempo restante
                    remaining_time = ((total_bytes - sent_bytes) / speed) if speed > 0 else 0
                    remaining_time_formatted = time.strftime("%M:%S", time.gmtime(remaining_time))

                    # Atualiza a barra de progresso no terminal
                    print(f"\r📤 {percent:.2f}% enviado - Velocidade: {speed_formatted} - Tempo restante: {remaining_time_formatted}", end="", flush=True)
                
                client.send_file(Config.DEST_CHAT_ID, file_path, caption=caption, progress_callback=progress_callback)
                uploaded_files.append(file_path)
                save_upload_state(uploaded_files)
                logging.info(f"Arquivo enviado: {caption}")
                code_number += 1
                time.sleep(2)
            except Exception as e:
                logging.error(f"Erro ao enviar {file_name}: {e}")
                save_upload_state(uploaded_files)
                break

def main_menu():
    """Menu interativo para o usuário escolher uma ação."""
    while True:
        print(("\n" + "-" * 80))
        print("Bem-vindo ao ATS - Telegram Automation Script!")
        print(("-" * 80))
        print("# Não se esqueça de configurar as variáveis de ambiente antes de iniciar.")
        print("# Não me responsabilizo pelo uso indevido deste script.")	
        print(("-" * 80))
        print("Escolha uma opção:")
        print("1 - Clonar mensagens")
        print("2 - Fazer upload de arquivos ou enviar um único arquivo")
        print("3 - Sair")

        choice = input("\n" + "Digite sua escolha: " + "\n" )
        try:
            if choice == "1":
                clone_messages()
            elif choice == "2":
                upload_files()
            elif choice == "3":
                print("Saindo...")
                break
            else:
                print("❌ Opção inválida! Tente novamente.")
        except Exception as e:
            print(f"⚠️ Ocorreu um erro: {e}")

if __name__ == "__main__":
    main_menu()
