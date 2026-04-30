def configurar_perfil(nome, idade, cidade="Desconhecida"):
    perfil = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }
    return perfil

perfil1 = configurar_perfil("Iris", 19, "São Paulo")
perfil2 = configurar_perfil("Diogo", 19)          

print(perfil1)
print(perfil2)