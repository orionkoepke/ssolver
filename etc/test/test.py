#! /usr/bin/env python3

import argparse
import configparser
import os
import unittest


def get_project_root_dir_path():
    return os.path.join(
        os.path.dirname(__file__),
        "../.."
    )


def get_path_to_config_file():
    return os.path.join(
        get_project_root_dir_path(),
        "etc/test/test.cfg"
    )


def get_configs():
    config_file_path = get_path_to_config_file()

    if os.path.isfile(config_file_path) and os.access(config_file_path, os.R_OK):
        configs = configparser.ConfigParser()
        configs.read(get_path_to_config_file())

    else:
        raise FileNotFoundError(
            "Test config file not found at path %s with read permissions."
            % os.path.abspath(config_file_path)
        )

    return configs


def run_unit_tests():
    configs = get_configs()

    unit_test_dir_path = os.path.join(
        get_project_root_dir_path(),
        configs.get("Unit Tests", "unit test dir path", fallback="tests")
    )

    if not os.path.isdir(unit_test_dir_path):
        raise NotADirectoryError(
            "Could not find a directory that contained unit tests at %s."
            % os.path.abspath(unit_test_dir_path)
        )

    else:
        test_loader = unittest.TestLoader()
        tests = test_loader.discover(
            start_dir=unit_test_dir_path,
            pattern=configs.get("Unit Tests", "unit test file name pattern"),
            top_level_dir=os.path.join(get_project_root_dir_path())
        )

        test_runner = unittest.TextTestRunner()
        return test_runner.run(tests)


def get_argument_parser():
    parser = argparse.ArgumentParser(
        description="This program runs testing for this project."
    )

    return parser


def run(args=None):
    parser = get_argument_parser()

    parser.parse_args(args=args)

    results = run_unit_tests()

    if len(results.errors) > 0 or len(results.failures) > 0:
        exit(1)

    else:
        exit(0)


if __name__ == "__main__":
    run()
