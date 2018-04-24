import pytest
from candidates import Candidate

@pytest.mark.parametrize('cid', range(82,100))
def test_candidate_status_code_get(cid):
        assert Candidate().get(cid).status_code == 200
    
def test_candidate_status_code_post():
        assert Candidate().post('Olga', 'Junior Automation QA').status_code == 201

@pytest.mark.parametrize('cid', range(82,100))
def test_candidate_status_code_delete(cid):
        assert Candidate().delete(cid).status_code == 200
