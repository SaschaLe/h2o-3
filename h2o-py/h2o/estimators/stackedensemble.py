#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric, is_type


class H2OStackedEnsembleEstimator(H2OEstimator):
    """
    Stacked Ensemble

    Builds a stacked ensemble (aka "super learner") machine learning method that uses two
    or more H2O learning algorithms to improve predictive performance. It is a loss-based
    supervised learning method that finds the optimal combination of a collection of prediction
    algorithms.This method supports regression and binary classification.

    Examples
    --------
      >>> import h2o
      >>> h2o.init()
      >>> from h2o.estimators.random_forest import H2ORandomForestEstimator
      >>> from h2o.estimators.gbm import H2OGradientBoostingEstimator
      >>> from h2o.estimators.stackedensemble import H2OStackedEnsembleEstimator
      >>> col_types = ["numeric", "numeric", "numeric", "enum", "enum", "numeric", "numeric", "numeric", "numeric"]
      >>> data = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/prostate/prostate.csv", col_types=col_types)
      >>> train, test = data.split_frame(ratios=[.8], seed=1)
      >>> x = ["CAPSULE","GLEASON","RACE","DPROS","DCAPS","PSA","VOL"]
      >>> y = "AGE"
      >>> nfolds = 5
      >>> my_gbm = H2OGradientBoostingEstimator(nfolds=nfolds, fold_assignment="Modulo", keep_cross_validation_predictions=True)
      >>> my_gbm.train(x=x, y=y, training_frame=train)
      >>> my_rf = H2ORandomForestEstimator(nfolds=nfolds, fold_assignment="Modulo", keep_cross_validation_predictions=True)
      >>> my_rf.train(x=x, y=y, training_frame=train)
      >>> stack = H2OStackedEnsembleEstimator(model_id="my_ensemble", training_frame=train, validation_frame=test, base_models=[my_gbm.model_id, my_rf.model_id])
      >>> stack.train(x=x, y=y, training_frame=train, validation_frame=test)
      >>> stack.model_performance()
    """

    algo = "stackedensemble"

    def __init__(self, **kwargs):
        super(H2OStackedEnsembleEstimator, self).__init__()
        self._parms = {}
        names_list = {"model_id", "training_frame", "response_column", "validation_frame", "base_models",
                      "keep_levelone_frame"}
        if "Lambda" in kwargs: kwargs["lambda_"] = kwargs.pop("Lambda")
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in names_list:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))
        self._parms["_rest_version"] = 99

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``H2OFrame``.
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        assert_is_type(training_frame, None, H2OFrame)
        self._parms["training_frame"] = training_frame


    @property
    def response_column(self):
        """
        Response variable column.

        Type: ``str``.
        """
        return self._parms.get("response_column")

    @response_column.setter
    def response_column(self, response_column):
        assert_is_type(response_column, None, str)
        self._parms["response_column"] = response_column


    @property
    def validation_frame(self):
        """
        Id of the validation data frame.

        Type: ``H2OFrame``.
        """
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        assert_is_type(validation_frame, None, H2OFrame)
        self._parms["validation_frame"] = validation_frame


    @property
    def base_models(self):
        """
        List of model ids which we can stack together. Models must have been cross-validated using nfolds > 1, and folds
        must be identical across models.

        Type: ``List[str]``  (default: ``[]``).
        """
        return self._parms.get("base_models")

    @base_models.setter
    def base_models(self, base_models):
         if is_type(base_models,[H2OEstimator]):
            base_models = [b.model_id for b in base_models]
            self._parms["base_models"] = base_models
         else:
            assert_is_type(base_models, None, [str])
            self._parms["base_models"] = base_models


    @property
    def keep_levelone_frame(self):
        """
        Keep level one frame used for metalearner training.

        Type: ``bool``  (default: ``False``).
        """
        return self._parms.get("keep_levelone_frame")

    @keep_levelone_frame.setter
    def keep_levelone_frame(self, keep_levelone_frame):
        assert_is_type(keep_levelone_frame, None, bool)
        self._parms["keep_levelone_frame"] = keep_levelone_frame


