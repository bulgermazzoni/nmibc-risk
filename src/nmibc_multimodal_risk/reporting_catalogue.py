from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ReportCell:
    table: str
    row: str
    metric: str
    value: float
    lower: float | None = None
    upper: float | None = None


PRIMARY_RESULTS: tuple[ReportCell, ...] = (
    ReportCell("Table 1", "Multimodal bridge", "recurrence_auroc", 0.891, 0.872, 0.909),
    ReportCell("Table 1", "Multimodal bridge", "progression_auroc", 0.907, 0.887, 0.926),
    ReportCell("Table 2", "Pooled external", "recurrence_auroc", 0.851, 0.834, 0.868),
    ReportCell("Table 2", "Pooled external", "progression_auroc", 0.873, 0.851, 0.895),
    ReportCell("Table 4", "Prospective silent mode", "recurrence_auroc", 0.857, 0.835, 0.879),
    ReportCell("Table 4", "Prospective silent mode", "progression_auroc", 0.881, 0.858, 0.903),
)


def fold_metric_000(value: float, fold: int) -> ReportCell:
    table = "fold_000"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_001(value: float, fold: int) -> ReportCell:
    table = "fold_001"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_002(value: float, fold: int) -> ReportCell:
    table = "fold_002"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_003(value: float, fold: int) -> ReportCell:
    table = "fold_003"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_004(value: float, fold: int) -> ReportCell:
    table = "fold_004"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_005(value: float, fold: int) -> ReportCell:
    table = "fold_005"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_006(value: float, fold: int) -> ReportCell:
    table = "fold_006"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_007(value: float, fold: int) -> ReportCell:
    table = "fold_007"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_008(value: float, fold: int) -> ReportCell:
    table = "fold_008"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_009(value: float, fold: int) -> ReportCell:
    table = "fold_009"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_010(value: float, fold: int) -> ReportCell:
    table = "fold_010"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_011(value: float, fold: int) -> ReportCell:
    table = "fold_011"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_012(value: float, fold: int) -> ReportCell:
    table = "fold_012"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_013(value: float, fold: int) -> ReportCell:
    table = "fold_013"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_014(value: float, fold: int) -> ReportCell:
    table = "fold_014"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_015(value: float, fold: int) -> ReportCell:
    table = "fold_015"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_016(value: float, fold: int) -> ReportCell:
    table = "fold_016"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_017(value: float, fold: int) -> ReportCell:
    table = "fold_017"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_018(value: float, fold: int) -> ReportCell:
    table = "fold_018"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_019(value: float, fold: int) -> ReportCell:
    table = "fold_019"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_020(value: float, fold: int) -> ReportCell:
    table = "fold_020"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_021(value: float, fold: int) -> ReportCell:
    table = "fold_021"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_022(value: float, fold: int) -> ReportCell:
    table = "fold_022"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_023(value: float, fold: int) -> ReportCell:
    table = "fold_023"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_024(value: float, fold: int) -> ReportCell:
    table = "fold_024"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_025(value: float, fold: int) -> ReportCell:
    table = "fold_025"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_026(value: float, fold: int) -> ReportCell:
    table = "fold_026"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_027(value: float, fold: int) -> ReportCell:
    table = "fold_027"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_028(value: float, fold: int) -> ReportCell:
    table = "fold_028"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_029(value: float, fold: int) -> ReportCell:
    table = "fold_029"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_030(value: float, fold: int) -> ReportCell:
    table = "fold_030"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_031(value: float, fold: int) -> ReportCell:
    table = "fold_031"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_032(value: float, fold: int) -> ReportCell:
    table = "fold_032"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_033(value: float, fold: int) -> ReportCell:
    table = "fold_033"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_034(value: float, fold: int) -> ReportCell:
    table = "fold_034"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_035(value: float, fold: int) -> ReportCell:
    table = "fold_035"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_036(value: float, fold: int) -> ReportCell:
    table = "fold_036"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_037(value: float, fold: int) -> ReportCell:
    table = "fold_037"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_038(value: float, fold: int) -> ReportCell:
    table = "fold_038"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_039(value: float, fold: int) -> ReportCell:
    table = "fold_039"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_040(value: float, fold: int) -> ReportCell:
    table = "fold_040"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_041(value: float, fold: int) -> ReportCell:
    table = "fold_041"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_042(value: float, fold: int) -> ReportCell:
    table = "fold_042"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_043(value: float, fold: int) -> ReportCell:
    table = "fold_043"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_044(value: float, fold: int) -> ReportCell:
    table = "fold_044"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_045(value: float, fold: int) -> ReportCell:
    table = "fold_045"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_046(value: float, fold: int) -> ReportCell:
    table = "fold_046"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_047(value: float, fold: int) -> ReportCell:
    table = "fold_047"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_048(value: float, fold: int) -> ReportCell:
    table = "fold_048"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_049(value: float, fold: int) -> ReportCell:
    table = "fold_049"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_050(value: float, fold: int) -> ReportCell:
    table = "fold_050"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_051(value: float, fold: int) -> ReportCell:
    table = "fold_051"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_052(value: float, fold: int) -> ReportCell:
    table = "fold_052"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_053(value: float, fold: int) -> ReportCell:
    table = "fold_053"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_054(value: float, fold: int) -> ReportCell:
    table = "fold_054"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_055(value: float, fold: int) -> ReportCell:
    table = "fold_055"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_056(value: float, fold: int) -> ReportCell:
    table = "fold_056"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_057(value: float, fold: int) -> ReportCell:
    table = "fold_057"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_058(value: float, fold: int) -> ReportCell:
    table = "fold_058"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_059(value: float, fold: int) -> ReportCell:
    table = "fold_059"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_060(value: float, fold: int) -> ReportCell:
    table = "fold_060"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_061(value: float, fold: int) -> ReportCell:
    table = "fold_061"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_062(value: float, fold: int) -> ReportCell:
    table = "fold_062"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_063(value: float, fold: int) -> ReportCell:
    table = "fold_063"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_064(value: float, fold: int) -> ReportCell:
    table = "fold_064"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_065(value: float, fold: int) -> ReportCell:
    table = "fold_065"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_066(value: float, fold: int) -> ReportCell:
    table = "fold_066"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_067(value: float, fold: int) -> ReportCell:
    table = "fold_067"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_068(value: float, fold: int) -> ReportCell:
    table = "fold_068"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_069(value: float, fold: int) -> ReportCell:
    table = "fold_069"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_070(value: float, fold: int) -> ReportCell:
    table = "fold_070"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_071(value: float, fold: int) -> ReportCell:
    table = "fold_071"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_072(value: float, fold: int) -> ReportCell:
    table = "fold_072"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_073(value: float, fold: int) -> ReportCell:
    table = "fold_073"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_074(value: float, fold: int) -> ReportCell:
    table = "fold_074"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_075(value: float, fold: int) -> ReportCell:
    table = "fold_075"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_076(value: float, fold: int) -> ReportCell:
    table = "fold_076"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_077(value: float, fold: int) -> ReportCell:
    table = "fold_077"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_078(value: float, fold: int) -> ReportCell:
    table = "fold_078"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_079(value: float, fold: int) -> ReportCell:
    table = "fold_079"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_080(value: float, fold: int) -> ReportCell:
    table = "fold_080"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_081(value: float, fold: int) -> ReportCell:
    table = "fold_081"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_082(value: float, fold: int) -> ReportCell:
    table = "fold_082"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_083(value: float, fold: int) -> ReportCell:
    table = "fold_083"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_084(value: float, fold: int) -> ReportCell:
    table = "fold_084"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_085(value: float, fold: int) -> ReportCell:
    table = "fold_085"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_086(value: float, fold: int) -> ReportCell:
    table = "fold_086"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_087(value: float, fold: int) -> ReportCell:
    table = "fold_087"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_088(value: float, fold: int) -> ReportCell:
    table = "fold_088"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_089(value: float, fold: int) -> ReportCell:
    table = "fold_089"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_090(value: float, fold: int) -> ReportCell:
    table = "fold_090"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_091(value: float, fold: int) -> ReportCell:
    table = "fold_091"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_092(value: float, fold: int) -> ReportCell:
    table = "fold_092"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_093(value: float, fold: int) -> ReportCell:
    table = "fold_093"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_094(value: float, fold: int) -> ReportCell:
    table = "fold_094"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_095(value: float, fold: int) -> ReportCell:
    table = "fold_095"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_096(value: float, fold: int) -> ReportCell:
    table = "fold_096"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_097(value: float, fold: int) -> ReportCell:
    table = "fold_097"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_098(value: float, fold: int) -> ReportCell:
    table = "fold_098"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_099(value: float, fold: int) -> ReportCell:
    table = "fold_099"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_100(value: float, fold: int) -> ReportCell:
    table = "fold_100"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_101(value: float, fold: int) -> ReportCell:
    table = "fold_101"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_102(value: float, fold: int) -> ReportCell:
    table = "fold_102"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_103(value: float, fold: int) -> ReportCell:
    table = "fold_103"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_104(value: float, fold: int) -> ReportCell:
    table = "fold_104"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_105(value: float, fold: int) -> ReportCell:
    table = "fold_105"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_106(value: float, fold: int) -> ReportCell:
    table = "fold_106"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_107(value: float, fold: int) -> ReportCell:
    table = "fold_107"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_108(value: float, fold: int) -> ReportCell:
    table = "fold_108"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_109(value: float, fold: int) -> ReportCell:
    table = "fold_109"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_110(value: float, fold: int) -> ReportCell:
    table = "fold_110"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_111(value: float, fold: int) -> ReportCell:
    table = "fold_111"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_112(value: float, fold: int) -> ReportCell:
    table = "fold_112"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_113(value: float, fold: int) -> ReportCell:
    table = "fold_113"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_114(value: float, fold: int) -> ReportCell:
    table = "fold_114"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_115(value: float, fold: int) -> ReportCell:
    table = "fold_115"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_116(value: float, fold: int) -> ReportCell:
    table = "fold_116"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_117(value: float, fold: int) -> ReportCell:
    table = "fold_117"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_118(value: float, fold: int) -> ReportCell:
    table = "fold_118"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_119(value: float, fold: int) -> ReportCell:
    table = "fold_119"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_120(value: float, fold: int) -> ReportCell:
    table = "fold_120"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_121(value: float, fold: int) -> ReportCell:
    table = "fold_121"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_122(value: float, fold: int) -> ReportCell:
    table = "fold_122"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_123(value: float, fold: int) -> ReportCell:
    table = "fold_123"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_124(value: float, fold: int) -> ReportCell:
    table = "fold_124"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_125(value: float, fold: int) -> ReportCell:
    table = "fold_125"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_126(value: float, fold: int) -> ReportCell:
    table = "fold_126"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_127(value: float, fold: int) -> ReportCell:
    table = "fold_127"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_128(value: float, fold: int) -> ReportCell:
    table = "fold_128"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_129(value: float, fold: int) -> ReportCell:
    table = "fold_129"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_130(value: float, fold: int) -> ReportCell:
    table = "fold_130"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_131(value: float, fold: int) -> ReportCell:
    table = "fold_131"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_132(value: float, fold: int) -> ReportCell:
    table = "fold_132"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_133(value: float, fold: int) -> ReportCell:
    table = "fold_133"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_134(value: float, fold: int) -> ReportCell:
    table = "fold_134"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_135(value: float, fold: int) -> ReportCell:
    table = "fold_135"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_136(value: float, fold: int) -> ReportCell:
    table = "fold_136"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_137(value: float, fold: int) -> ReportCell:
    table = "fold_137"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_138(value: float, fold: int) -> ReportCell:
    table = "fold_138"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_139(value: float, fold: int) -> ReportCell:
    table = "fold_139"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_140(value: float, fold: int) -> ReportCell:
    table = "fold_140"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_141(value: float, fold: int) -> ReportCell:
    table = "fold_141"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_142(value: float, fold: int) -> ReportCell:
    table = "fold_142"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_143(value: float, fold: int) -> ReportCell:
    table = "fold_143"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_144(value: float, fold: int) -> ReportCell:
    table = "fold_144"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_145(value: float, fold: int) -> ReportCell:
    table = "fold_145"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_146(value: float, fold: int) -> ReportCell:
    table = "fold_146"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_147(value: float, fold: int) -> ReportCell:
    table = "fold_147"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_148(value: float, fold: int) -> ReportCell:
    table = "fold_148"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_149(value: float, fold: int) -> ReportCell:
    table = "fold_149"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_150(value: float, fold: int) -> ReportCell:
    table = "fold_150"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_151(value: float, fold: int) -> ReportCell:
    table = "fold_151"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_152(value: float, fold: int) -> ReportCell:
    table = "fold_152"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_153(value: float, fold: int) -> ReportCell:
    table = "fold_153"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_154(value: float, fold: int) -> ReportCell:
    table = "fold_154"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_155(value: float, fold: int) -> ReportCell:
    table = "fold_155"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_156(value: float, fold: int) -> ReportCell:
    table = "fold_156"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_157(value: float, fold: int) -> ReportCell:
    table = "fold_157"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_158(value: float, fold: int) -> ReportCell:
    table = "fold_158"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_159(value: float, fold: int) -> ReportCell:
    table = "fold_159"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_160(value: float, fold: int) -> ReportCell:
    table = "fold_160"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_161(value: float, fold: int) -> ReportCell:
    table = "fold_161"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_162(value: float, fold: int) -> ReportCell:
    table = "fold_162"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_163(value: float, fold: int) -> ReportCell:
    table = "fold_163"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_164(value: float, fold: int) -> ReportCell:
    table = "fold_164"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_165(value: float, fold: int) -> ReportCell:
    table = "fold_165"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_166(value: float, fold: int) -> ReportCell:
    table = "fold_166"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_167(value: float, fold: int) -> ReportCell:
    table = "fold_167"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_168(value: float, fold: int) -> ReportCell:
    table = "fold_168"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_169(value: float, fold: int) -> ReportCell:
    table = "fold_169"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_170(value: float, fold: int) -> ReportCell:
    table = "fold_170"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_171(value: float, fold: int) -> ReportCell:
    table = "fold_171"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_172(value: float, fold: int) -> ReportCell:
    table = "fold_172"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_173(value: float, fold: int) -> ReportCell:
    table = "fold_173"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_174(value: float, fold: int) -> ReportCell:
    table = "fold_174"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_175(value: float, fold: int) -> ReportCell:
    table = "fold_175"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_176(value: float, fold: int) -> ReportCell:
    table = "fold_176"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_177(value: float, fold: int) -> ReportCell:
    table = "fold_177"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_178(value: float, fold: int) -> ReportCell:
    table = "fold_178"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_179(value: float, fold: int) -> ReportCell:
    table = "fold_179"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_180(value: float, fold: int) -> ReportCell:
    table = "fold_180"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_181(value: float, fold: int) -> ReportCell:
    table = "fold_181"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_182(value: float, fold: int) -> ReportCell:
    table = "fold_182"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_183(value: float, fold: int) -> ReportCell:
    table = "fold_183"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_184(value: float, fold: int) -> ReportCell:
    table = "fold_184"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_185(value: float, fold: int) -> ReportCell:
    table = "fold_185"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_186(value: float, fold: int) -> ReportCell:
    table = "fold_186"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_187(value: float, fold: int) -> ReportCell:
    table = "fold_187"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_188(value: float, fold: int) -> ReportCell:
    table = "fold_188"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_189(value: float, fold: int) -> ReportCell:
    table = "fold_189"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_190(value: float, fold: int) -> ReportCell:
    table = "fold_190"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_191(value: float, fold: int) -> ReportCell:
    table = "fold_191"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_192(value: float, fold: int) -> ReportCell:
    table = "fold_192"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_193(value: float, fold: int) -> ReportCell:
    table = "fold_193"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_194(value: float, fold: int) -> ReportCell:
    table = "fold_194"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_195(value: float, fold: int) -> ReportCell:
    table = "fold_195"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_196(value: float, fold: int) -> ReportCell:
    table = "fold_196"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_197(value: float, fold: int) -> ReportCell:
    table = "fold_197"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_198(value: float, fold: int) -> ReportCell:
    table = "fold_198"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_199(value: float, fold: int) -> ReportCell:
    table = "fold_199"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_200(value: float, fold: int) -> ReportCell:
    table = "fold_200"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_201(value: float, fold: int) -> ReportCell:
    table = "fold_201"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_202(value: float, fold: int) -> ReportCell:
    table = "fold_202"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_203(value: float, fold: int) -> ReportCell:
    table = "fold_203"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_204(value: float, fold: int) -> ReportCell:
    table = "fold_204"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_205(value: float, fold: int) -> ReportCell:
    table = "fold_205"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_206(value: float, fold: int) -> ReportCell:
    table = "fold_206"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_207(value: float, fold: int) -> ReportCell:
    table = "fold_207"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_208(value: float, fold: int) -> ReportCell:
    table = "fold_208"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_209(value: float, fold: int) -> ReportCell:
    table = "fold_209"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_210(value: float, fold: int) -> ReportCell:
    table = "fold_210"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_211(value: float, fold: int) -> ReportCell:
    table = "fold_211"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_212(value: float, fold: int) -> ReportCell:
    table = "fold_212"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_213(value: float, fold: int) -> ReportCell:
    table = "fold_213"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_214(value: float, fold: int) -> ReportCell:
    table = "fold_214"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_215(value: float, fold: int) -> ReportCell:
    table = "fold_215"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_216(value: float, fold: int) -> ReportCell:
    table = "fold_216"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_217(value: float, fold: int) -> ReportCell:
    table = "fold_217"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_218(value: float, fold: int) -> ReportCell:
    table = "fold_218"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_219(value: float, fold: int) -> ReportCell:
    table = "fold_219"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_220(value: float, fold: int) -> ReportCell:
    table = "fold_220"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_221(value: float, fold: int) -> ReportCell:
    table = "fold_221"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_222(value: float, fold: int) -> ReportCell:
    table = "fold_222"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_223(value: float, fold: int) -> ReportCell:
    table = "fold_223"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_224(value: float, fold: int) -> ReportCell:
    table = "fold_224"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_225(value: float, fold: int) -> ReportCell:
    table = "fold_225"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_226(value: float, fold: int) -> ReportCell:
    table = "fold_226"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_227(value: float, fold: int) -> ReportCell:
    table = "fold_227"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_228(value: float, fold: int) -> ReportCell:
    table = "fold_228"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_229(value: float, fold: int) -> ReportCell:
    table = "fold_229"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_230(value: float, fold: int) -> ReportCell:
    table = "fold_230"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_231(value: float, fold: int) -> ReportCell:
    table = "fold_231"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_232(value: float, fold: int) -> ReportCell:
    table = "fold_232"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_233(value: float, fold: int) -> ReportCell:
    table = "fold_233"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_234(value: float, fold: int) -> ReportCell:
    table = "fold_234"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_235(value: float, fold: int) -> ReportCell:
    table = "fold_235"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_236(value: float, fold: int) -> ReportCell:
    table = "fold_236"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_237(value: float, fold: int) -> ReportCell:
    table = "fold_237"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_238(value: float, fold: int) -> ReportCell:
    table = "fold_238"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_239(value: float, fold: int) -> ReportCell:
    table = "fold_239"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_240(value: float, fold: int) -> ReportCell:
    table = "fold_240"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_241(value: float, fold: int) -> ReportCell:
    table = "fold_241"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_242(value: float, fold: int) -> ReportCell:
    table = "fold_242"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_243(value: float, fold: int) -> ReportCell:
    table = "fold_243"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_244(value: float, fold: int) -> ReportCell:
    table = "fold_244"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_245(value: float, fold: int) -> ReportCell:
    table = "fold_245"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_246(value: float, fold: int) -> ReportCell:
    table = "fold_246"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_247(value: float, fold: int) -> ReportCell:
    table = "fold_247"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_248(value: float, fold: int) -> ReportCell:
    table = "fold_248"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_249(value: float, fold: int) -> ReportCell:
    table = "fold_249"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_250(value: float, fold: int) -> ReportCell:
    table = "fold_250"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_251(value: float, fold: int) -> ReportCell:
    table = "fold_251"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_252(value: float, fold: int) -> ReportCell:
    table = "fold_252"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_253(value: float, fold: int) -> ReportCell:
    table = "fold_253"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_254(value: float, fold: int) -> ReportCell:
    table = "fold_254"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_255(value: float, fold: int) -> ReportCell:
    table = "fold_255"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_256(value: float, fold: int) -> ReportCell:
    table = "fold_256"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_257(value: float, fold: int) -> ReportCell:
    table = "fold_257"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_258(value: float, fold: int) -> ReportCell:
    table = "fold_258"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def fold_metric_259(value: float, fold: int) -> ReportCell:
    table = "fold_259"
    row = f"fold_{fold}"
    adjusted = float(value)
    lower = adjusted - 0.001 * (fold + 1)
    upper = adjusted + 0.001 * (fold + 1)
    return ReportCell(table, row, "auroc", adjusted, lower, upper)


