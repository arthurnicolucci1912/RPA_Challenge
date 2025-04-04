![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-1D6F42?style=for-the-badge&logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)


RPA Challenge Automation
Este projeto é um script em Python que automatiza o preenchimento de formulários no site RPA Challenge utilizando a biblioteca Selenium.
O script lê os dados de um arquivo Excel e preenche os campos do formulário automaticamente.

✅ Funcionalidades
Lê dados de uma planilha .xlsx com pandas e openpyxl

Automatiza o navegador Google Chrome via Selenium

Preenche dinamicamente os campos do formulário

Gera logs de erros para facilitar o debug

📋 Pré-requisitos
Python 3.7 ou superior

Google Chrome instalado

ChromeDriver compatível com sua versão do Chrome e adicionado ao PATH

Bibliotecas Python (instale com o pip):

bash
Copiar
Editar
pip install -r requirements.txt
🛠 Instalação
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/rpa-challenge-automation.git
cd rpa-challenge-automation
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Certifique-se de que o arquivo challenge.xlsx esteja no caminho correto especificado no script:

txt
Copiar
Editar
C:\Users\SE189129\Documents\_VEXIA\PYTHON\Selenium\Projetos\_RPACH_arthur_CERTO\docs\challenge.xlsx
▶️ Como usar
Execute o script no terminal:

bash
Copiar
Editar
python RPAChallenge.py
O navegador abrirá automaticamente e começará a preencher os formulários.

Ao final, ele será fechado automaticamente após uma pausa de 10 segundos.

📁 Estrutura do Projeto
bash
Copiar
Editar
rpa-challenge-automation/
│
├── RPAChallenge.py              # Script principal de automação
├── docs/
│   └── challenge.xlsx           # Planilha com os dados de entrada
├── error_log.txt                # Log de erros na leitura do Excel
├── field_erro_log.txt           # Log de erros nos campos do formulário
└── requirements.txt             # Lista de dependências do projeto
⚠️ Observações
O campo field_erro_log.txt é gerado caso algum campo do formulário não seja preenchido corretamente.

Sempre verifique se o ChromeDriver está atualizado e compatível com a versão do seu navegador Chrome.

Caso tenha problemas com leitura do Excel ou preenchimento, consulte os arquivos de log.

🤝 Contribuição
Contribuições são sempre bem-vindas!
Abra uma issue ou envie um pull request com melhorias, correções ou sugestões.

📄 Licença
Este projeto está licenciado sob a MIT License.
Consulte o arquivo LICENSE para mais informações.