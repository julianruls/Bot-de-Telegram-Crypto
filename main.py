# Importamos las bibliotecas necesarias
import telebot
import yfinance as yf

# Seteamos al bot
TOKEN = "kjsadsldiasdioashdhio" # Agregar el token generado
bot = telebot.TeleBot(TOKEN)

#---------- BTC -----------

# Manejar el comando /btc
@bot.message_handler(commands=['btc'])
def precio_btc(mensaje):
    try:
        # Obtener datos de BTC-USD
        btc_info = yf.Ticker("BTC-USD")
        # history(period="1d") obtiene los datos del día actual, y ['Close'].iloc[-1] devuelve el último precio de cierre.
        btc_precio = btc_info.history(period="1d")['Close'].iloc[-1] 
        # Respuesta del bot
        respuesta = f"Hola! La cotización actual de BITCOIN es: ${btc_precio:.2f} USD."
    except Exception as e:
        respuesta = f"Hubo un error al obtener la cotización: {e}"
    bot.reply_to(mensaje, respuesta)
    
#---------- ETH -----------    
    
# Manejar el comando /eth
@bot.message_handler(commands=['eth'])
def precio_eth(mensaje):
    try:
        # Obtener datos de ETH-USD
        eth_info = yf.Ticker("ETH-USD")
        # history(period="1d") obtiene los datos del día actual, y ['Close'].iloc[-1] devuelve el último precio de cierre.
        eth_precio = eth_info.history(period="1d")['Close'].iloc[-1] 
        # Respuesta del bot
        respuesta = f"Hola! La cotización actual de ETHEREUM es: ${eth_precio:.2f} USD."
    except Exception as e:
        respuesta = f"Hubo un error al obtener la cotización: {e}"
    bot.reply_to(mensaje, respuesta)
    
#---------- SOL -----------

# Manejar el comando /sol
@bot.message_handler(commands=['sol'])
def precio_sol(mensaje):
    try:
        # Obtener datos de SOL-USD
        sol_info = yf.Ticker("SOL-USD")
        # history(period="1d") obtiene los datos del día actual, y ['Close'].iloc[-1] devuelve el último precio de cierre.
        sol_precio = sol_info.history(period="1d")['Close'].iloc[-1] 
        # Respuesta del bot
        respuesta = f"Hola! La cotización actual de SOLANA es: ${sol_precio:.2f} USD."
    except Exception as e:
        respuesta = f"Hubo un error al obtener la cotización: {e}"
    bot.reply_to(mensaje, respuesta)
    
#---------- BNB -----------

# Manejar el comando /bnb
@bot.message_handler(commands=['bnb'])
def precio_bnb(mensaje):
    try:
        # Obtener datos de BNB-USD
        bnb_info = yf.Ticker("BNB-USD")
        # history(period="1d") obtiene los datos del día actual, y ['Close'].iloc[-1] devuelve el último precio de cierre.
        bnb_precio = bnb_info.history(period="1d")['Close'].iloc[-1] 
        # Respuesta del bot
        respuesta = f"Hola! La cotización actual de BNB es: ${bnb_precio:.2f} USD."
    except Exception as e:
        respuesta = f"Hubo un error al obtener la cotización: {e}"
    bot.reply_to(mensaje, respuesta)

#---------- XRP -----------

# Manejar el comando /xrp
@bot.message_handler(commands=['xrp'])
def precio_xrp(mensaje):
    try:
        # Obtener datos de XRP-USD
        xrp_info = yf.Ticker("XRP-USD")
        # history(period="1d") obtiene los datos del día actual, y ['Close'].iloc[-1] devuelve el último precio de cierre.
        xrp_precio = xrp_info.history(period="1d")['Close'].iloc[-1] 
        # Respuesta del bot
        respuesta = f"Hola! La cotización actual de XRP es: ${xrp_precio:.2f} USD."
    except Exception as e:
        respuesta = f"Hubo un error al obtener la cotización: {e}"
    bot.reply_to(mensaje, respuesta)
    