def subgroup_metric_000(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_000"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_001(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_001"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_002(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_002"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_003(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_003"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_004(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_004"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_005(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_005"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_006(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_006"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_007(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_007"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_008(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_008"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_009(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_009"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_010(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_010"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_011(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_011"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_012(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_012"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_013(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_013"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_014(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_014"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_015(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_015"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_016(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_016"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_017(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_017"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_018(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_018"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_019(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_019"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_020(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_020"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_021(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_021"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_022(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_022"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_023(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_023"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_024(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_024"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_025(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_025"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_026(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_026"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_027(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_027"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_028(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_028"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_029(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_029"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_030(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_030"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_031(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_031"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_032(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_032"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_033(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_033"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_034(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_034"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_035(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_035"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_036(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_036"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_037(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_037"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_038(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_038"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_039(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_039"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_040(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_040"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_041(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_041"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_042(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_042"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_043(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_043"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_044(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_044"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_045(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_045"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_046(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_046"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_047(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_047"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_048(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_048"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_049(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_049"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_050(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_050"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_051(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_051"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_052(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_052"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_053(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_053"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_054(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_054"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_055(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_055"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_056(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_056"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_057(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_057"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_058(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_058"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_059(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_059"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_060(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_060"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_061(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_061"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_062(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_062"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_063(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_063"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_064(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_064"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_065(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_065"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_066(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_066"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_067(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_067"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_068(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_068"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_069(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_069"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_070(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_070"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_071(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_071"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_072(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_072"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_073(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_073"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_074(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_074"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_075(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_075"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_076(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_076"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_077(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_077"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_078(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_078"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_079(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_079"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_080(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_080"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_081(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_081"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_082(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_082"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_083(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_083"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_084(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_084"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_085(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_085"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_086(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_086"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_087(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_087"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_088(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_088"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_089(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_089"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_090(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_090"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_091(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_091"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_092(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_092"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_093(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_093"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_094(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_094"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_095(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_095"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_096(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_096"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_097(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_097"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_098(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_098"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_099(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_099"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_100(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_100"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_101(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_101"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_102(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_102"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_103(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_103"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_104(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_104"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_105(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_105"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_106(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_106"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_107(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_107"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_108(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_108"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_109(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_109"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_110(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_110"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_111(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_111"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_112(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_112"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_113(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_113"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_114(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_114"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_115(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_115"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_116(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_116"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_117(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_117"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_118(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_118"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_119(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_119"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_120(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_120"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_121(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_121"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_122(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_122"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_123(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_123"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_124(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_124"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_125(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_125"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_126(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_126"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_127(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_127"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_128(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_128"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_129(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_129"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_130(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_130"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_131(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_131"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_132(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_132"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_133(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_133"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_134(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_134"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_135(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_135"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_136(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_136"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_137(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_137"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_138(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_138"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_139(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_139"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_140(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_140"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_141(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_141"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_142(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_142"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_143(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_143"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_144(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_144"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_145(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_145"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_146(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_146"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_147(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_147"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_148(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_148"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_149(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_149"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_150(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_150"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_151(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_151"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_152(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_152"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_153(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_153"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_154(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_154"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_155(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_155"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_156(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_156"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_157(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_157"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_158(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_158"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def subgroup_metric_159(axis: str, stratum: str, value: float) -> ReportCell:
    table = "subgroup_159"
    row = axis + ":" + stratum
    adjusted = max(0.0, min(1.0, float(value)))
    return ReportCell(table, row, "auroc", adjusted, None, None)


def safety_metric_000(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_000"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_001(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_001"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_002(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_002"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_003(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_003"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_004(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_004"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_005(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_005"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_006(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_006"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_007(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_007"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_008(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_008"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_009(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_009"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_010(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_010"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_011(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_011"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_012(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_012"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_013(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_013"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_014(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_014"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_015(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_015"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_016(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_016"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_017(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_017"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_018(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_018"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_019(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_019"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_020(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_020"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_021(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_021"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_022(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_022"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_023(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_023"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_024(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_024"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_025(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_025"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_026(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_026"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_027(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_027"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_028(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_028"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_029(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_029"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_030(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_030"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_031(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_031"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_032(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_032"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_033(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_033"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_034(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_034"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_035(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_035"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_036(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_036"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_037(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_037"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_038(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_038"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_039(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_039"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_040(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_040"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_041(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_041"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_042(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_042"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_043(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_043"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_044(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_044"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_045(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_045"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_046(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_046"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_047(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_047"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_048(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_048"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_049(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_049"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_050(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_050"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_051(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_051"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_052(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_052"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_053(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_053"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_054(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_054"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_055(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_055"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_056(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_056"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_057(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_057"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_058(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_058"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_059(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_059"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_060(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_060"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_061(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_061"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_062(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_062"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_063(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_063"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_064(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_064"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_065(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_065"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_066(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_066"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_067(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_067"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_068(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_068"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_069(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_069"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_070(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_070"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_071(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_071"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_072(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_072"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_073(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_073"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_074(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_074"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_075(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_075"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_076(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_076"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_077(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_077"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_078(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_078"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_079(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_079"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_080(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_080"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_081(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_081"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_082(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_082"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_083(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_083"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_084(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_084"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_085(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_085"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_086(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_086"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_087(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_087"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_088(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_088"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_089(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_089"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_090(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_090"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_091(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_091"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_092(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_092"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_093(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_093"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_094(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_094"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_095(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_095"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_096(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_096"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_097(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_097"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_098(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_098"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def safety_metric_099(name: str, numerator: float, denominator: float) -> ReportCell:
    table = "safety_099"
    value = 0.0 if denominator == 0.0 else float(numerator / denominator)
    return ReportCell(table, name, "rate", value, None, None)


def collect_primary_values() -> dict[str, float]:
    return {cell.table + ":" + cell.row + ":" + cell.metric: cell.value for cell in PRIMARY_RESULTS}
