# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from marshmallow import Schema, fields, post_dump, post_load

from polyaxon_schemas.base import BaseConfig


class BuildJobSchema(Schema):
    config = fields.Dict(allow_none=True)

    class Meta:
        ordered = True

    @post_load
    def make(self, data):
        return BuildJobConfig(**data)

    @post_dump
    def unmake(self, data):
        return BuildJobConfig.remove_reduced_attrs(data)


class BuildJobConfig(BaseConfig):
    SCHEMA = BuildJobSchema
    IDENTIFIER = 'build_job'

    def __init__(self, config=None):
        self.config = config  # The json compiled content of this experiment