# Copyright 2015 Google Inc. All Rights Reserved.
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


from argparse import ArgumentParser
from fontmake.font_project import FontProject


def main():
    parser = ArgumentParser()
    parser.add_argument('glyphs_path', metavar='GLYPHS_PATH')
    parser.add_argument('-c', '--compatible', action='store_true')
    parser.add_argument('-i', '--interpolate', action='store_true')
    args = vars(parser.parse_args())

    glyphs_path = args.pop('glyphs_path')
    project = FontProject()
    project.run_all(glyphs_path, **args)


if __name__ == '__main__':
    main()
