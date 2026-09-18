def test_project_smoke():
    from core.detector import detect_attack
    from core.defense import apply_defense
    from core.permissions import check_tool_permission
    from core.leakage_guard import detect_sensitive_data

    assert callable(detect_attack)
    assert callable(apply_defense)
    assert callable(check_tool_permission)
    assert callable(detect_sensitive_data)