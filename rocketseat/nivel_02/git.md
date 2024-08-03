# Inicia o git (repositorio) no seu projeto

git init

# Verifica se há alterações de pastas e arquivos no projeto

 git status

# adiciona todos arquivos e pastas mofdigficados, ao stage area

 git add

# Cria e descreve um ponto na história

 git commit -m "message here"

# historico de de commits do projeto

 git log

# Comando para restaurar arquivos do git a um dado momento da história

 git restore

# Comando para acessar algum ponto da história (commit)

 git checkout + (Parte do id coletado com git log)

# Create a new repository on the command line

```
echo "# stgare" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/cristianoAmaral/stgare.git
git push -u origin main
```

# Push an existing repository from the command line

```
git remote add origin https://github.com/cristianoAmaral/stgare.git
git branch -M main
git push -u origin main
```
