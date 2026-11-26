# Jonathan Bezerra · Portfólio e Radar de Repositórios

Site estático (HTML, CSS e JavaScript puros, sem dependências nem fontes externas) com:
- apresentação, trajetória (linha do tempo) e projetos;
- catálogo crítico de repositórios públicos do GitHub para contabilidade, fiscal, tributário, auditoria e automação.

## Arquivos
- `index.html`: o site inteiro.
- `data/perfil.json`: dados pessoais, credenciais, trajetória e projetos. Para incluir um logo, salve o arquivo em `assets/logos/` e preencha o campo `logo` do item (ex.: `"logo": "assets/logos/kpmg.svg"`). Para publicar o link de um projeto, preencha `link`.
- `data/repos.json`: catálogo de repositórios. Itens com `status: "pendente"` não aparecem no site; a aprovação é humana.
- `refresh_stats.py`: atualiza estrelas, data do último commit, licença e marca arquivados.

## Publicar
Settings > Pages > Deploy from a branch > `main` / root.

## Testar localmente
`python3 -m http.server` na pasta e abrir http://localhost:8000.

## Atualização quinzenal
Um agente agendado (dias 1 e 15) atualiza as estatísticas e abre um pull request com candidatos novos como `pendente`. Nada entra no ar sem aprovação.
