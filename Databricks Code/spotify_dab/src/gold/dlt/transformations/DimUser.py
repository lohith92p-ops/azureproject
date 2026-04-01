import dlt
from pyspark.sql.functions import col

expectations = {"rule_1":col("user_id").isNotNull()}


@dlt.table
@dlt.expect_all_or_drop(expectations)
def dimuser_stag():
    df = spark.readStream.table("spotify_cata.silver.dimuser")
    return df

dlt.create_streaming_table("dimuser")

dlt.create_auto_cdc_flow(
    target="dimuser",
    source="dimuser_stag",
    keys=["user_id"],
    sequence_by="updated_at",
    stored_as_scd_type=2,
    track_history_except_column_list = None,
    name = None,
    once= False

)