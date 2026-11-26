# Radar de Repositórios

Projeto pessoal de Jonathan Bezerra.

Catálogo curado de repositórios públicos do GitHub para contabilidade, fiscal, tributário, auditoria e automação.

- `index.html`: portal estático (visão geral, filtros por categoria, busca, selos de manutenção, licença e parecer).
- `data/repos.json`: única fonte de dados. Para adicionar um repo, inclua um item com `repo`, `category`, `what`, `how`, `value`, `note`.
- `refresh_stats.py`: atualiza estrelas, último commit e licença (`python3 refresh_stats.py`, exige `gh` autenticado).

## Publicar
Settings > Pages > Deploy from branch > `main` / root.

## Teste local
`python3 -m http.server` e abra http://localhost:8000

## Curadoria
Todo repo novo entra por revisão humana: verificar licença, último commit e se há nota técnica fiscal recente.
