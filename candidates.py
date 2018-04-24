import requests
import json

url = "http://qainterview.cogniance.com/candidates"

class ListCandidates:
    def get(self):
        get_candidates = requests.get(url)
        return get_candidates
        
class Candidate:
    def get(self, cid):
        get_candidate = requests.get(url+r'/'+str(cid))
        return get_candidate
        
    def post(self, name, position):
        data={'name': name,
              'position': position}
        new_candidate = requests.post(url,
                                     headers={'content-type': 'application/json'},
                                     data=json.dumps(data))
        return new_candidate

    def delete(self, cid):
        delete_candidate = requests.delete(url+r'/'+str(cid),
                                           headers={'content-type': 'application/json'},
                                           data=json.dumps(data))
        return delete_candidate
