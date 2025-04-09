def verificarCadastro(participante):
    idade_anos = participante.get("idade")
    categoria = participante.get("categoria")
    tempo = participante.get("tempoEstimado")
    termo = participante.get("assinaturaTermo")

    if (10 <= idade_anos <= 60):
        if categoria == "infantil" and not (10 <= idade_anos <= 14):
            return False
        elif categoria == "juvenil" and not (15 <= idade_anos <= 17):
            return False
        elif categoria == "adulto" and not (18 <= idade_anos <= 60):
            return False
        elif categoria not in ["infantil", "juvenil", "adulto"]:
            return False
    else:
        return False

    if not (30 <= tempo <= 180):
        return False

    if not termo:
        return False

    return True

