# monitoramento.py
import logging
from prometheus_client import start_http_server, Counter

# Configuração de Logs
logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Métricas Prometheus
REQUEST_COUNT = Counter('http_requests_total', 'Total de requisições HTTP')

def processar_requisicao():
    try:
        REQUEST_COUNT.inc()
        # Lógica da aplicação
    except Exception as e:
        logging.error(f"Erro ao processar requisição: {str(e)}")

if __name__ == '__main__':
    start_http_server(8000)  # Expondo métricas na porta 8000
