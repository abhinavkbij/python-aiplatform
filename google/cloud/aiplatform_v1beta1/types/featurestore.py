# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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


from google.protobuf import timestamp_pb2 as timestamp  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.aiplatform.v1beta1',
    manifest={
        'Featurestore',
    },
)


class Featurestore(proto.Message):
    r"""Featurestore configuration information on how the
    Featurestore is configured.

    Attributes:
        name (str):
            Output only. Name of the Featurestore. Format:
            ``projects/{project}/locations/{location}/featurestores/{featurestore}``
        display_name (str):
            Required. The user-defined name of the
            Featurestore. The name can be up to 128
            characters long and can consist of any UTF-8
            characters.
            Display name of a Featurestore must be unique
            within a single Project and Location Pair.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this Featurestore
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this Featurestore
            was last updated.
        etag (str):
            Optional. Used to perform consistent read-
            odify-write updates. If not set, a blind
            "overwrite" update happens.
        labels (Sequence[google.cloud.aiplatform_v1beta1.types.Featurestore.LabelsEntry]):
            Optional. The labels with user-defined
            metadata to organize your Featurestore.
            Label keys and values can be no longer than 64
            characters (Unicode codepoints), can only
            contain lowercase letters, numeric characters,
            underscores and dashes. International characters
            are allowed.
            See https://goo.gl/xmQnxf for more information
            on and examples of labels. No more than 64 user
            labels can be associated with one
            Featurestore(System labels are excluded)."
            System reserved label keys are prefixed with
            "aiplatform.googleapis.com/" and are immutable.
        online_serving_config (google.cloud.aiplatform_v1beta1.types.Featurestore.OnlineServingConfig):
            Required. Config for online serving
            resources.
        state (google.cloud.aiplatform_v1beta1.types.Featurestore.State):
            Output only. State of the featurestore.
    """
    class State(proto.Enum):
        r"""Possible states a Featurestore can have."""
        STATE_UNSPECIFIED = 0
        STABLE = 1
        UPDATING = 2

    class OnlineServingConfig(proto.Message):
        r"""OnlineServingConfig specifies the details for provisioning
        online serving resources.

        Attributes:
            fixed_node_count (int):
                Required. The number of nodes for each
                cluster. The number of nodes will not scale
                automatically but can be scaled manually by
                providing different values when updating.
            max_online_serving_size (int):
                Maximum number of feature values per entity
                that will be stored in online serving storage.
                The Featurestore will retain the latest feature
                values per entity and periodically remove any
                older feature values. It can take up to a day
                before the older feature values are deleted.
                Storage infrastructure cost is propotional to
                this value. Recommend to set to the largest
                number of versions (i.e last-k) needed at online
                serving time. If not set, default to 1.
        """

        fixed_node_count = proto.Field(proto.INT32, number=2)

        max_online_serving_size = proto.Field(proto.INT32, number=3)

    name = proto.Field(proto.STRING, number=1)

    display_name = proto.Field(proto.STRING, number=2)

    create_time = proto.Field(proto.MESSAGE, number=3,
        message=timestamp.Timestamp,
    )

    update_time = proto.Field(proto.MESSAGE, number=4,
        message=timestamp.Timestamp,
    )

    etag = proto.Field(proto.STRING, number=5)

    labels = proto.MapField(proto.STRING, proto.STRING, number=6)

    online_serving_config = proto.Field(proto.MESSAGE, number=7,
        message=OnlineServingConfig,
    )

    state = proto.Field(proto.ENUM, number=8,
        enum=State,
    )


__all__ = tuple(sorted(__protobuf__.manifest))