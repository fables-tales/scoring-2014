
import os
import subprocess
import yaml

def tla_result_fixture(zone_number):
    return {
        "score": 0,
        "present": True,
        "disqualified": False,
        "zone": zone_number,
    }

def run(relative_path):
    process = subprocess.Popen(["./score.py",  relative_path], \
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retcode = process.wait()
    return retcode, process

def assert_run(relative_path):
    retcode, process = run(relative_path)
    if retcode != 0:
        print process.stderr.read()

    assert retcode == 0, "Bad return code scoring '{0}'.".format(relative_path)

    result = process.stdout.reads()
    result_dict = yaml.load(result)
    return result_dict

def test_run_the_template():
    result_dict = assert_run("templates/yaml_template.yaml")

    assert result_dict["version"] == "1.0.0"
    assert result_dict["match_number"] == 0
    assert result_dict["scores"] == {
        "TLA1": tla_result_fixture(0),
        "TLA2": tla_result_fixture(1),
        "TLA3": tla_result_fixture(2),
        "TLA4": tla_result_fixture(3),
    }

def check_by_input_file(input_name):
    input_file = os.path.join("test/data", input_name)
    output_file = os.path.join("test/data", input_name[:-5] + '.out.yaml')

    assert os.path.exists(output_file), "Missing output expectation '{1}' for input '{0}'.".format(input_name, output_file)

    expected_output = yaml.load(open(output_file).read())
    output = assert_run(input_file)

    assert output == expected_output

def test_input_file():
    files = os.listdir("test/data")
    outputs = [f for f in files if f.endswith('.out.yaml')]
    inputs = [f for f in files if f.endswith('.yaml') and not f in outputs]

    for input_name in inputs:
        yield check_by_input_file, input_name
