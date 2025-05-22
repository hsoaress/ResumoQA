# Resumo da matéria de QA

#### 1. Fundamentos de Garantia da Qualidade (QA)
Conceitos de qualidade em software: Garantir que o produto atenda aos requisitos e expectativas do usuário (ex.: teste de usabilidade em um e-commerce).

#### Tipos de testes:

- Unitário: Testar funções isoladas (ex.: validar cálculo de desconto).

- Integração: Verificar comunicação entre módulos (ex.: API de pagamento integrada ao carrinho).

- Aceitação: Validar se atende aos critérios do cliente (ex.: aprovação do PO em uma User Story).

- Metodologias: QA em Agile (testes contínuos em sprints) e DevOps (testes automatizados no CI/CD).

- Ferramentas: Jira para gestão de bugs, TestRail para organização de casos de teste.

#### 2. Planejamento e Estratégias de Teste
Critérios de aceitação: Usar BDD (Behavior-Driven Development) para definir cenários (ex.: "Dado um usuário logado, quando adiciona um item ao carrinho, então o total deve ser atualizado").

- Casos de teste: Criar cenários baseados em riscos (ex.: priorizar testes no módulo de pagamento).

- Métricas: Taxa de defeitos detectados, cobertura de testes (ex.: 90% do código testado).

- Gestão de mudanças: Versionamento de scripts de teste no Git para acompanhar evolução.

#### 3. Automação de Testes
Ferramentas:

- Selenium/Cypress: Automação de front-end (ex.: testar login em um site).

- Postman/Newman: Testes de API (ex.: validar resposta de um endpoint REST).

- JMeter: Teste de carga (ex.: simular 1000 usuários acessando simultaneamente).

- CI/CD: Integração com GitHub Actions para rodar testes automaticamente a cada commit.

- IA na automação: Gerar casos de teste com ferramentas como Testim.io.

#### 4. Controle e Monitoramento da Qualidade
Auditorias: Análise de conformidade com padrões (ex.: verificar se aplica LGPD).

#### Conclusão
Ao longo do semestre, desenvolvemos habilidades para integrar QA em todas as etapas do ciclo de vida do software, desde o planejamento até a entrega contínua. Aprendemos que testes bem estruturados, automação inteligente e monitoramento proativo são pilares para um software robusto e confiável.

Esses conhecimentos nos permitem não apenas identificar e corrigir problemas, mas também preveni-los, contribuindo para a melhoria contínua e a entrega de valor ao usuário final.

Monitoramento: Usar SonarQube para análise estática de código e Prometheus/Grafana para métricas em tempo real.

Gestão de bugs: Priorização com Matriz de Impacto x Severidade (ex.: bug crítico no checkout).

Observabilidade: Logs, métricas e rastreamento (ex.: usar ELK Stack para investigar erros em produção).
