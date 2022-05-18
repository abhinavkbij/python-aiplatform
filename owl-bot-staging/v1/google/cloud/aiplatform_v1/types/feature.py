# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.cloud.aiplatform_v1.types import feature_monitoring_stats
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.aiplatform.v1',
    manifest={
        'Feature',
    },
)


class Feature(proto.Message):
    r"""Feature Metadata information that describes an attribute of
    an entity type. For example, apple is an entity type, and color
    is a feature that describes apple.

    Attributes:
        name (str):
            Immutable. Name of the Feature. Format:
            ``projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}``

            The last part feature is assigned by the client. The feature
            can be up to 64 characters long and can consist only of
            ASCII Latin letters A-Z and a-z, underscore(_), and ASCII
            digits 0-9 starting with a letter. The value will be unique
            given an entity type.
        description (str):
            Description of the Feature.
        value_type (google.cloud.aiplatform_v1.types.Feature.ValueType):
            Required. Immutable. Type of Feature value.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this EntityType
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this EntityType
            was most recently updated.
        labels (Mapping[str, str]):
            Optional. The labels with user-defined
            metadata to organize your Features.
            Label keys and values can be no longer than 64
            characters (Unicode codepoints), can only
            contain lowercase letters, numeric characters,
            underscores and dashes. International characters
            are allowed.
            See https://goo.gl/xmQnxf for more information
            on and examples of labels. No more than 64 user
            labels can be associated with one Feature
            (System labels are excluded)."
            System reserved label keys are prefixed with
            "aiplatform.googleapis.com/" and are immutable.
        etag (str):
            Used to perform a consistent
            read-modify-write updates. If not set, a blind
            "overwrite" update happens.
        disable_monitoring (bool):
            Optional. If not set, use the monitoring_config defined for
            the EntityType this Feature belongs to. Only Features with
            type
            ([Feature.ValueType][google.cloud.aiplatform.v1.Feature.ValueType])
            BOOL, STRING, DOUBLE or INT64 can enable monitoring.

            If set to true, all types of data monitoring are disabled
            despite the config on EntityType.
        monitoring_stats_anomalies (Sequence[google.cloud.aiplatform_v1.types.Feature.MonitoringStatsAnomaly]):
            Output only. The list of historical stats and
            anomalies with specified objectives.
    """
    class ValueType(proto.Enum):
        r"""An enum representing the value type of a feature."""
        VALUE_TYPE_UNSPECIFIED = 0
        BOOL = 1
        BOOL_ARRAY = 2
        DOUBLE = 3
        DOUBLE_ARRAY = 4
        INT64 = 9
        INT64_ARRAY = 10
        STRING = 11
        STRING_ARRAY = 12
        BYTES = 13

    class MonitoringStatsAnomaly(proto.Message):
        r"""A list of historical [Snapshot
        Analysis][FeaturestoreMonitoringConfig.SnapshotAnalysis] or [Import
        Feature Analysis]
        [FeaturestoreMonitoringConfig.ImportFeatureAnalysis] stats requested
        by user, sorted by
        [FeatureStatsAnomaly.start_time][google.cloud.aiplatform.v1.FeatureStatsAnomaly.start_time]
        descending.

        Attributes:
            objective (google.cloud.aiplatform_v1.types.Feature.MonitoringStatsAnomaly.Objective):
                Output only. The objective for each stats.
            feature_stats_anomaly (google.cloud.aiplatform_v1.types.FeatureStatsAnomaly):
                Output only. The stats and anomalies
                generated at specific timestamp.
        """
        class Objective(proto.Enum):
            r"""If the objective in the request is both
            Import Feature Analysis and Snapshot Analysis, this objective
            could be one of them. Otherwise, this objective should be the
            same as the objective in the request.
            """
            OBJECTIVE_UNSPECIFIED = 0
            IMPORT_FEATURE_ANALYSIS = 1
            SNAPSHOT_ANALYSIS = 2

        objective = proto.Field(
            proto.ENUM,
            number=1,
            enum='Feature.MonitoringStatsAnomaly.Objective',
        )
        feature_stats_anomaly = proto.Field(
            proto.MESSAGE,
            number=2,
            message=feature_monitoring_stats.FeatureStatsAnomaly,
        )

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    description = proto.Field(
        proto.STRING,
        number=2,
    )
    value_type = proto.Field(
        proto.ENUM,
        number=3,
        enum=ValueType,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    etag = proto.Field(
        proto.STRING,
        number=7,
    )
    disable_monitoring = proto.Field(
        proto.BOOL,
        number=12,
    )
    monitoring_stats_anomalies = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=MonitoringStatsAnomaly,
    )


__all__ = tuple(sorted(__protobuf__.manifest))