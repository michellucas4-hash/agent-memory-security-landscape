# Segurança para agentes e cadeia de suprimentos

## Ferramentas complementares
- **Bandit**: análise estática Python, complementa revisão humana.
- **Gitleaks / TruffleHog**: detecção de segredos; diferentes motores e padrões.
- **OSV Scanner / pip-audit / Trivy**: vulnerabilidades de dependências e artefatos.
- **NVIDIA SkillSpector**: inspeção de riscos associados a skills/agentes, incluindo prompt injection e exfiltração.
- **Syft / CycloneDX CLI**: inventário e validação de SBOM.
- **Cosign / in-toto**: assinatura, proveniência e atestações.
- **GUAC**: correlaciona componentes, cadeias e dados de segurança num grafo.
- **SOPS**: arquivos cifrados; não publicar valores de segredos.
- **OpenSSF Scorecard**: boas práticas de segurança de repositórios (escala 0 a 10); **Criticality Score**: criticidade para ecossistema (escala 0 a 1).

## Pipeline sugerido, sem instalar ferramentas automaticamente
```text
PR / commit
   │
   ├─ Revisão de licença e proveniência
   ├─ Testes unitários + SAST Python (Bandit)
   ├─ Secret scanning (Gitleaks)
   ├─ Dependency scan (OSV / pip-audit)
   ├─ Skill security scan (quando aplicável)
   ├─ Geração de SBOM (Syft / CycloneDX)
   ├─ Proveniência / assinatura de build (in-toto / Cosign)
   └─ Aprovação humana e publicação explícita
```

### Barreiras obrigatórias para pesquisa
Não executar scripts de instalação de fontes não verificadas; manter redes e credenciais isoladas; evitar envio de código ou prompts a modelos hospedados; restringir o que sai nos relatórios; usar releases/tags/commits fixados; documentar rollback e exceções.
