# Evidence Matrix

| Requirement | Implementation | Evidence |
|---|---|---|
| Threat Model | Threat model document | docs/threat_model.md |
| Attack Corpus | Synthetic CSV corpus | data/attacks.csv |
| Direct Injection | Detector | core/detector.py |
| Indirect Injection | Document scanner | core/detector.py |
| Tool Abuse | Permission sandbox | core/permissions.py |
| Output Leakage | Leakage guard | core/leakage_guard.py |
| Audit Trail | SQLite logging | core/logger.py |
| Evaluation | Evaluation dashboard | core/evaluator.py |
| Baseline | Baseline simulator | core/baseline.py |
| Innovation | Mutation engine | core/mutation.py |
| Residual Risk | Mutation analysis | docs/residual_risk.md |
| Automated Testing | Pytest | tests/ |
| Dependency Security | pip-audit | requirements.txt |
| CI | GitHub Actions | .github/workflows/ci.yml |
| Reproducibility | Docker | Dockerfile |
| Health Validation | Health check | health_check.py |
| Research Evaluation | Final report | docs/final_evaluation_report.md |
| System Card | System documentation | docs/system_card.md |
| Error Analysis | Failure analysis | docs/error_analysis.md |