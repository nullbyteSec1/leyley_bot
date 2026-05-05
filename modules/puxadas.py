import httpx
from telegram import Update
from telegram.ext import ContextTypes
import json


async def puxada_cep(target_cep:str ,update: Update,context: ContextTypes.DEFAULT_TYPE):
    if not target_cep:
        await update.reply_message("error use /cep <cep_que_deseja_consultar ")
    try:
      resp = httpx.get(f"https://viacep.com.br/ws/{cep}/json/")
      data = resp.json()

      estado = data.get("locaridade")
      ddd = data.get("ddd")
      regiao = data.get("regiao")
      bairro = data.get("bairro")

      template_resp = f"""
✅CONSULTA REALIZADA COM SUCESSO✅
CEP {target_cep}
estado:{estado}
região:{regiao}
bairro:{bairro}
ddd:{ddd}
by leyley_bot
"""
      await update.message.reply_message(template_resp)
    except httpx.ConnectError:
      await update.message.reply_message("Erroa consultar api")


async def puxada_ip(target_ip:str,update: Update,context:ContextTypes.DEFAULT_TYPE):
    if not target_ip:
        await update.reply_message("error use /ip <ip_que_deseja_consultar>")
    try:
      resp = httpx.get(f"http://ip-api.com/json/{target_ip}")
      data = resp.json()

      country = data.get("coutry")
      region_name = data.get("regionName")
      city = data.get("city")
      lat = data.get("lat")
      lon = data.get("lon")
      isp = data.get("isp")

      template_resp = f"""
✅CONSULTA REALIZADA COM SUCESSO✅

ip:{target_ip}
pais:{country}
estado/região:{region_name}
cidade:{city}
latitude:{lat}
longitude:{lon}
isp:{isp}

by leyley 404
      """
      await update.message.reply_text(template_resp)
    except httpx.ConnectError:
        await update.message.reply_message("erro a consultar api")


async def puxada_cnpj(target_cnpj: str, update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not target_cnpj:
        await update.message.reply_text("CNPJ inválido.")
        return

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"https://www.receitaws.com.br/v1/cnpj/{target_cnpj}", timeout=10)

        data = resp.json()

        if data.get("status") == "ERROR":
            await update.message.reply_text(f"Erro: {data.get('message')}")
            return

        abertura = data.get("abertura")
        situacao = data.get("situacao")
        nome = data.get("nome")
        cep = data.get("cep")
        email = data.get("email")

        atividades = []
        diretores = []

        for atividade in data.get("atividades_secundarias", []):
            atividades.append(atividade.get("text"))

        for pessoa in data.get("qsa", []):
            diretores.append(f"{pessoa.get('nome')} - {pessoa.get('qual')}")

        resposta = f"""
📌 Nome: {nome}
📅 Abertura: {abertura}
📊 Situação: {situacao}
📍 CEP: {cep}
📧 Email: {email}

📚 Atividades:
{chr(10).join(atividades) if atividades else "Nenhuma"}

👥 QSA:
{chr(10).join(diretores) if diretores else "Nenhum"}
"""

        await update.message.reply_text(resposta)

    except Exception as e:
        await update.message.reply_text(f"Erro na requisição: {str(e)}")


    
