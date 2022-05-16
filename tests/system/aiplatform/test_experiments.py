# -*- coding: utf-8 -*-

# Copyright 2021 Google LLC
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
import pytest

from google.api_core import exceptions

from google.cloud import aiplatform
from tests.system.aiplatform import e2e_base


PARAMS = {"sdk-param-test-1": 0.1, "sdk-param-test-2": 0.2}

METRICS = {"sdk-metric-test-1": 0.8, "sdk-metric-test-2": 100}

PARAMS_2 = {"sdk-param-test-1": 0.2, "sdk-param-test-2": 0.4}

METRICS_2 = {"sdk-metric-test-1": 1.6, "sdk-metric-test-2": 200}


class TestExperiments(e2e_base.TestEndToEnd):

    _temp_prefix = "tmpvrtxsdk-e2e"

    def setup_class(cls):
        cls._experiment_name = cls._make_display_name("experiment")[:30]

    def test_create_experiment(self, shared_state):

        # Truncating the name because of resource id constraints from the service

        tensorboard = aiplatform.Tensorboard.create(
            project=e2e_base._PROJECT,
            location=e2e_base._LOCATION,
            display_name=self._experiment_name)

        shared_state['resources'] = [tensorboard]

        aiplatform.init(
            project=e2e_base._PROJECT,
            location=e2e_base._LOCATION,
            experiment=self._experiment_name,
            experiment_tensorboard=tensorboard
        )

        shared_state["resources"].append(aiplatform.metadata.experiment_tracker.experiment)

    def test_get_experiment(self):
        experiment = aiplatform.Experiment(experiment_name=self._experiment_name)
        assert experiment.name == self._experiment_name

    def test_delete_experiment(self):
        experiment = aiplatform.Experiment(experiment_name=self._experiment_name)
        experiment.delete(delete_backing_tensorboard_runs=True)

        with pytest.raises(exceptions.NotFound):
            aiplatform.Experiment(experiment_name=self._experiment_name)


        # # Truncating the name because of resource id constraints from the service
        # run_name_1 = self._make_display_name("run")[:30]
        # aiplatform.start_run(run_name_1)
        #
        # shared_state["resources"].extend(
        #     [
        #         aiplatform.metadata.metadata_service._run,
        #         aiplatform.metadata.metadata_service._metrics,
        #         aiplatform.metadata.metadata_service._experiment_run,
        #     ]
        # )
        #
        # aiplatform.log_params(PARAMS)
        # aiplatform.log_metrics(METRICS)
        #
        # run_name_2 = self._make_display_name("run")[:30]
        # aiplatform.start_run(run_name_2)
        #
        # shared_state["resources"].extend(
        #     [
        #         aiplatform.metadata.metadata_service._run,
        #         aiplatform.metadata.metadata_service._metrics,
        #         aiplatform.metadata.metadata_service._experiment_run,
        #     ]
        # )
        #
        # aiplatform.log_params(PARAMS_2)
        # aiplatform.log_metrics(METRICS_2)
        #
        # df = aiplatform.get_experiment_df()
        #
        # true_df_dict_1 = {f"metric.{key}": value for key, value in METRICS.items()}
        # for key, value in PARAMS.items():
        #     true_df_dict_1[f"param.{key}"] = value
        #
        # true_df_dict_1["experiment_name"] = experiment_name
        # true_df_dict_1["run_name"] = run_name_1
        #
        # true_df_dict_2 = {f"metric.{key}": value for key, value in METRICS_2.items()}
        # for key, value in PARAMS_2.items():
        #     true_df_dict_2[f"param.{key}"] = value
        #
        # true_df_dict_2["experiment_name"] = experiment_name
        # true_df_dict_2["run_name"] = run_name_2
        #
        # assert sorted(
        #     [true_df_dict_1, true_df_dict_2], key=lambda d: d["run_name"]
        # ) == sorted(df.to_dict("records"), key=lambda d: d["run_name"])