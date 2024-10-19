def perform_analysis(code):
    # Verificação simples de segurança
    issues = []
    
    if 'eval' in code:
        issues.append("Uso de 'eval' detectado. Evite usar 'eval' para melhorar a segurança.")
    
    # Pode adicionar mais regras
    if not issues:
        return "Análise concluída! Nenhum problema encontrado."
    return "Problemas encontrados:\n" + "\n".join(issues)
