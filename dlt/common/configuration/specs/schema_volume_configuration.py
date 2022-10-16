from typing import Optional, Literal

from dlt.common.configuration.specs.base_configuration import BaseConfiguration, configspec

TSchemaFileFormat = Literal["json", "yaml"]


@configspec(init=True)
class SchemaVolumeConfiguration(BaseConfiguration):
    schema_volume_path: str = None  # path to volume with default schemas
    import_schema_path: Optional[str] = None  # import schema from external location
    export_schema_path: Optional[str] = None  # export schema to external location
    external_schema_format: TSchemaFileFormat = "yaml"  # format in which to expect external schema
    external_schema_format_remove_defaults: bool = True  # remove default values when exporting schema