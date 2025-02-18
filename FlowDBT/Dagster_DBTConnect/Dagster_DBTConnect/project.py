from pathlib import Path

from dagster_dbt import DbtProject

FlowDBT_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
# FlowDBT_project.prepare_if_dev()