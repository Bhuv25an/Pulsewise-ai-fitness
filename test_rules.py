import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))
from coach_rules import has_red_flag, safe_calorie_target, escalate_or_answer, vrat_day_ok


def test_red_flag_detected():
    assert has_red_flag("I have chest pain when I run")


def test_normal_message_not_flagged():
    assert not has_red_flag("What should I eat after a walk?")


def test_calorie_floor():
    assert safe_calorie_target(800) == 1200
    assert safe_calorie_target(1800) == 1800


def test_escalation():
    assert escalate_or_answer("I feel dizzy").startswith("ESCALATE")


def test_vrat_mode():
    assert vrat_day_ok(["sabudana", "fruit"])
    assert not vrat_day_ok(["rice"])
