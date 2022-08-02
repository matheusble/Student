# Student
## CRUD para cadastro de alunos com curso.

Configure o database no arquivo settings com seu usuário, senha, porta, host e nome do banco de dados.(MySQL)
```
python3 manage.py makemigrations todotask  --- Faz a migração do model.
python3 manage.py migrate todotask  --- Faz a migração para o banco de dados.
python3 manage.py runserver --- Inicia o servidor.
```

###### Utilização: Fazer o cadatro da categoria que pertence o curso, cadastrar o curso e atribuir uma categoria, cadastrar aluno e atribuir um curso.

## Endpoints.
```
/students/ --- Lista e cadastra os alunos.
/students/<int:pk>/ --- Busca aluno pelo id.
/course/ Lista e cadastra os cursos.
/courses/<int:pk>/ --- Busca curso pelo id.
/categories/ --- Lista e cadastra as categorias.
/categories/<int:pk>/ --- Busca categoria pelo id.
```
