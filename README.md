<div align="center">

# 🤖 leyley bot

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Telegram](https://img.shields.io/badge/telegram-bot-26A5E4.svg)](https://telegram.org)

bot de telegram feito em python, com o objetivo de fornecer ferramentas úteis e entretenimento aos usuários

</div>

---
#📥 instalação
## instalação no android
 1- baixe o aplivativo "termux" no site fdroid.org
 [link direto] (https://f-droid.org/packages/com.termux/)
 alias caso você esteja vendo isso depois da google implementar a política nova política de apks (previsto para setembro de 2026), sinto muito provavelmente não irá conseguir usar o software recomendo que começe a usar uma custom rom e recupere sua liberdade. 

 2- apos instalar o aplicativo abra ele e digite os seguintes comandos em ordem
 primeiro:
 ```bash
    pkg update && pkg upgrade -y
 ```
 seguindo:
 ```bash
   pkg install git python -y
```
 terceiro e quarto:
 ```bash
 git clone https://github.com/nullbyteSec1/leyley_bot && cd leyley_bot
```
```bash
  pip install httpx python-telegram-bot scraping34=2.0
``` 
## criando token

agora entre no seu telegram e inicie um chat com o @BotFather

use o comando /newbot, ele irá te perguntar o nickname qe deseja dar a ele, escolha e você receberá um token de acesso
na pasta do bot você ira notar que existe um arquivo chamado "config.json", troque o lcoal em que estar o texto "seu-token-aqui" pelo token verdadeiro 

lembrando esse token dar acesso total a conta fo seu bot  NÃO COMPARTILHE ELE COM NINGUÉM

## iniciando bot
para iniciar use o comando
```bash
python bot.py
```