#---------- DOGE -----------

# Manejar el comando /doge
@bot.message_handler(commands=['doge'])
def precio_doge(mensaje):
    try:
        # Obtener datos de DOGE-USD
        doge_info = yf.Ticker("DOGE-USD")
        # history(period="1d") obtiene los datos del día actual, y ['Close'].iloc[-1] devuelve el último precio de cierre.
        doge_precio = doge_info.history(period="1d")['Close'].iloc[-1] 
        # Respuesta del bot
        respuesta = f"Hola! La cotización actual de DOGE es: ${doge_precio:.2f} USD."
    except Exception as e:
        respuesta = f"Hubo un error al obtener la cotización: {e}"
    bot.reply_to(mensaje, respuesta)
    
#---------- ADA -----------

# Manejar el comando /ada
@bot.message_handler(commands=['ada'])
def precio_ada(mensaje):
    try:
        # Obtener datos de ADA-USD
        ada_info = yf.Ticker("ADA-USD")
        # history(period="1d") obtiene los datos del día actual, y ['Close'].iloc[-1] devuelve el último precio de cierre.
        ada_precio = ada_info.history(period="1d")['Close'].iloc[-1] 
        # Respuesta del bot
        respuesta = f"Hola! La cotización actual de CARADANO es: ${ada_precio:.2f} USD."
    except Exception as e:
        respuesta = f"Hubo un error al obtener la cotización: {e}"
    bot.reply_to(mensaje, respuesta)

#---------- AVAX -----------

# Manejar el comando /avax
@bot.message_handler(commands=['avax'])
def precio_avax(mensaje):
    try:
        # Obtener datos de AVAX-USD
        avax_info = yf.Ticker("AVAX-USD")
        # history(period="1d") obtiene los datos del día actual, y ['Close'].iloc[-1] devuelve el último precio de cierre.
        avax_precio = avax_info.history(period="1d")['Close'].iloc[-1] 
        # Respuesta del bot
        respuesta = f"Hola! La cotización actual de AVALANCHE es: ${avax_precio:.2f} USD."
    except Exception as e:
        respuesta = f"Hubo un error al obtener la cotización: {e}"
    bot.reply_to(mensaje, respuesta)    

#---------- TRX -----------

# Manejar el comando /trx
@bot.message_handler(commands=['trx'])
def precio_trx(mensaje):
    try:
        # Obtener datos de TRX-USD
        trx_info = yf.Ticker("TRX-USD")
        # history(period="1d") obtiene los datos del día actual, y ['Close'].iloc[-1] devuelve el último precio de cierre.
        trx_precio = trx_info.history(period="1d")['Close'].iloc[-1] 
        # Respuesta del bot
        respuesta = f"Hola! La cotización actual de TRON es: ${trx_precio:.2f} USD."
    except Exception as e:
        respuesta = f"Hubo un error al obtener la cotización: {e}"
    bot.reply_to(mensaje, respuesta)
    
#---------- TON -----------

# Manejar el comando /ton
@bot.message_handler(commands=['ton'])
def precio_ton(mensaje):
    try:
        # Obtener datos de TON-USD
        ton_info = yf.Ticker("TON11419-USD")
        # history(period="1d") obtiene los datos del día actual, y ['Close'].iloc[-1] devuelve el último precio de cierre.
        ton_precio = ton_info.history(period="1d")['Close'].iloc[-1] 
        # Respuesta del bot
        respuesta = f"Hola! La cotización actual de TONCOIN es: ${ton_precio:.2f} USD."
    except Exception as e:
        respuesta = f"Hubo un error al obtener la cotización: {e}"
    bot.reply_to(mensaje, respuesta)
    
# Iniciar el bot
print("El bot está funcionando...")
bot.polling(none_stop=True)
