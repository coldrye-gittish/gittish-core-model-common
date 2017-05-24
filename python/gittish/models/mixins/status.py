# Copyright 2017 Carsten Klein
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from sqlalchemy import Column
from sqlalchemy.types import Integer


__all__ =
[
  'StatusMixin'
]


class StatusMixin:

  _status = Column('status', Integer, nullable = False)

  # Concrete classes need to define this to be the enum class
  # used for representing the status value
  # __status_class__ = None

  @property
  def status(self):
    return self.__class__.__status_class__(self._status)

  @status.setter
  def status(self, value):
    self._status = int(self.__class__.__status_class__(value))


# vim: expandtab:ts=2:sw=2:
