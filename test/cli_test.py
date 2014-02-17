import subprocess
import yaml

def tla_result_fixture(zone_number):
    return {
        "score": 0,
        "present": True,
        "disqualified": False,
        "zone": zone_number,
    }

def test_run_the_template():
    process = subprocess.Popen(["./score.py",  "templates/yaml_template.yaml"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retcode = process.wait()
    if retcode != 0:
        print process.stderr.read()

    assert retcode == 0

    result = process.stdout.reads()
    result_dict = yaml.load(result)


    assert result_dict["version"] == "1.0.0"
    assert result_dict["match_number"] == 0
    assert result_dict["scores"] == {
        "TLA1": tla_result_fixture(0),
        "TLA2": tla_result_fixture(1),
        "TLA3": tla_result_fixture(2),
        "TLA4": tla_result_fixture(3),
    }


