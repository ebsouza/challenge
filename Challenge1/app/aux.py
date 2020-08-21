import re

def validate_request_json(file_json, fields):

    #Teste json vazio
    if file_json == {}:
        return False   
    
    #Existencia dos campos listados em fields
    n_fields = 0
    for key in file_json.keys():
        if (key in fields):
            n_fields += 1

    if n_fields != len(fields):
        return False

    #Existencia de outros campos alem dos listados em fields
    for key in file_json.keys():
        if not (key in fields):
            return False

    #Existencia dos valores
    for value in file_json.values():
        if value == None:
            return False

    return True

def cnpj_checker(cnpj):

    CNPJ_Pattern = r"^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$"

    return bool(re.match(CNPJ_Pattern, cnpj))

def cpf_checker(cpf):

    CPF_Pattern = r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"

    return bool(re.match(CPF_Pattern, cpf))
