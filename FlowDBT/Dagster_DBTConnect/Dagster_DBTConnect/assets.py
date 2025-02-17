from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import FlowDBT_project


@dbt_assets(manifest=FlowDBT_project.manifest_path)
def FlowDBT_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    