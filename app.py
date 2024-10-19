from bottle import route, run, request, template
from analysis import perform_analysis

# Rota para exibir o formulário HTML
@route('/')
def index():
    return template('index')

# Rota para processar o código
@route('/analyze', method='POST')
def analyze_code():
    code = request.forms.get('code')
    if not code:
        return "Por favor, envie o código para análise."

    analysis_result = perform_analysis(code)
    return analysis_result

if __name__ == "__main__":
    run(host='localhost', port=8080)
