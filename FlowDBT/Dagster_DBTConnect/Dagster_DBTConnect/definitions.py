from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import FlowDBT_dbt_assets
from .project import FlowDBT_project
from .schedules import schedules

defs = Definitions(
    assets=[FlowDBT_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=FlowDBT_project),
    },
)